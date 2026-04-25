
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, validators

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[validators.Optional()]), min_entries=1)

    def validate_mylist(form, field):
        if not any(value.data for value in field):
            raise validators.ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Process the form data
        items = [item.data for item in form.mylist if item.data]
        return f'Validated items: {items}'
    return render_template('your_template.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

