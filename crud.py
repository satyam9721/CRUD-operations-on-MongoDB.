import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine #ModuleNotFoundError: No module named 'flask_mongoengine' = (venv) C:\flaskmyproject>pip install flask-mongoengine
 
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'project',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)
 
class User(db.Document):
    name = db.StringField()
    email = db.StringField()
    def to_json(self):
        return {"name": self.name,
                "email": self.email}
 
@app.route('/')
def query_records():
    name = 'Satyamgupta'
    user = User.objects(name=name).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())
 
@app.route('/add')
def create_record():
    user = User(name='Caite',
                email='caite@gmail.com')
    user.save()
    return jsonify(user.to_json())
 
@app.route('/update')
def update_record():
    name = 'Satyamgupta'
    user = User.objects(name=name).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.update(email='emailupdate@gmail.com')
    return jsonify(user.to_json())
     
@app.route('/delete')
def delete_record():
    name = 'Caite'
    user = User.objects(name=name).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.delete()
    return jsonify(user.to_json())
     
if __name__ == "__main__":
    app.run(debug=True)