
def postback(i, user, tval):
    """functie ce posteaza raspunsul bazei de date;stringul din mesaj tb sa fie mai mic de 140 de caractere"""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    return result.get(i, lambda: None)()  # Default to a no-op if i is not found

# Example usage:
response = postback(1, 'user123', 'some_value')
