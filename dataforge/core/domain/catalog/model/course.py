from sqlalchemy import Column, String, Integer, ForeignKey
from dataforge.core.domain.base import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(String, primary_key=True)
    title = Column(String)
    capacity = Column(Integer)
    department_id = Column(String, ForeignKey('departments.id'))

    def __repr__(self):
        return f"<Course(id='{self.id}', title='{self.title}')>"
