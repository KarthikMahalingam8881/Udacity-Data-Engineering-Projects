import configparser
import psycopg2

config = configparser.ConfigParser()
config.read('dwh.cfg')

try:
    conn = psycopg2.connect(
        host=config['CLUSTER']['HOST'],
        dbname=config['CLUSTER']['DB_NAME'],
        user=config['CLUSTER']['DB_USER'],
        password=config['CLUSTER']['DB_PASSWORD'],
        port=config['CLUSTER']['DB_PORT']
    )
    print("✅ Connected to Redshift!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
