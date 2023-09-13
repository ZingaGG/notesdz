from .i_file_service import IFileService
from note import Note
import json

class FileService(IFileService):
    fileName = "notes.json"

    def __private_readJSON(self):
        with open(self.fileName, "r") as file:
            try:
                data = json.load(file)
                return data
            except json.decoder.JSONDecodeError:
                data = []
                return data
            
    def __private_findByIdInJSON(self, id: int):
        data = self.__private_readJSON()
        try:
            for el in data:
                if el.get("id") == id:
                    return el
                else:
                    raise IndexError("No note with such index")
        except IndexError as e:
            print(e)


    def __private_writeJSON(self, data: list):
        with open(self.fileName, "w") as file:
            json.dump(data, file, default=str, indent=2)

    def __private_takeID(self):
        while True:
            try:
                print("Input note id you want to change")
                id = int(input())
                return id
            except ValueError as e:
                print(e)
                print("Enter valid id!")
            
    def printJSON(self):
        data = self.__private_readJSON()
        for el in data:
            print(el)

    def addNote(self, note: Note):
        note_dict = {"id": note.id, "title": note.title, "text": note.text, "date": note.date}

        data = self.__private_readJSON()
        data.append(note_dict)

        with open(self.fileName, "w") as file:
            json.dump(data, file, default=str, indent=2)

    def editNote(self):
        data = self.__private_readJSON()
        id = self.__private_takeID()
        noteToEdit = self.__private_findByIdInJSON(id)

        while True:
            print("Input attribute you want to change(title, text)")
            attribute = input().lower()
            
            try:
                if(attribute != "title" and attribute != "text"):
                    raise AttributeError("Wrong attribute!")
                print("Input new info")
                newData = input()
                noteToEdit.update({attribute: newData})
                print("Updated note: ")
                print(noteToEdit)

                # Запись обнволенного листа заметок
                data.pop(id - 1)
                data.insert(id-1, noteToEdit)
                self.__private_writeJSON(data)

                
                print()
                print("Success edit!")
                print()
                break
            except AttributeError as e:
                print(e)
                print("Restarting edition...")

    def removeFromJSON(self):
        data = self.__private_readJSON()
        id = self.__private_takeID
        data.pop(id - 1)
        self.__private_writeJSON(data)

        # Реализовать обновление индексов

        print("Note deleted!")
