from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Ashvi1112@localhost/TodoApplicationDatabase'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Ashvi%401234@127.0.0.1:3306/TodoApplicationDatabase'
SQLALCHEMY_DATABASE_URI = 'sqlite:///todos.db'
engine = create_engine(SQLALCHEMY_DATABASE_URI,connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

 