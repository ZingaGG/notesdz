from .i_note_service import INoteService
from .file_service import FileService
from note import Note

class NoteService(INoteService):

    def createNote(self):
        idTaker = FileService()
        id = len(idTaker.readJSON()) + 1
        print("Input note title: ")
        title = input()
        print("Input note text: ")
        text = input()
        return Note(id, title, text)

