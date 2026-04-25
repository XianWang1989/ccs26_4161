
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[InputRequired()]), min_entries=1)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        # Process the submitted data
        items = form.mylist.data
        return redirect(url_for('success', items=items))
    return render_template('index.html', form=form)

@app.route('/success')
def success():
    items = request.args.getlist('items')
    return f"Submitted items: {', '.join(items)}"

if __name__ == '__main__':
    app.run(debug=True)
