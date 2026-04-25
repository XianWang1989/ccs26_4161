
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError

app = Flask(__name__)
app.secret_key = 'secret'  # Replace with your secret key

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(self, field):
        if not field.data or all(item == '' for item in field.data):
            raise ValidationError('You must provide at least one item.')

@app.route('/form', methods=['GET', 'POST'])
def form_view():
    form = MyForm()

    if form.validate_on_submit():
        # Handle the data
        items = form.mylist.data
        return f'Items received: {items}'

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
