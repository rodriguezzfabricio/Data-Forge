from sqlalchemy.orm import Session
from dataforge.core.domain.enrollment.model.enrollment import Enrollment
from dataforge.core.domain.enrollment.repository.enrollment_repository import EnrollmentRepository

class SqlAlchemyEnrollmentRepository(EnrollmentRepository):

    def __init__(self, session: Session):
        self.session = session

    def save(self, enrollment: Enrollment) -> Enrollment:
        self.session.add(enrollment)
        self.session.commit()
        self.session.refresh(enrollment)
        return enrollment

    def find_by_id(self, enrollment_id: str) -> Enrollment:
        return self.session.query(Enrollment).filter(Enrollment.id == enrollment_id).first()
