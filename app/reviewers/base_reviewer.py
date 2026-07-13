from abc import ABC
from abc import abstractmethod


class BaseReviewer(ABC):

    @abstractmethod
    def review(self, content: str):

        pass
