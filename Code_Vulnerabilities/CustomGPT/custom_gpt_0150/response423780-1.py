
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with your secret key

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)

    def validate_mylist(form, field):
        if not field.data or all(not item for item in field.data):
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm(request.form)
    if request.method == 'POST' and form.validate():
        return 'Form submitted with items: ' + ', '.join(form.mylist.data)
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
