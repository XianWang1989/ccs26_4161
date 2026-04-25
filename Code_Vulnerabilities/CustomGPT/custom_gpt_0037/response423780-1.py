
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, validators
from wtforms.validators import ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'


class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)

    def validate_mylist(form, field):
        if not field.data or all(item == '' for item in field.data):
            raise ValidationError('At least one item must be filled.')


@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm(csrf_enabled=False)

    if request.method == 'POST':
        form.mylist.process(data=request.form.getlist('mylist'))
        if form.validate():
            # Process the valid data
            return f'Valid items: {form.mylist.data}'

    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
