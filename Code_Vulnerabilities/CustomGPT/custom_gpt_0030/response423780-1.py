
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]))

    def validate_mylist(self, field):
        if not field.data or all(field_item.data.strip() == '' for field_item in field):
            raise ValidationError('You must enter at least one item.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm(request.form)
    if request.method == 'POST' and form.validate():
        items = form.mylist.data
        # Process the items as needed
        flash('Items submitted successfully!', 'success')
        return redirect(url_for('doit'))
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
