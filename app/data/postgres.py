from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import getenv

# default connection string from local docker instance
connection_string = getenv('POSTGRES_CONNECTION_STRING')
if connection_string:
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    Base = declarative_base()
else:
    print("Connection string not found")