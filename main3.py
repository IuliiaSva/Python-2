from session_builder import SessionBuilder
from connection import Connection
from table.sellers import SellersDTO
from fastapi import FastAPI

app = FastAPI()

@app.get('/sellers')
def run():
    session = SessionBuilder(
        Connection(
            server='localhost',
            port=5432,
            user='postgres',
            password='<PASSWORD>',
            db_name='test',
            sql_type='postgresSQL'
        )
    )
    session = session.build()
    results = session.query(SellersDTO).all()
    return results

@app.get('/sellers/{id}')
async def get_seller(id: int):
    session = SessionBuilder(
        Connection(
            server='localhost',
            port=5432,
            user='postgres',
            password='<PASSWORD>',
            db_name='test',
            sql_type='postgresSQL'
        )
    )
    session = session.build()
    if id in session.query(SellersDTO).all():
        return session.query(SellersDTO).get(id)
    else:
        return ('Not found')

@app.put('/sellers/{id}/update')
async def get_seller(id: int):
    session = SessionBuilder(
        Connection(
            server='localhost',
            port=5432,
            user='postgres',
            password='<PASSWORD>',
            db_name='test',
            sql_type='postgresSQL'
        )
    )
    session = session.build()
    if id in session.query(SellersDTO).all():
        session.query(SellersDTO).get(id).name = "Новое"
        session.query(SellersDTO).get(id).age = "15"
    return session.query(SellersDTO).get(id)