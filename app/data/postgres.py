from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# default connection string from local docker instance
connection_string = "postgresql+psycopg2://postgres:postgres@db:5432"

engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)

Base = declarative_base()