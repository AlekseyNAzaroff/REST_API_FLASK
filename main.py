from flask import Flask, jsonify, request
from flask.json.provider import DefaultJSONProvider
from model.post import Post
from model.comment import Comment
from model.storage import Storage

storage = Storage()


class CustomJSONProvider(DefaultJSONProvider): #кастомный json-декодер для версии flsk 2.3
    @staticmethod
    def default(obj):
        if isinstance(obj, Post):
            return {'body': obj.text, 'author': obj.author,
                    'comments': obj.comments}
        elif isinstance(obj, Comment):
            return {'text': obj.text,
                    'author': obj.author}
        else:
            return DefaultJSONProvider.default(obj)


app = Flask(__name__)

app.json = CustomJSONProvider(app)


@app.route('/post/', methods=['POST']) #контроллер создания поста
def create_post():
    post_json = request.get_json()
    post = Post(post_json['text'], post_json['author'])
    post_id = storage.add_in_storage(post)
    return jsonify({'status': 'success', 'msg': f'id {post_id} added'})


@app.route('/post/<post_id>/', methods=['GET']) #контроллер просмотра поста
def read_post(post_id):
    return jsonify(storage.read_post(post_id))


@app.route('/post/', methods=['GET']) #контроллер просмотра всех постов
def read_posts():
    return jsonify(storage.read_posts())


@app.route('/post/<post_id>/', methods=['PUT'])  #контроллер изменения поста
def update_post(post_id):
    post_json = request.get_json()
    post = Post(post_json['text'], post_json['author'])
    storage.update_post(post_id, post)
    return jsonify({'status': 'success', 'msg': f'id {post_id} update'})


@app.route('/post/<post_id>/', methods=['DELETE'])   #контроллер удаления поста
def delete_post(post_id):
    storage.delete_post(post_id)
    return jsonify({'status': 'success', 'msg': f'id {post_id} delete'})


@app.route('/post/<post_id>/', methods=['POST'])   #контроллер создания комментария
def create_comment(post_id):
    comment_json = request.get_json()
    comment = Comment(post_id, comment_json['text'],
                      comment_json['author'])
    storage.create_comment(post_id, comment)
    return jsonify(
        {'status': 'success', 'msg': f'Comment to the post {post_id} created'})


if __name__ == '__main__':
    app.run(debug=True)
