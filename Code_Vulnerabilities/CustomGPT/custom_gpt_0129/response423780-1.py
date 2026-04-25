
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, FieldList, SubmitField
from wtforms.validators import DataRequired, length

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    mylist = FieldList(
        StringField('Item', validators=[DataRequired()]), min_entries=1, max_entries=10
    )
    submit = SubmitField('Submit')

@app.route('/myform', methods=['GET', 'POST'])
def my_form():
    form = MyForm()

    if form.validate_on_submit():
        # Process the validated data
        items = form.mylist.data
        if len(items) < 1:
            flash('You must provide at least one item.')
            return redirect(url_for('my_form'))
        else:
            # Do something with the valid items
            # e.g., save to database or process further
            flash('Form submitted successfully!')
            return redirect(url_for('my_form'))

    return render_template('myform.html', form=form)

@app.route('/doit', methods=['POST'])
def doit():
    # This route can handle form submissions
    return redirect(url_for('my_form'))

if __name__ == '__main__':
    app.run(debug=True)
