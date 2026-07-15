from abc import ABC
from abc import abstractmethod


class BaseAction(ABC):

    @abstractmethod
    def execute(self, command):
        pass