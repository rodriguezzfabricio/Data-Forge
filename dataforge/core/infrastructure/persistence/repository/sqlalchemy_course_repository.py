from sqlalchemy.orm import Session
from dataforge.core.domain.catalog.model.course import Course
from dataforge.core.domain.catalog.repository.course_repository import CourseRepository

class SqlAlchemyCourseRepository(CourseRepository):

    def __init__(self, session: Session):
        self.session = session

    def save(self, course: Course) -> Course:
        self.session.add(course)
        self.session.commit()
        self.session.refresh(course)
        return course

    def find_by_id(self, course_id: str) -> Course:
        return self.session.query(Course).filter(Course.id == course_id).first()
