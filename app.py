import sqlite3
from flask import Flask, render_template, request, g, session, redirect, url_for
import os
import queryscript as qs
import regex as re
import testDataCreator as tdc


app = Flask(__name__)

# Database sti
os.remove('music_events.db') if os.path.exists('music_events.db') else None  # Slet gammel database hvis den findes
DATABASE = 'music_events.db'


def get_db():
    """Få database forbindelse"""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  # Gør at vi kan bruge kolonnenavne
    return db


@app.teardown_appcontext
def close_connection(exception):
    """Luk database forbindelse"""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def get_all_users_credentials():
    """Hent alle brugeres emails og passwords fra database"""
    db = get_db()
    users = db.execute('SELECT email, password FROM users').fetchall()
    
    # Convert to list of dictionaries for easier handling

    user_list = []
    for user in users:
        user_list.append({
            'email': user['email'],
            'password': user['password']
        })
    
    return user_list


def get_all_users_safe():
    db = get_db()
    users = db.execute('SELECT name, email, phone_nr, password FROM users').fetchall()
    
    user_list = []
    for user in users:
        user_list.append({
            'name': user['name'],
            'email': user['email'],
            'phone_nr': user['phone_nr'],
            'password': user['password']  
        })
    
    return user_list

def verify_user_login(email, password):
    """Verificer bruger login (sikker måde)"""
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
    
    if user and user['password'] == password:  # In production, use password hashing!
        return True
    return False

# If you want to use it in a route:
@app.route('/admin/users')
def admin_users():
    """Admin route to view all users (without passwords)"""
    users = get_all_users_safe()
    return render_template('admin_users.html', users=users)

def init_db():
    """Opret database og indsæt test data"""
    
    if not os.path.exists(DATABASE):
        print("Opretter database...")
        db = sqlite3.connect(DATABASE)
        
        with open("VS-DIS/Database.sql", "r") as sql_file:
            content = sql_file.read()
        # Opret tabel
        
        pattern = re.compile(r'(?s)(.*?;)(?=\s*(--|$))', re.MULTILINE | re.DOTALL)
        statements = pattern.findall(content)

        # Extract only the matched statements
        statements = [stmt[0].strip() for stmt in statements]
     
        for statement in statements:
            
            db.execute(f'''
                {statement}
            ''')

        testuserlist=tdc.fakeToSQL()    
        for user in testuserlist:
            db.execute(user)

        db.commit()
        db.close()
        print("Database oprettet med test data!")


def get_all_events():
    """Hent alle events fra database"""
    db = get_db()
    events = db.execute('SELECT * FROM events ORDER BY date').fetchall()
    return events

def search_events(query):
    """Søg efter events"""
    db = get_db()
    search_term = f'%{query}%'
    events = db.execute('''
        SELECT * FROM events 
        WHERE artist_name LIKE ? OR venue LIKE ? OR genre LIKE ?
        ORDER BY date
    ''', (search_term, search_term, search_term)).fetchall()
    return events


@app.route('/editEvents', methods=['GET', 'POST'])
def edit_events():
    event_id = request.form.get('event_id')

    return render_template('editEvents.html',currentUser=currentUser,events=get_all_events(),event_id=event_id)

@app.route('/')
def index():
    """Forside - vis alle events eller søgeresultater"""
    query = request.args.get('search', '').strip()

    if query:
        events = search_events(query)
        message = f'Søgeresultater for "{query}" ({len(events)} events fundet)'
    else:
        events = get_all_events()
        message = f'Alle kommende events ({len(events)} events)'
    
    print(f"Antal events: {len(events)}")  # Debug print
    print(f"Template variabler: query='{query}', message='{message}'")  # Debug print
    if currentUser == 'None':
        return render_template('index.html', events=events, query=query, message=message)
    if currentUser != 'None':
        return render_template('index.html', events=events, query=query, message=message, currentUser=currentUser)


#@app.route(f'edit-events?event_id={1}', methods=['GET', 'POST'])

@app.route('/newuser', methods=['GET', 'POST'])
def newuser():

    """Håndter formular for ny bruger"""
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')
    
    if not name or not email or not phone or not password:
        return render_template('newuser.html', error='Alle felter skal udfyldes.')
    
    
    # Her kan du tilføje logik for at gemme brugeren i databasen
    print(f"Ny bruger oprettet: {name}, {email}, {phone}, {password}")
    db= get_db()
    db.execute(f'''
                {qs.add_user(name, email, phone, password)}
            ''')
    db.commit()
    db.close()
    return render_template('succes.html', success='Bruger oprettet!') 

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login"""
    email = request.form.get('email')
    password = request.form.get('password')
    if verify_user_login(email, password):
        print(f"Bruger {email} logget ind.")
        currentUser = email  # Gem nuværende bruger i en global variabel
        return render_template('index.html', success='Login succesfuldt!', currentUser=currentUser,query='', events=get_all_events())
    else:
        print(f"Login mislykkedes for {email}.")
        return render_template('login.html', error='Forkert email eller adgangskode.')

    return render_template('login.html')
    


@app.template_filter('format_price')
def format_price(price):
    """Formatér pris"""
    if price == 0:
        return "Gratis"
    return f"{price} kr"

@app.template_filter('format_date')
def format_date(date_string):
    """Formatér dato til dansk"""
    try:
        from datetime import datetime
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        months = {
            1: 'jan', 2: 'feb', 3: 'mar', 4: 'apr',
            5: 'maj', 6: 'jun', 7: 'jul', 8: 'aug',
            9: 'sep', 10: 'okt', 11: 'nov', 12: 'dec'
        }
        return f"{date_obj.day}. {months[date_obj.month]} {date_obj.year}"
    except:
        return date_string

if __name__ == '__main__':
    # Opret database hvis den ikke findes

    init_db()   

    # Start Flask app
    print("Starter Flask app...")
    print("Åbn http://127.0.0.1:5000 i din browser")
    currentUser = None
    app.run(debug=True)
