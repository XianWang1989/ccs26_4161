
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    data_list = Data.query.all()
    return render_template('index.html', data=data_list)

if __name__ == '__main__':
    db.create_all()  # This creates the database tables
    app.run(debug=True)
