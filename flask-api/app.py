from flask import Flask, jsonify, request
from connection import listB, getByStudy
import secrets

app = Flask(__name__)

app.secret_key = secrets.token_hex(16)

@app.route('/list', methods=['GET'])
def get_list():
    items = listB()
    return jsonify(items=items)

@app.route('/study', methods=['GET'])
def get_study():
    study_name = request.args.get('study_name')
    if study_name:
        study_data = getByStudy(study_name)
        if study_data:
            return jsonify(study_data)
        else:
            return jsonify({'message': 'Study not found'}), 404
    else:
        return jsonify({'message': 'Missing study_name parameter'}), 400


if __name__ == '__main__':
    app.run(debug=True)