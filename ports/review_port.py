from abc import ABC, abstractmethod

class ReviewPort(ABC):

    @abstractmethod
    def add_review(self, review_data):
        pass