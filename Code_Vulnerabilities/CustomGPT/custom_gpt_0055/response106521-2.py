
import locale

def format_number(num):
    locale.setlocale(locale.LC_ALL, '')
    return locale.format_string('%.2f', num, grouping=True)
