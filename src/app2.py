from sqlalchemy import create_engine, Column, INTEGER, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///CarDataRelation.db', echo = True)
engine.connect()

Base = declarative_base()

class Car(Base):
    __tablename__ = 'carsinfo'

    id = Column(INTEGER, primary_key=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    price = Column(Float)
    qty = Column(INTEGER)

    customer_id = Column(INTEGER, ForeignKey('cutomerinfo.id'))

    customers = relationship('Customer', back_populates = 'owner')

class Customer(Base):
    __tablename__ = 'customerinfo'

    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(INTEGER, nullable=False)

    owner = relationship('Car', back_populates='customers')

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
SessionLocal = Session()