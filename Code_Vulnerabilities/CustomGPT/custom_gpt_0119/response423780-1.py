
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, validators

app = Flask(__name__)
app.secret_key = 'your_secret_key'


class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[validators.Optional()]), min_entries=1)

    def validate_mylist(self, field):
        if not any(field.data):
            raise validators.ValidationError('At least one item is required.')


@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if form.validate_on_submit():
        # Process the valid data here
        items = form.mylist.data
        flash('Form submitted successfully!')
        return redirect(url_for('doit'))

    return render_template('form.html', form=form)


@app.route('/')
def index():
    form = MyForm()
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
