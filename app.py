from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ARS.db'
db = SQLAlchemy(app)

class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    flight = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

    def __repr__(self) -> str:
        return f"{self.sno} -{self.flight}"

@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hello, World!'



if __name__=="__main__":
    app.run(debug=True,port=8000)