"""start with a docstring"""

def nice_number(phone_number):
    """Docstring goes here."""
    phone_number = input('what is your phone number?')
    print(phone_number)

    if len(phone_number) == 10:
        print('longer than ten...')

nice_number()
