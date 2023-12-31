from .i_file_service import IFileService
from note import Note
import json

class FileService(IFileService):
    fileName = "notes.json"

    def readJSON(self):
        try:
            with open(self.fileName, "r") as file:
                try:
                    data = json.load(file)
                    return data
                except json.decoder.JSONDecodeError:
                    data = []
                    return data
        except FileNotFoundError as e:
            print(f"Файл {self.fileName} не существует. Создаем новый файл.")
            with open(self.fileName, "w") as file:
                json.dump([], file)  # Создаем пустой JSON файл
            return []
            
    def _findByIdInJSON(self, id: int):
        data = self.readJSON()
        for el in data:
            if el.get("id") == id:
                return el

    def _writeJSON(self, data: list):
        with open(self.fileName, "w") as file:
            json.dump(data, file, default=str, indent=2)

    def _takeID(self):
        data = self.readJSON()
        while True:
            try:
                print("Input note id: ")
                id = int(input())
                if(id <= 0 or id > len(data)):
                    raise IndexError("No note with such index")
                return id
            except ValueError as e:
                print(e)
                print("Enter valid id!")
            except IndexError as e:
                print(e)
                print("Enter valid id!")
                self._takeID
            
    def printJSON(self):
        data = self.readJSON()
        for el in data:
            print()
            print(el)
            print()

    def addNote(self, note: Note):
        note_dict = {"id": note.id, "title": note.title, "text": note.text, "date": note.date}

        data = self.readJSON()
        data.append(note_dict)

        with open(self.fileName, "w") as file:
            json.dump(data, file, default=str, indent=2)

    def editNote(self):
        data = self.readJSON()
        id = self._takeID()
        noteToEdit = self._findByIdInJSON(id)

        while True:
            print("Input attribute you want to change (title, text)")
            attribute = input().lower()
            
            try:
                if attribute != "title" and attribute != "text":
                    raise AttributeError("Wrong attribute!")
                print("Input new info")
                newData = input()
                noteToEdit.update({attribute: newData})
                print("Updated note: ")
                print(noteToEdit)

                # Запись обновленного списка заметок
                data.pop(id - 1)
                data.insert(id - 1, noteToEdit)
                self._writeJSON(data)

                print()
                print("Success edit!")
                print()
                break
            except AttributeError as e:
                print(e)
                print("Restarting edition...")

    def removeFromJSON(self):
        data = self.readJSON()
        id = self._takeID()
        data.pop(id - 1)

        for i in range(len(data)):
            data[i]["id"] = i + 1

        self._writeJSON(data)

        print("Note deleted!")
