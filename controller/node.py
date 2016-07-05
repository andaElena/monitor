from base import *
from sqlalchemy import Column, Integer, String, Float

class Node(Base):
	"""Groups the informations about one machine."""
	__tablename__='node'

	id = Column(Integer,primary_key=True)
	ipAdress = Column(String(32))
	totalDiskSpace = Column(Float)
	freeDiskSpace = Column(Float)
	cpuLoad = Column(String(32))
	totalMemory = Column(Float)
	freeMemory = Column(Float)