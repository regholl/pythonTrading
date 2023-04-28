from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class user(base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    # add fields as columns, specify type
    un = Column(String)
    pw = Column(String)

    def __init__(self, username, password):
        self.un = username
        self.pw = password
    
# security(aka stock)
# positions
# balances
# trades


