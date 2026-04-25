
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]), min_entries=1)

    def validate_mylist(self, field):
        if not field.data or len(field.data) < 1:
            raise ValidationError("At least one item is required.")

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyListForm()
    if form.validate_on_submit():
        # Process valid form data
        return "Form submitted successfully with: " + ', '.join(form.mylist.data)
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
