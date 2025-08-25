from abc import ABC, abstractmethod
from dataforge.core.domain.enrollment.model.enrollment import Enrollment

class EnrollmentRepository(ABC):

    @abstractmethod
    def save(self, enrollment: Enrollment) -> Enrollment:
        pass

    @abstractmethod
    def find_by_id(self, enrollment_id: str) -> Enrollment:
        pass
