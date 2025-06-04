import psycopg2
from flask import Flask, render_template, request, g
import os
import queryscript as qs


app = Flask(__name__)

# Database sti
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

def init_db():
    """Opret database og indsæt test data"""
    if not os.path.exists(DATABASE):
        print("Opretter database...")
        db = sqlite3.connect(DATABASE)
        
        # Opret tabel
        db.execute('''
            CREATE TABLE events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                artist TEXT NOT NULL,
                date TEXT NOT NULL,
                venue TEXT NOT NULL,
                price INTEGER NOT NULL,
                category TEXT NOT NULL
            )
        ''')
        
        # Indsæt test data
        events_data = [
            ('Mew - Triumf Tour', 'Mew', '2025-06-15', 'Vega, København', 450, 'Rock'),
            ('Roskilde Festival 2025', 'Forskellige kunstnere', '2025-06-28', 'Roskilde', 2100, 'Festival'),
            ('Copenhagen Jazz Festival', 'Jazz kunstnere', '2025-07-04', 'Forskellige venues', 200, 'Jazz'),
            ('Lukas Graham - Comeback', 'Lukas Graham', '2025-08-22', 'Royal Arena', 395, 'Pop'),
            ('Distortion Festival', 'Electronic Artists', '2025-06-01', 'København', 0, 'Electronic'),
            ('Volbeat - European Tour', 'Volbeat', '2025-07-10', 'Parken, København', 650, 'Rock'),
            ('Trentemøller Live', 'Trentemøller', '2025-05-15', 'Vega, København', 350, 'Electronic'),
            ('Agnes Obel Concert', 'Agnes Obel', '2025-09-05', 'DR Koncerthuset', 400, 'Alternative'),
            ('Medina - Comeback Tour', 'Medina', '2025-06-20', 'Forum, København', 375, 'Pop'),
            ('Copenhagen Opera Gala', 'Operasangere', '2025-08-15', 'Operaen', 500, 'Klassisk')
        ]
        
        db.executemany('''
            INSERT INTO events (title, artist, date, venue, price, category)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', events_data)
        
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
        WHERE title LIKE ? OR artist LIKE ? OR venue LIKE ? OR category LIKE ?
        ORDER BY date
    ''', (search_term, search_term, search_term, search_term)).fetchall()
    return events

@app.route('/')
def index():
    """Forside - vis alle events eller søgeresultater"""
    query = request.args.get('search', '').strip()
    
    print(f"Søgeord: '{query}'")  # Debug print
    
    if query:
        events = search_events(query)
        message = f'Søgeresultater for "{query}" ({len(events)} events fundet)'
    else:
        events = get_all_events()
        message = f'Alle kommende events ({len(events)} events)'
    
    print(f"Antal events: {len(events)}")  # Debug print
    print(f"Template variabler: query='{query}', message='{message}'")  # Debug print
    
    return render_template('index.html', events=events, query=query, message=message)

@app.route('/newuser', methods=['GET', 'POST'])
def newuser():

    """Håndter formular for ny bruger"""
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    
    if not name or not email or not phone:
        return render_template('newuser.html', error='Alle felter skal udfyldes.')
    
    
    # Her kan du tilføje logik for at gemme brugeren i databasen
    print(f"Ny bruger oprettet: {name}, {email}, {phone}")
    qs.add_user(name, email, phone)  
    
    return render_template('succes.html', success='Bruger oprettet!') 

@app.route('/login')
def login():
    """Opret ny bruger """
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
    app.run(debug=True)
