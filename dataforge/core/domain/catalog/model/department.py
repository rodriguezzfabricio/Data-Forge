from sqlalchemy import Column, String
from dataforge.core.domain.base import Base

class Department(Base):
    __tablename__ = 'departments'

    id = Column(String, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"<Department(id='{self.id}', name='{self.name}')>"
