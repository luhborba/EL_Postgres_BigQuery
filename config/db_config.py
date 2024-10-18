"""Conexão com o PostgreSQL e BigQuery."""
import psycopg2 as pg
from google.cloud import bigquery
from environs import Env

env = Env()
env.read_env()

def get_db_connection_postgres():
    """Conexão com o PostgreSQL."""
    try:
        conn = pg.connect(
            host=env.str("POSTGRES_HOST"),
            database=env.str("POSTGRES_DATABASE"),
            user=env.str("POSTGRES_USER"),
            password=env.str("POSTGRES_PASSWORD"),
            port=env.str("POSTGRES_PORT"),
        )
            
        return conn
    except Exception as e:
        print(f"Conexão Falhou, {e}")
        return None
    
def get_db_connection_bigquery():
    """Conexão com o BigQuery."""
    try:
        client = bigquery.Client()
        return client
    except Exception as e:
        print(f"Conexão Falhou, {e}")
        return None
