
from flask import Flask, render_template, redirect, url_for, flash
from forms import MyForm  # Assume your form class is in forms.py

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()

    if form.validate_on_submit():
        # Process the valid data
        items = form.mylist.data
        # Do something with items...
        flash('Form submitted successfully!')
        return redirect(url_for('doit'))

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
