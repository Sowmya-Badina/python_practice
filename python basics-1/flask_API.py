from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "ana"},
    {"id": 2, "name": "kate"}
]

@app.route('/')
def hello():
    return "welcome User!"

@app.route('/users', methods=['GET'])
def home():
    return jsonify({users})

@app.route('/users', methods=['POST'])
def enter_user_name():
    input_data = request.get_json()
    new_user = {
        'id': len(users) + 1,
        'name': input_data['name']
    }
    users.append(new_user)
    return jsonify({'message':'new_user created'})

@app.route('/users/<int:int>', methods=['GET'])
def get_user_data(int):
    for i in users:
        if i['id'] == int:
            return jsonify(i)
    return jsonify({'error':'user not found'})


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_data(user_id):

    user=next(u for u in users if u['id']==user_id)
    if user is None:
        return jsonify({'error':'user not found'})


    users.remove(user)
    return jsonify({'message':'user deleted'})
if __name__ == '__main__':
    app.run(debug=True)
