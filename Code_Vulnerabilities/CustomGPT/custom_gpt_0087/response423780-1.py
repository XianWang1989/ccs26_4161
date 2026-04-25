
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, validators, SubmitField

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', [validators.Optional()]))
    submit = SubmitField('Submit')

    def validate_mylist(self, field):
        if not any(field.data):
            raise validators.ValidationError('At least one item is required.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm(request.form)
    if request.method == 'POST' and form.validate():
        # Process the data
        items = form.mylist.data
        return f'Valid items: {items}'

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
