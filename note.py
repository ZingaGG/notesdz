import datetime

class Note:

    def __init__(self,id :int, title: str, text: str):
        self.id = id
        self.title = title
        self.text = text
        self.date = datetime.datetime.now() 
    
    def toString(self):
        print("Id = ", self.id)
        print("Title = ", self.title)
        print("Text = ", self.text)
        print("Date = ", self.date)

    