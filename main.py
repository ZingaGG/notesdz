from note import Note
from services.note_service import NoteService 
from services.file_service import FileService

def main():
    file_name = "notes.json"
    noteService = NoteService()
    fileService = FileService() 

    while True:
        print("Hello! Input operation (add, read, edit, delete, stop)")
        operation = input().lower()

        match operation:
            # Добавить заметку
            case "add":
                # Создание заметки
                note = noteService.createNote()
                print()
                print("Note creation success!")
                print()
                # Добавление в файл
                fileService.addNote(note)

            # Вывод всех существующих заметок
            case "read":
                fileService.printJSON()

            # Редактирование по id
            case "edit":
                fileService.editNote()
            
            # Удалить по id 
            case "delete":
                fileService.removeFromJSON()

            case "stop":
                print("Exitinig...")
                break

main()

# Сделать тесты