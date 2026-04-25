
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField
from wtforms.validators import DataRequired, Optional

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[Optional()]), min_entries=1)
    submit = SubmitField('Submit')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if request.method == 'POST':
        form.process(request.form)
        # Check if at least one item is filled
        if any(form.mylist.data):
            # Process the data if validation passes
            return redirect(url_for('success'))
    return render_template('form.html', form=form)

@app.route('/success')
def success():
    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
