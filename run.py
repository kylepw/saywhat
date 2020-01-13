"""Run on production server.

    Usage:
        $ gunicorn run:app


"""
from dotenv import load_dotenv
from saywhat import create_app

load_dotenv('.env')

app = create_app()
