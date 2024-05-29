import psycopg2
from config import DB_CONFIG

def init_db():
    conn = psycopg2.connect(**DB_CONFIG)
    print('к баззе данных подключен')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS file_movements (
                   id SERIAL PRIMARY KEY,
                   filename TEXT,
                   src TEXT,
                   dest TEXT,
                   timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()

def log_movement(filename, src, dest):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO file_movements (filename, src, dest)
                   VALUES (%s, %s, %s)''', (filename, src, dest))
    conn.commit()
    conn.close

