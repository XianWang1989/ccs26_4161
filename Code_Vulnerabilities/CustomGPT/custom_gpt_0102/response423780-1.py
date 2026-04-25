
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired, length

app = Flask(__name__)
app.secret_key = 'supersecretkey'

class MyForm(FlaskForm):
    mylist = FieldList(
        StringField('Item', validators=[DataRequired(), length(min=1)]),
        min_entries=1  # Ensure at least one input is required
    )

    def validate_mylist(self, field):
        if not field.data or len(field.data) == 0:
            raise ValidationError("At least one item must be entered.")

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if form.validate_on_submit():
        # Process the valid data here
        items = form.mylist.data
        flash(f"Items submitted: {items}")
        return redirect('/')

    return render_template('form.html', form=form)

@app.route('/')
def index():
    form = MyForm()
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
