from abc import ABC, abstractmethod
class INoteService(ABC):

    @abstractmethod
    def createNote(self):
        pass
