from connection import Connection
from session_builder import SessionBuilder
from connection import Connection
from base_table import BaseTable
from table.users import Users

session = SessionBuilder(
    Connection(
        server='localhost',
        port=5432,
        user='postgres',
        password='<PASSWORD>',
        db_name='test',
        sql_type='postgres',
    ),
).build()

BaseTable.metadata.drop_all(session.engine)
BaseTable.metadata.create_all(session.engine)