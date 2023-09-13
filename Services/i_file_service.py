from abc import ABC, abstractmethod
from note import Note

class IFileService(ABC):
    @abstractmethod
    def __private_readJSON(self):
        pass

    @abstractmethod
    def __private_findByIdInJSON(self, id: int):
        pass

    @abstractmethod
    def __private_writeJSON(self, data: list):
        pass

    @abstractmethod
    def __private_takeID(self):
        pass

    @abstractmethod
    def printJSON(self):
        pass

    @abstractmethod
    def addNote(self, note: Note):
        pass

    @abstractmethod
    def editNote(self):
        pass

    @abstractmethod
    def removeFromJSON(self):
        pass
