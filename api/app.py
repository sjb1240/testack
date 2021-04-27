from flask import Flask, jsonify, request
import matrix
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})


@app.route('/vXs', methods=['POST'])
def vector_times_scalar():
    mat1 = request.args.get('vector')
    n = int(request.args.get('scalar'))
    v1 = list(map(int, mat1.split(',')))
    x = matrix.multiply_vector_by_scalar(v1, n)
    return jsonify({'data': 'done', 'result': x})


@app.route('/mXs', methods=['POST'])
def matrix_times_scalar():
    content = request.json
    m = content['m']
    n = content['n']
    x = matrix.multiply_matrix_by_scalar(m, n)
    return jsonify({'data': 'done', 'result': x})


@app.route('/mXm', methods=['POST'])
def matrix_times_matrix():
    content = request.json
    print(content)
    m1 = content['m1']
    m2 = content['m2']
    result = matrix.multiply_matrix_by_matrix(m1, m2)
    return jsonify({'result': result})


@app.route('/tm', methods=['POST'])
def translate_matrix():
    content = request.json
    m1 = content['m1']
    result = matrix.transpose(m1)
    return jsonify({'result': result})


# driver function
if __name__ == '__main__':
    app.run(debug=True)
