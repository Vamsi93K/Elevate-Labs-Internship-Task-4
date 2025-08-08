from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and Email are required'})
    
    user_id = str(len(users) + 1)
    users[user_id] = {
        "id":user_id,
        "name":data['name'],
        "email":data['email']
    }
    return jsonify(users[user_id]), 201

@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(list(users.values())), 200

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'error' : 'User not found'}), 404

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'error':'user not found'}), 404
    data = request.get_json()
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    return jsonify(user), 200

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({'message':"user deleted"}),200
    return jsonify({"error":'user not found'}),404

if __name__ == '__main__':
    app.run(debug=True)