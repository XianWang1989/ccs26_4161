
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, FieldList, FormField, validators

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class ItemForm(FlaskForm):
    item = StringField('Item', [validators.DataRequired()])

class MyListForm(FlaskForm):
    mylist = FieldList(FormField(ItemForm), min_entries=1)  # At least one item is required

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm()
    if form.validate_on_submit():
        # Process the valid form data
        items = [item.item.data for item in form.mylist.entries]
        return f"Received items: {items}"
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
