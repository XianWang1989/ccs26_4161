
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item'))
    submit = SubmitField('Submit')

    def validate_mylist(self, mylist):
        if not mylist.data or all(item == '' for item in mylist.data):
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if form.validate_on_submit():
        # Process the data
        return f"Received: {form.mylist.data}"

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
