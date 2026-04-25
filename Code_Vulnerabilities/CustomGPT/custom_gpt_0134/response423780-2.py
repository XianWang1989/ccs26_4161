
class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)  # Requires at least one entry
    submit = SubmitField('Submit')

    def validate_mylist(form, field):
        if not field.data or all(item.data == '' for item in field):
            raise ValidationError('At least one item is required.')
