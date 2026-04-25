
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for CSRF protection

class ArrayForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]), min_entries=1)

    def validate_mylist(self, field):
        if not field.data or len(field.data) == 0:
            raise ValidationError("You must provide at least one item.")

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = ArrayForm()

    if form.validate_on_submit():
        # Process the validated data
        return "Form submitted successfully!"

    return render_template('form_template.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
