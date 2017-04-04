tree_names = {'Maple': 'Acer','Cedar': 'Caedrus','Cypress':'Cupressaceae','Pine':'Pinaceae','Elm':'Ulmaceae'}

name = input('What tree? >>')

if name in tree_names:
    print('Yes')
else:
    print('No')
if name in tree_names.values():
    print('This is the Latin label')
else:
    print('No')
