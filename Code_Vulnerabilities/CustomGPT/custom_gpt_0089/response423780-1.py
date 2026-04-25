
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyListForm(FlaskForm):
    mylist = FieldList(
        StringField('Item', validators=[DataRequired()]),
        min_entries=1
    )

    def validate_mylist(form, field):
        if not field.data:
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm()
    if form.validate_on_submit():
        # Process the valid data
        items = form.mylist.data
        return f'Items: {items}'
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run()
