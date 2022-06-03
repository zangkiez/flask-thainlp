from flask import Flask, request, jsonify
from pythainlp import word_tokenize, collate
import json

app = Flask(__name__)


@app.route("/")
def hello():
    data_show = {'count': [], 'word': []}
    q = request.args.get('q')
    list_word = word_tokenize(q, keep_whitespace=False)
    count_number = len(list_word)
    data_show['count'].append(count_number)
    data_show['word'].append(collate(list_word))
    # print(json.dumps(data_show))
    return jsonify(data_show)

# if __name__ == "__main__":
#     app.run(port=5000, debug=False, host='0.0.0.0')
