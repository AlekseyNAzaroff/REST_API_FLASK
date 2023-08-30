from model.user import User


class Comment:
    def __init__(self, post_id: str, text: str, author: User):
        self.post_id = post_id
        self.text = text
        self.author = author
