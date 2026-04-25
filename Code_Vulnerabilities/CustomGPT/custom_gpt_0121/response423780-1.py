
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

class MyForm(FlaskForm):
    mylist = FieldList(StringField("Item", validators=[DataRequired()]), min_entries=1)
    submit = SubmitField("Submit")

    def validate_mylist(form, field):
        if not any(field.data):
            raise ValidationError("At least one item must be entered.")

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if form.validate_on_submit():
        # Process the valid data
        items = form.mylist.data
        return f"Received: {items}"
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
