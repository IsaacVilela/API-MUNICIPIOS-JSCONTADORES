from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class MUNICIPIOS(Base):
    __tablename__ = "munic"

    codigo = Column(Integer, primary_key=True)
    descricao = Column(String)