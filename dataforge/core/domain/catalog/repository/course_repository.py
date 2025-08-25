from abc import ABC, abstractmethod
from dataforge.core.domain.catalog.model.course import Course

class CourseRepository(ABC):

    @abstractmethod
    def save(self, course: Course) -> Course:
        pass

    @abstractmethod
    def find_by_id(self, course_id: str) -> Course:
        pass
