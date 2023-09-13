from abc import ABC, abstractmethod
from note import Note

class IFileService(ABC):
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
