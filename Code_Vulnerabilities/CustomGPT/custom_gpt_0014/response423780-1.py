
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(self, field):
        if not field.data or all(not item for item in field.data):
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if form.validate_on_submit():
        # Process the validated data
        items = form.mylist.data
        return f"Received: {items}"
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
