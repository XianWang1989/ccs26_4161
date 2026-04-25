
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()

    if form.validate_on_submit():
        # Process the input data from the form
        items = form.mylist.data
        flash(f'Success! You submitted: {items}')
        return redirect(url_for('doit'))

    return render_template('form.html', form=form)
