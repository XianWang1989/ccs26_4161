
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, validators

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[validators.Optional()]), min_entries=1)

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        # Form processing logic here
        return "Form submitted successfully!"

    return render_template('form.html', form=form)

@app.route('/')
def index():
    form = MyForm()
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
