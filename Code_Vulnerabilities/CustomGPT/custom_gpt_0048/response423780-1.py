
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]), min_entries=1)

    def validate_mylist(self, field):
        if not field.data or all(item.strip() == '' for item in field.data):
            raise ValidationError('At least one item is required.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm(request.form)
    if request.method == 'POST' and form.validate():
        # Process the valid data
        return 'Form successfully submitted with: ' + ', '.join(form.mylist.data)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
