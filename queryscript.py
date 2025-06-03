import psycopg2
from psycopg2 import Error

# PostgreSQL database connection parameters, I kan bare ændre disse til jeres egne
# Husk at installere requirements.txt filen med pip install -r requirements.txt
connection_params = {
    'host': 'localhost',
    'database': 'projecttest',  
    'user': 'postgres',         
    'password': 'pin1dt4e',     
    'port': '5432'
}   

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

def add_user(name, email, phone_nr):
        connection = psycopg2.connect(**connection_params)
        cursor = connection.cursor()
        
        query = """
        INSERT INTO users (name, email, phone_nr) 
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (name, email, phone_nr))
        connection.commit()
        
        print(f"User {name} added successfully.")



#choice = input("\nEnter your choice (1-3): ").strip()
#if choice == '':
    #select_data('users','*')   
#if choice == '1':
        #add_user('Samuel','zfc990@alumni.ku.dk','93402508')
        


    


    