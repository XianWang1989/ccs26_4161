
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]))

    def validate_mylist(form, field):
        if not field.data or all(item.strip() == '' for item in field.data):
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if form.validate_on_submit():
        # Process the input data
        items = form.mylist.data
        return f'Validated items: {items}'
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
