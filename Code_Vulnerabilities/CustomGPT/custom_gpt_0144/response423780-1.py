from flask import Flask, request, render_template_string
from flask_wtf import FlaskForm
from wtforms import Field
from wtforms.validators import ValidationError

class MyListField(Field):
    def process_formdata(self, valuelist):
        self.data = valuelist

    def pre_validate(self, form):
        if not self.data or all(item.strip() == '' for item in self.data):
            raise ValidationError('At least one item is required.')

class MyForm(FlaskForm):
    mylist = MyListField()

# Flask app setup
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if form.validate_on_submit():
        return f'Submitted data: {form.mylist.data}'
    return render_template_string('''
        <form method="post">
            <input type="text" name="mylist" value="one">
            <input type="text" name="mylist" value="two">
            <input type="text" name="mylist" value="three">
            <input type="text" name="mylist" value="four">
            <input type="submit">
        </form>
        {% for field, errors in form.errors.items() %}
            {% for error in errors %}
                <p style="color: red;">{{ error }}</p>
            {% endfor %}
        {% endfor %}
    ''', form=form)

if __name__ == '__main__':
    app.run(debug=True)
