
from flask_babel import format_decimal

@app.route('/result', methods=['POST'])
def result():
    amount = request.form.get('amount')
    formatted_amount = format_decimal(amount, locale=get_locale())
    return f'Formatted Amount: {formatted_amount}'
