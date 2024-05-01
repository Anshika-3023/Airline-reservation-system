from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///ARS.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class User(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    name=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(200),nullable=False)
    phone=db.Column(db.String(200),nullable=False)
    message=db.Column(db.String(500),nullable=True)
    flight=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} -{self.flight}"

@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hello, World!'



if __name__=="__main__":
    app.run(debug=True,port=8000)