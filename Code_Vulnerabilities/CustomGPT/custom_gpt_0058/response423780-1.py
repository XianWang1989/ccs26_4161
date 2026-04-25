
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, FieldList, FormField, ValidationError, SubmitField

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class MyListForm(FlaskForm):
    myitem = StringField('Item')

class MyForm(FlaskForm):
    mylist = FieldList(FormField(MyListForm), min_entries=1)  # at least one item
    submit = SubmitField('Submit')

    def validate_mylist(self, field):
        if not any(item.myitem.data for item in field):
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()

    if form.validate_on_submit():
        # Process the data in form.mylist
        items = [item.myitem.data for item in form.mylist]
        return f'Items Submitted: {items}'

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
