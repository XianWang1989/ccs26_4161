
from flask import Flask, request, render_template_string
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[InputRequired()]), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(self, field):
        if len(field.data) == 0:
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if form.validate_on_submit():
        # Form is valid, process the data
        items = form.mylist.data
        return f'Success! Items: {items}'
    return render_template_string('''
        <form method="post" action="/doit">
            {{ form.mylist() }}
            <input type="text" name="mylist" value="one">
            <input type="text" name="mylist" value="two">
            <input type="text" name="mylist" value="three">
            <input type="text" name="mylist" value="four">
            <input type="submit" value="Submit">
        </form>
        {{ form.errors }}
    ''', form=form)

if __name__ == '__main__':
    app.run(debug=True)
