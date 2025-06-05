import psycopg2
from psycopg2 import Error
import sqlite3
import os

# PostgreSQL database connection parameters, I kan bare ændre disse til jeres egne
# Husk at installere requirements.txt filen med pip install -r requirements.txt




connection_params = {
    'host': 'localhost',
    'database': 'projecttest',  
    'user': 'postgres',         
    'password': 'pin1dt4e',     
    'port': '5432'
}   

def init_db():
    """Initialize the database by executing the SQL script."""
    try:
        connection = psycopg2.connect(**connection_params)
        cursor = connection.cursor()
        
        # Open and read the SQL file
        with open("Database.sql", "r") as file:
            sql_script = file.read()
        
        # Execute the SQL script
        cursor.execute(sql_script)
        connection.commit()
        
        print("Database initialized successfully.")
    
    except (Exception, Error) as error:
        print(f"Error while initializing database: {error}")
    
    finally:
        if connection:
            cursor.close()
            connection.close()
       

def select_data(table_name,rows):

        connection = psycopg2.connect(**connection_params)
        cursor = connection.cursor()
        
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"Connected to: {db_version[0]}\n")

        query = f"""
        SELECT {rows} FROM {table_name} 
        """
        cursor.execute(query)
        
        # Fetch column names
        column_names = [desc[0] for desc in cursor.description]
        print(f"Columns: {', '.join(column_names)}")
        print("-" * 50)
        
        # Fetch and print all results
        records = cursor.fetchall()
        print(records)

def add_user(name, email, phone_nr, password):
        query = f"""
        INSERT INTO users (name, email, phone_nr, password)
        VALUES ('{name}', '{email}', {phone_nr},' {password}'); 
        """
        print(query)
        return query

def update_user(user_id, name, email, phone_nr):
        connection = psycopg2.connect(**connection_params)
        cursor = connection.cursor()
        
        query = """
        UPDATE users 
        SET name = %s, email = %s, phone_nr = %s 
        WHERE id = %s
        """
        cursor.execute(query, (name, email, phone_nr, user_id))
        connection.commit()
        
        print(f"User {user_id} updated successfully.")

def delete_user(user_id):
        connection = psycopg2.connect(**connection_params)
        cursor = connection.cursor()
        
        query = """
        DELETE FROM users 
        WHERE id = %s
        """
        cursor.execute(query, (user_id,))
        connection.commit()
        
        print(f"User {user_id} deleted successfully.")

def get_user(user_id):
        connection = psycopg2.connect(**connection_params)
        cursor = connection.cursor()
        
        query = """
        SELECT * FROM users 
        WHERE id = %s
        """
        cursor.execute(query, (user_id,))
        
        user = cursor.fetchone()
        if user:
            print(f"User {user_id} found: {user}")
        else:
            print(f"User {user_id} not found.")
        
        return user

def update_event(event_id, title, artist, date, venue, price, category):
        connection = psycopg2.connect(**connection_params)
        cursor = connection.cursor()
        
        query = """
        UPDATE events 
        SET title = %s, artist = %s, date = %s, venue = %s, price = %s, category = %s 
        WHERE id = %s
        """
        cursor.execute(query, (title, artist, date, venue, price, category, event_id))
        connection.commit()
        
        print(f"Event {event_id} updated successfully.")

def update_event2(event_id, column, new_value):
        connection = psycopg2.connect(**connection_params)
        cursor = connection.cursor()
        
        query = f"""
        UPDATE events 
        SET {column} = %s 
        WHERE id = %s
        """
        cursor.execute(query, (new_value, event_id))
        connection.commit()
        
        print(f"Event {event_id} updated successfully.")

def delete_ticket(ticket_id):
        connection = psycopg2.connect(**connection_params)
        cursor = connection.cursor()
        
        query = """
        DELETE FROM tickets 
        WHERE id = %s
        """
        cursor.execute(query, (ticket_id,))
        connection.commit()
        
        print(f"Ticket {ticket_id} deleted successfully.")



    


    