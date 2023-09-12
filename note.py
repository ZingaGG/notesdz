import datetime

class Note:
    id = 1

    def __init__(self, title, text):
        self.id = Note.id
        self.title = title
        self.text = text
        self.date = datetime.datetime.now() 
        Note.id += 1
    
    def toString(self):
        print("Id = ", self.id)
        print("Title = ", self.title)
        print("Text = ", self.text)
        print("Date = ", self.date)

    