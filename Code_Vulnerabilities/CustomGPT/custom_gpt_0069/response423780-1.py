
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]), min_entries=1)

    def validate_mylist(form, field):
        if not field.data or len(field.data) == 0:
            raise ValidationError('You must provide at least one item.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm(request.form)
    if request.method == 'POST' and form.validate():
        # Process the validated data
        items = form.mylist.data
        return f'Validated items: {items}'
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
