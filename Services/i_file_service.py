from abc import ABC, abstractmethod
from note import Note

class IFileService(ABC):
    @abstractmethod
    def addNote(self, note: Note):
        pass
