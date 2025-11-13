from base_table import BaseTable
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import *
import datetime

class Orders(BaseTable):
    __tablename__ = 'Orders'

    ID: Mapped[BaseTable.type_annotation_map['IID']]
    Name: Mapped[str]
    Age: Mapped[int]
    CreatedOn: Mapped[datetime.datetime] = mapped_column(server_default=text('CURRENT_TIMESTAMP'))
    UpdatedOn: Mapped[datetime.datetime] = mapped_column(server_default=text('CURRENT_TIMESTAMP'), onupdate=datetime.datetime.now())