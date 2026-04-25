
from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(self, field):
        if not field.data or len(field.data) == 0:
            raise ValidationError('At least one item is required!')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyListForm()
    if form.validate_on_submit():
        # Process your valid inputs here
        return redirect('/success')  # Redirect after successful POST

    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
