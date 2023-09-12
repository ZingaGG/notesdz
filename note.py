import datetime

class note:
    def __init__(self, id, title, text, time):
        self.id = id
        self.title = title
        self.text = text
        self.time = datetime.datetime.now() 

    