import json

from flask import Flask, jsonify, request

from model.twit import Twit

from flask.json.provider import DefaultJSONProvider

twits = []


class CustomJSONProvider(DefaultJSONProvider):
    @staticmethod
    def default(obj):
        if isinstance(obj, Twit):
            return {'body': obj.body, 'author': obj.author}
        else:
            return DefaultJSONProvider.default(obj)


app = Flask(__name__)

app.json = CustomJSONProvider(app)


@app.route('/twit', methods=['POST'])
def create_twit():
    '''{"body": "Hello world", "author": "@aqaguy"}
    '''
    twit_json = request.get_json()
    twit = Twit(twit_json['body'], twit_json['author'])
    twits.append(twit)
    return jsonify({'status': 'success'})


@app.route('/twit', methods=['GET'])
def read_twits():
    return jsonify({'twits': twits})


if __name__ == '__main__':
    app.run(debug=True)
