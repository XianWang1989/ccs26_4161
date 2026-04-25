
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(self, mylist):
        if len(mylist.data) < 1:
            raise ValidationError('You need to enter at least one item.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyListForm()
    if form.validate_on_submit():
        # Process the list
        items = form.mylist.data
        return f'Success! You submitted: {items}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
