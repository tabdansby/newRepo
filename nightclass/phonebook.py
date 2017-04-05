#put a name in dictionary; organize name-number pairs by last name as the key;
#once finished, paste this code into Slack for review on Monday

phonebook = {'hartsfield': {'name': 'Brian Hartsfield', 'phone': '(899)501-2317'},
            'jackson': {'name': 'Randy Jackson','phone': '(811) 587-6915'},
            'kirkpatrick': {'name': 'Michael Kirkpatrick', 'phone': '(833) 908-2556'},
            'mooney': {'name': 'Marie Mooney', 'phone': '(822) 375-8140'},
            'nye': {'name': 'Michael Nye','phone':'(822) 419-8377'},
            'renz': {'name': 'Chadwick Renz','phone': '(811) 545-4601'},
            'collins': {'name': 'Kenya Collins', 'phone': '(833) 198-7444'},
            'tindal': {'name': 'Teresa Tindal', 'phone': '(822) 106-3461'},
            'calloway': {'name': 'Cleo Calloway', 'phone': '(811) 816-2840'},
            'childers': {'name': 'Shelly Childers','phone': '(844) 958-6692'}
            }
"""to look up by phone number:
for ke, va in phonebook.items():
    for k, v in va.items():
        if q in v:
            print("name: {}".format(phonebook[ke]['name']))
            print("phone: {}".format(phonebook)[ke]['phone'])
            side note: .items breaks dictionaries into tuples
"""
while True:
    u_i = input("Do you want to find, add, or delete an entry? Or quit?: ")
    if u_i == 'find':
        p_ln = input("What's the last name?: ").lower()
        if p_ln in phonebook:
            print(p_ln, phonebook[p_ln])
        else:
            print('Not found!')
    elif u_i == 'add':
        added_last_name = input("What is the last name of the person you want to add?: ")
        added_first_name = input("What is the first name of the person you want to add?: ")
        added_phone = input("What is the phone number of the person you want to add?: ")
        new_phonebook = phonebook[added_last_name] = ('name', (added_first_name + " " + added_last_name).capitalize(), ('phone', added_phone))
        print(new_phonebook)
    elif u_i == 'delete':
        minus_name = input("What is the last name of the person you want to delete?: ").lower()
        del(phonebook[minus_name])
        print('Entry for '+ minus_name +' is now deleted.')
    else:
        print('Phonebook closed. Bye!')
        break




"""num = input('What is the number?: ')
            added_name phonebook['name':]
phonebook[newname]

elif u_i == delete:
    xxxxxx


else u_i == quit:
    print('Goodbye')
    break







def pn(dic, name):
    print(dic[name]['name'])
    print(dic[name]{'phone'})

Ask user if they want to add, delete, look up someone
edit <--advanced, if you get there

'hartsfield':(899) 501-2317: Brian Hartsfield
(811) 587-6915: Randy Jackson
(833) 908-2556: Michael Kirkpatrick
(822) 375-8140: Marie Mooney
(822) 419-8377: Michael Nye
(811) 545-4601: Chadwick Renz
(833) 198-7444: Kenya Collins
(822) 106-3461: Teresa Tindal
(811) 816-2840: Cleo Calloway
(844) 958-6692: Shelly Childers




if p_ln = number:
    find_num = input('What is the number?: ')
        find_num phonebook['phone']"""
