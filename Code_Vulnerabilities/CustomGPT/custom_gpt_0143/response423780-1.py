
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, validators

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secret key for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', [validators.Optional()]), min_entries=1)

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        # Process the valid form data
        items = form.mylist.data
        flash(f'You submitted: {items}')
        return redirect(url_for('form'))
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
