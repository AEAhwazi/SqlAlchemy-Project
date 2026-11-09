from sqlalchemy import create_engine, Column, INTEGER, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///CarData.db', echo = True)
engine.connect()

Base = declarative_base()

class Car(Base):
    __tablename__ = 'carsinfo'

    id = Column(INTEGER, primary_key=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    price = Column(Float)
    qty = Column(INTEGER)


Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
SessionLocal = Session()

car1 = Car(brand = 'BMW', model = 'Grand', price = 5000000, qty = 20)
car2 = Car(brand = 'Caprice', model = 'B Class', price = 150000, qty = 10)

SessionLocal.add_all([car1, car2])

SessionLocal.commit()
