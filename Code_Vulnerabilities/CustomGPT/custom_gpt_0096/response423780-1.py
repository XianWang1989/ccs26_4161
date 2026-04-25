
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, validators

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', [validators.InputRequired()]))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()

    if request.method == 'POST' and form.validate_on_submit():
        # Process your valid form data
        items = form.mylist.data
        return f'Validated items: {items}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
