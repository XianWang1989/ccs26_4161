
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, Validators

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[Validators.InputRequired()]), min_entries=1)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        # Process the form data
        items = form.mylist.data
        return redirect(url_for('success', items=items))
    return render_template('index.html', form=form)

@app.route('/success')
def success():
    items = request.args.getlist('items')
    return f'Success! Your items: {", ".join(items)}'

if __name__ == '__main__':
    app.run(debug=True)
