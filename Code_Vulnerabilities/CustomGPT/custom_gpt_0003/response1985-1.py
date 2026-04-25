
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

# Define a model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    # Fetch all items from the database
    items = Item.query.all()
    return render_template('index.html', items=items)

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)
