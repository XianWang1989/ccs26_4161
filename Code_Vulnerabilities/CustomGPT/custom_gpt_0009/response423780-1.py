
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, validators

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', [validators.Length(min=1)]), min_entries=1)

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()

    if form.validate_on_submit():
        # Process the validated list
        items = form.mylist.data
        return f"Received items: {', '.join(items)}"

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
