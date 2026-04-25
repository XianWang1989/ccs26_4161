
from flask import Flask, render_template, redirect, url_for, flash
from forms import MyListForm

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm()
    if form.validate_on_submit():
        # Process the validated data
        flash('Form submitted successfully!')
        return redirect(url_for('doit'))
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
