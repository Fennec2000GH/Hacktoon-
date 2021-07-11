
from sqlalchemy import create_engine, Table, Column, Integer, String, Time, MetaData
from pprint import pprint

engine = create_engine('', echo=True)
meta = MetaData()

command_history = Table(
   'command_history',
   meta, 
   Column('id', Integer, primary_key = True),
   Column('timestamp', Time) 
   Column('input', String), 
   Column('command', String) 
)

meta.create_all(engine)

# pprint(dir(Column))
