from dotenv import load_dotenv
import os

load_dotenv()
PASSWORD = os.getenv('PASSWORD')

class DevelopmentConfig:
  SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:{PASSWORD}@localhost/movie_db'
  CACHE_TYPE = 'SimpleCache'
  DEBUG = True