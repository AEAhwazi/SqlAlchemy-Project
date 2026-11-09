from sqlalchemy import create_engine, Column, INTEGER, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///UniverSity.db', echo=True)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'StudentTable'

    id = Column(INTEGER, primary_key=True)    
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=False)
    mark = Column(Float, unique=False)

    lessons = relationship('Lesson', back_populates='student')

class Lesson(Base):
    __tablename__ = 'LessonTable'

    id = Column(INTEGER, primary_key=True)
    title = Column(String, nullable=False)
    unit = Column(INTEGER, nullable=False)
    
    student_id = Column(INTEGER, ForeignKey('StudentTable.id'))
    student = relationship('Student', back_populates='lessons')

Base.metadata.create_all(engine)
SessinLocal = sessionmaker(bind=engine)


#def add_record_lesson(v_lesson_id: int, v_title: str, v_unit: float):
def add_record_lesson(v_title: str, v_unit: float):
    with SessinLocal() as session:
        #lesson = Lesson(lesson_id=v_lesson_id, title=v_title, unit=v_unit)
        lesson = Lesson(title=v_title, unit=v_unit)
        lesson = Lesson(title=v_title, unit=v_unit)
        session.add(lesson)
        session.commit()
        session.refresh(lesson)
        session.close()

        return lesson

#def add_record_student(v_student_id: int, v_name: str, v_gender: str, v_phone: str, v_address: str):
def add_record_student(v_name: str, v_gender: str, v_phone: str, v_address: str):

    with SessinLocal() as session:
        #student = Student(student_id=v_student_id, name=v_name, gender=v_gender, phone=v_phone, address=v_address)
        student = Student(name=v_name, gender=v_gender, phone=v_phone, address=v_address)
        session.add(student)
        session.commit()
        session.refresh(student)
        session.close()

        return student

def view_record_student(v_student_id: int):
    with SessinLocal() as session:
        student = session.query(Student).filter_by(id = v_student_id).first()
        if student is None:
            result = False
            return result

        else:
            result = (student.id,
                      student.name,
                      student.gender,
                      student.phone,
                      student.address)
            return result

def del_record_student(v_student_id: int):
    with SessinLocal() as session:
        student = session.query(Student).filter_by(id = v_student_id).first()

        if student is None:
            return False

        session.delete(student)
        session.commit()

        return True


#result = del_record_student(111)
#print(result)