
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for CSRF protection


class MyListForm(FlaskForm):
    # FieldList to hold multiple StringFields
    mylist = FieldList(StringField('Item', validators=[InputRequired()]))

    def validate_mylist(form, field):
        if not any(field.data):  # Check if at least one input is filled
            raise ValidationError('At least one item is required.')


@app.route("/", methods=["GET", "POST"])
def index():
    form = MyListForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # Process valid data here
            items = form.mylist.data
            return redirect(url_for("success"))
    return render_template("index.html", form=form)


@app.route("/success")
def success():
    return "Form submitted successfully!"


if __name__ == "__main__":
    app.run(debug=True)
