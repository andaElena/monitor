from node import *
from sqlalchemy import create_engine

def createSchema():
	"""Creates mysql schema to store data from nodes."""
	engine = create_engine('mysql://root:0000@localhost:3306')
	engine.execute('CREATE DATABASE IF NOT EXISTS monitordb')
	db_engine = create_engine('mysql://root:0000@localhost:3306/monitordb')
	Base.metadata.create_all(db_engine)
