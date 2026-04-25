
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.secret_key = 'secret'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(self, field):
        if not field.data or all(item.strip() == '' for item in field.data):
            raise ValidationError('At least one item is required.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        # Process the valid data
        items = form.mylist.data
        return redirect(url_for('success', items=items))
    return render_template('index.html', form=form)

@app.route('/success')
def success():
    items = request.args.getlist('items')
    return f'Success! Items: {", ".join(items)}'

if __name__ == '__main__':
    app.run(debug=True)
