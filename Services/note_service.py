from .i_note_service import INoteService
from note import Note

class NoteService(INoteService):
    def createNote(self):
        print("Input note title: ")
        title = input()
        print("Input note text: ")
        text = input()
        return Note(title, text)

