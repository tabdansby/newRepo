"""start with a docstring"""

def nice_number():
    """Docstring goes here."""
    phone_number = input('what is your phone number?')
    print(phone_number)

    if len(phone_number) == 10:
        print('longer than ten...')

first_three = phone_number[0:3]

middle_three = phone_number[3:6]

last_four = phone_number [7:10]

formatted = first_three '-' middle_three '-' last_four

formatted = '{}-{}-{}'.format(first_three, middle_three, last_four)

nice_number()
