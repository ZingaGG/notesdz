from .i_file_service import IFileService
from note import Note
import json

class FileService(IFileService):
    def addNote(self, note: Note):
        note_dict = {"id": note.id, "title": note.title, "text": note.text, "date": note.date}
        with open("notes.json", "a+") as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                data = []

            data.append(note_dict)

            json.dump(data, file, default=str, indent=2)
            file.write("\n")