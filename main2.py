from connection import Connection
from session_builder import SessionBuilder
from connection import Connection
from base_table import BaseTable
from table.orders import Orders
from table.producer import Producers
from table.products import Products

session = SessionBuilder(
    Connection(
        server='localhost',
        port=5432,
        user='postgres',
        password='<PASSWORD>',
        db_name='test',
        sql_type='postgres',
    ),
)


BaseTable.metadata.create_all(session.engine)