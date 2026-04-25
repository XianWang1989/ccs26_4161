
from flask import Flask, request, render_template_string
from flask_wtf import FlaskForm
from wtforms import FieldList, FormField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class ItemForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])

class MyListForm(FlaskForm):
    mylist = FieldList(FormField(ItemForm), min_entries=1)
    submit = SubmitField('Submit')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm()
    if form.validate_on_submit():
        # process the validated data
        return 'Success: {}'.format([item.item.data for item in form.mylist])
    return render_template_string('''
        <form method="post" action="/doit">
            {{ form.mylist }} 
            <input type="submit" value="Submit">
        </form>
    ''', form=form)

if __name__ == '__main__':
    app.run(debug=True)
