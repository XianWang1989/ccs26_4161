
from flask_babel import format_number, parse_number

# In your index route
if request.method == 'POST':
    number = request.form.get('number')
    try:
        # Parse the number according to the current locale
        parsed_number = parse_number(number)
        formatted_number = format_number(parsed_number)
    except Exception as e:
        formatted_number = _("Invalid number format")

    return render_template('index.html', number=formatted_number)
