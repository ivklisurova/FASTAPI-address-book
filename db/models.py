from sqlalchemy.sql.sqltypes import Integer, String, Float
from sqlalchemy import Column

from db.database import Base


class DBAddress(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True, index=True)
    country = Column(String)
    city = Column(String)
    street_name = Column(String)
    street_number = Column(Integer)
    postal_code = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

