from .i_file_service import IFileService
from note import Note
import json

class FileService(IFileService):
    fileName = "notes.json"

    def readJSON(self):
        with open(self.fileName, "r") as file:
            try:
                data = json.load(file)
                return data
            except json.decoder.JSONDecodeError:
                data = []
                return data

    def addNote(self, note: Note):
        note_dict = {"id": note.id, "title": note.title, "text": note.text, "date": note.date}

        data = self.readJSON()
        data.append(note_dict)

        with open(self.fileName, "w") as file:
            json.dump(data, file, default=str, indent=2)