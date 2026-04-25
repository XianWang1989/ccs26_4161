
from flask import render_template_string, request

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Handle the submitted number here
        return f'Processed amount: {form.amount.data}'

    return render_template_string('''
        <form method="post">
            {{ form.amount.label }} {{ form.amount() }}<br>
            {{ form.submit() }}
        </form>
    ''', form=form)

if __name__ == '__main__':
    app.run(debug=True)
