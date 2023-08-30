from .post import Post
from .comment import Comment


class Storage:
    def __init__(self):
        self.dict = {}
        self.counter_id = 0

    def add_in_storage(self, post: Post):
        self.counter_id += 1
        self.dict[str(self.counter_id)] = post
        return str(self.counter_id)

    def read_post(self, post_id: str):
        return self.dict[post_id]

    def read_posts(self):
        return self.dict

    def update_post(self, post_id: str, post: Post):
        self.dict[str(post_id)] = post

    def delete_post(self, post_id: str):
        del self.dict[post_id]

    def create_comment(self, post_id: str, comment: Comment):
        self.dict[post_id].comments.append(comment)
        return self.dict[post_id]

# d = {'1': {'id': '1', 'text': 'post 1', 'author': 'alex', 'comment': []},
#     '2': {'id': '2', 'text': 'post 2', 'author': 'alex', 'comment': []}
# }
