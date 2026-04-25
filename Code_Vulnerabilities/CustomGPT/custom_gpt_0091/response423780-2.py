
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for CSRF protection

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()

    if form.validate_on_submit():
        # Process validated data
        items = form.mylist.data
        return f'Success! Items: {items}'

    return render_template('form.html', form=form)
