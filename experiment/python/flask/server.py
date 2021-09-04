from flask import Flask, request, jsonify
import json
from models import db, FlaskModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'
db.init_app(app)


@app.after_request # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/flask', methods=['GET'])
def Index():
    flasks = FlaskModel.query.all()
    return jsonify({'data': [result.serialized for result in flasks]})


@app.route('/flask/create', methods=['POST', 'OPTIONS'])
def Create():
    request_body = json.loads(request.get_data())
    flask_name = request_body['flask_name']
    flask = FlaskModel(flask_name)
    db.session.add(flask)
    db.session.commit()
    return f"Done"


@app.route('/flask/<int:id>', methods=['PUT', 'OPTIONS'])
def Update(id):
    request_body = json.loads(request.get_data())
    flask_name = request_body['flask_name']
    update_task_now = FlaskModel.query.get_or_404(id)
    update_task_now.flask_name = flask_name

    try:
        db.session.commit()
        return f"Done"
    except:
        return f"Flask with id={id} doesn't exist"


@app.route('/flask/<int:id>', methods=['GET', 'OPTIONS'])
def RetrieveSingleFlask(id):
    flask = FlaskModel.query.filter_by(id=id).first()
    if flask:
        return jsonify(flask.serialized)
    return f"Flask with id={id} doesn't exist"


@app.route('/flask/<int:id>', methods=['DELETE'])
def Delete(id):
    flask = FlaskModel.query.filter_by(id=id).first()
    if flask:
        db.session.delete(flask)
        db.session.commit()
        return f"Done"
    return f"Flask with id={id} doesn't exist"



if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
