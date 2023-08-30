from model.user import User


class Post:
    def __init__(self, text: str, author: User):
        self.id = ''
        self.text = text
        self.author = author
        self.comments = []
