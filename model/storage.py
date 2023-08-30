from .post import Post
from .comment import Comment


class Storage:
    def __init__(self):
        self.dict = {}
        self.counter_id = 0

    def add_in_storage(self, post: Post):   #функция добавления поста в хранилище
        self.counter_id += 1
        self.dict[str(self.counter_id)] = post
        return str(self.counter_id)

    def read_post(self, post_id: str):    #функция чтения поста
        return self.dict[post_id]

    def read_posts(self):     #функция чтения всех постов
        return self.dict

    def update_post(self, post_id: str, post: Post):     #функция изменения поста
        self.dict[str(post_id)] = post

    def delete_post(self, post_id: str):     #функция удаления поста
        del self.dict[post_id]

    def create_comment(self, post_id: str, comment: Comment):     #функция создания комментария
        self.dict[post_id].comments.append(comment)
        return self.dict[post_id]
