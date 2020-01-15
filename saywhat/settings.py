"""Default configuration settings."""
import os

# Flask
SECRET_KEY = os.environ.get('SECRET_KEY')

# Twitter
API_KEY = os.environ.get('API_KEY')
API_SECRET_KEY = os.environ.get('API_SECRET_KEY')

# Postgresql
DATABASE = os.environ.get('DATABASE')
