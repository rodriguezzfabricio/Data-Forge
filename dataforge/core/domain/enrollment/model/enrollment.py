from sqlalchemy import Column, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from dataforge.core.domain.base import Base
import enum

class EnrollmentStatus(enum.Enum):
    PENDING = "PENDING"
    ENROLLED = "ENROLLED"
    DROPPED = "DROPPED"
    FAILED_PREREQUISITES = "FAILED_PREREQUISITES"
    FAILED_CAPACITY = "FAILED_CAPACITY"

class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(String, primary_key=True)
    student_id = Column(String, ForeignKey('students.id'))
    course_id = Column(String, ForeignKey('courses.id'))
    status = Column(Enum(EnrollmentStatus))

    student = relationship("Student")
    course = relationship("Course")

    def __repr__(self):
        return f"<Enrollment(id='{self.id}', student_id='{self.student_id}', course_id='{self.course_id}', status='{self.status}')>"
