from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Sample data - i virkeligheden ville dette komme fra en database
EVENTS_DATA = [
    {
        'id': 1,
        'title': 'Mew - Triumf Tour',
        'artist': 'Mew',
        'date': '2025-06-15',
        'time': '20:00',
        'venue': 'Vega, København',
        'price_from': 450,
        'category': 'Rock',
        'image_icon': '🎸',
        'description': 'Danmarks mest elskede indie rock band er tilbage med en triumferende tour'
    },
    {
        'id': 2,
        'title': 'Roskilde Festival 2025',
        'artist': 'Forskellige kunstnere',
        'date': '2025-06-28',
        'time': '12:00',
        'venue': 'Roskilde',
        'price_from': 2100,
        'category': 'Festival',
        'image_icon': '🎤',
        'description': 'Nordeuropas største musikfestival med internationale stjerner'
    },
    {
        'id': 3,
        'title': 'Copenhagen Jazz Festival',
        'artist': 'Forskellige kunstnere',
        'date': '2025-07-04',
        'time': '19:00',
        'venue': 'Forskellige venues',
        'price_from': 200,
        'category': 'Jazz',
        'image_icon': '🎹',
        'description': 'Ti dage med jazz i hele København'
    },
    {
        'id': 4,
        'title': 'Lukas Graham - Comeback',
        'artist': 'Lukas Graham',
        'date': '2025-08-22',
        'time': '20:00',
        'venue': 'Royal Arena, København',
        'price_from': 395,
        'category': 'Pop',
        'image_icon': '🎵',
        'description': 'Lukas Graham vender tilbage med nye sange og klassikere'
    },
    {
        'id': 5,
        'title': 'Distortion Festival',
        'artist': 'Electronic Artists',
        'date': '2025-06-01',
        'time': '14:00',
        'venue': 'København',
        'price_from': 0,
        'category': 'Electronic',
        'image_icon': '🎧',
        'description': 'Gratis gademusik festival i Københavns gader'
    },
    {
        'id': 6,
        'title': 'DR Koncerthuset - Klassisk Aften',
        'artist': 'DR Symfoniorkesteret',
        'date': '2025-07-15',
        'time': '19:30',
        'venue': 'DR Koncerthuset',
        'price_from': 150,
        'category': 'Klassisk',
        'image_icon': '🎻',
        'description': 'En aften med klassisk musik i smukke omgivelser'
    }
]

CATEGORIES = [
    {'name': 'Rock & Metal', 'icon': '🎸', 'slug': 'rock'},
    {'name': 'Pop & Chart', 'icon': '🎤', 'slug': 'pop'},
    {'name': 'Jazz & Blues', 'icon': '🎷', 'slug': 'jazz'},
    {'name': 'Electronic', 'icon': '🎧', 'slug': 'electronic'},
    {'name': 'Klassisk', 'icon': '🎻', 'slug': 'klassisk'},
    {'name': 'Festivaler', 'icon': '🎪', 'slug': 'festival'}
]

@app.route('/')
def index():
    """Startside med alle events"""
    return render_template('index.html', 
                         events=EVENTS_DATA, 
                         categories=CATEGORIES,
                         page_title="Find dine drømme koncerter")

@app.route('/search')
def search():
    """Søgefunktion for events"""
    query = request.args.get('q', '').lower()
    category = request.args.get('category', '').lower()
    
    filtered_events = EVENTS_DATA
    
    # Filtrer efter søgeord
    if query:
        filtered_events = [
            event for event in filtered_events 
            if query in event['title'].lower() or 
               query in event['artist'].lower() or 
               query in event['venue'].lower()
        ]
    
    # Filtrer efter kategori
    if category:
        filtered_events = [
            event for event in filtered_events 
            if event['category'].lower() == category
        ]
    
    return render_template('search_results.html', 
                         events=filtered_events, 
                         query=query,
                         category=category,
                         categories=CATEGORIES)

@app.route('/event/<int:event_id>')
def event_detail(event_id):
    """Detaljeside for et specifikt event"""
    event = next((e for e in EVENTS_DATA if e['id'] == event_id), None)
    if not event:
        return "Event ikke fundet", 404
    
    return render_template('event_detail.html', event=event)

@app.route('/category/<category_slug>')
def category_events(category_slug):
    """Vis events for en specifik kategori"""
    category_events = [
        event for event in EVENTS_DATA 
        if event['category'].lower() == category_slug.lower()
    ]
    
    category_name = next(
        (cat['name'] for cat in CATEGORIES if cat['slug'] == category_slug), 
        category_slug.title()
    )
    
    return render_template('category.html', 
                         events=category_events,
                         category_name=category_name,
                         categories=CATEGORIES)

@app.route('/api/events')
def api_events():
    """API endpoint for at hente events (til AJAX)"""
    return jsonify(EVENTS_DATA)

@app.template_filter('format_date')
def format_date(date_string):
    """Custom filter til at formatere datoer på dansk"""
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        months = {
            1: 'januar', 2: 'februar', 3: 'marts', 4: 'april',
            5: 'maj', 6: 'juni', 7: 'juli', 8: 'august',
            9: 'september', 10: 'oktober', 11: 'november', 12: 'december'
        }
        return f"{date_obj.day}. {months[date_obj.month]} {date_obj.year}"
    except:
        return date_string

@app.template_filter('format_price')
def format_price(price):
    """Custom filter til at formatere priser"""
    if price == 0:
        return "Gratis"
    return f"{price:,} kr".replace(',', '.')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
