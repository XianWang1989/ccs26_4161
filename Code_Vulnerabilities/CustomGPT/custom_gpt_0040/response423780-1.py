
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item',validators=[DataRequired()]))

    def validate_mylist(form, field):
        if len(field.data) < 1:
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Process the validated data
        return "Form submitted successfully!"

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
