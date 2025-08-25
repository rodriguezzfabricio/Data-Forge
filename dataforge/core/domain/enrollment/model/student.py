from sqlalchemy import Column, String
from dataforge.core.domain.base import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __repr__(self):
        return f"<Student(id='{self.id}', first_name='{self.first_name}', last_name='{self.last_name}')>"
