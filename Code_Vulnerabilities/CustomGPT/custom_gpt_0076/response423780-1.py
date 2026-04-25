
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError, SubmitField

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(form, field):
        if not any(field.data):
            raise ValidationError('At least one item is required.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyListForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        # Process the valid data
        mylist_data = form.mylist.data
        return f"Received items: {mylist_data}"
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
