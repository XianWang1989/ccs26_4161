
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'


class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(self, field):
        if not field.data or all(item.data == "" for item in field):
            raise ValidationError("At least one item is required.")


@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm()
    if form.validate_on_submit():
        # Process the valid data
        items = [item.data for item in form.mylist if item.data]
        return f"Received: {items}"
    return render_template('form.html', form=form)


@app.route('/')
def index():
    form = MyListForm()
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
