
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class CustomListField(FieldList):
    def __init__(self, *args, **kwargs):
        super().__init__(StringField(), *args, **kwargs)

    def validate(self, form, extra_validators=[]):
        if not super().validate(form, extra_validators):
            return False
        # Custom validation: at least one item must be filled in
        if not any(field.data for field in self.entries):
            raise ValidationError("You must provide at least one item.")
        return True

class MyForm(FlaskForm):
    mylist = CustomListField()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        # Form is valid, process the data
        return "Form submitted successfully!"
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
