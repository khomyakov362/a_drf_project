from django.core.management import BaseCommand
import pyodbc
from config import settings

class Command(BaseCommand):

    def handle(self, *args, **options):
        ConnectionString = f"""
                            DRIVER={settings.DRIVER};
                            SERVER={settings.HOST};
                            DATABASE={settings.PAD_DATABASE};
                            UID={settings.USER};
                            PWD={settings.PASSWORD};
                            """
        try:
            conn = pyodbc.connect(ConnectionString)
        except pyodbc.Error as e:
            print(e)
        else:
            conn.autocommit = True
            try:
                conn.execute(fr'CREATE DATABASE {settings.DATABASE};')
            except pyodbc.Error as e:
                print(e)
            else:
                print(f'Database {settings.DATABASE} created successfully.')
