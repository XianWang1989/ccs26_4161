
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField
from wtforms.validators import InputRequired, ValidationError

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[InputRequired()]), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(form, field):
        if not any(bool(item.data) for item in field):
            raise ValidationError('At least one item is required.')

# In your route handling
@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if form.validate_on_submit():
        # Process the validated data
        pass
    return render_template('your_template.html', form=form)
