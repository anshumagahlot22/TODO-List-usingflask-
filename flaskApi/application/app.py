from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# instantiate flask object
app = Flask(__name__)

# set app config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# create db instance
db = SQLAlchemy(app)

# instanctiate ma
ma = Marshmallow(app)

# create model
class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    completed = db.Column(db.Boolean, nullable=False, default = False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


# create db schema class
class TodoListSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name','completed', 'date_created')


# instantiate schema objects for todolist and todolists
todolist_schema = TodoListSchema(many=False)
todolists_schema = TodoListSchema(many=True)

#handle errors
@app.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood'}), 400)


@app.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)


@app.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)

# add a todo
@app.route("/todolist", methods = ["POST"])
def add_todo():
    try:
        name = request.json['name']
        new_todo = TodoList(name=name)
        
        db.session.add(new_todo)
        db.session.commit()

        return todolist_schema.jsonify(new_todo)
    except Exception as e:
        return jsonify({"Error": "Invalid Request, please try again."})

#get todos
@app.route("/todolist", methods = ["GET"])
def get_todos():
    todos = TodoList.query.all()
    result_set = todolists_schema.dump(todos)
    return jsonify(result_set)


# get a specific todo
@app.route("/todolist/<int:id>", methods=["GET"])
def get_todo(id):
    todo = TodoList.query.get_or_404(int(id))
    return todolist_schema.jsonify(todo)


# update a todo
@app.route("/todolist/<int:id>", methods=["PUT"])
def update_todo(id):

    todo = TodoList.query.get_or_404(int(id))

    try:
        name = request.json['name']
        completed = request.json['completed']

        todo.name = name
        todo.completed = completed

        db.session.commit()
    except Exception as e:
        return jsonify({"Error": "Invalid request, please try again."})
        
    return todolist_schema.jsonify(todo)

# delete todo
@app.route("/todolist/<int:id>", methods=["DELETE"])
def delete_todo(id):
    todo = TodoList.query.get_or_404(int(id))
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"Success" : "Todo deleted."})

if __name__ == "__main__":
    app.run(debug = True)