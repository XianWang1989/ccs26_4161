
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if form.validate_on_submit():
        # Process valid data
        items = [item.data for item in form.mylist]
        return f'Success! Items: {items}'
    return render_template('form_template.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
