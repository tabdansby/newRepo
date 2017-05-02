
1. Use python _list comprehensions_ to complete your solutions.

The following test data is provided:

```
>>> names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

>>> people = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]
```

- `names` is a list of strings.
- `people` is a list of tuples.


Write the following functions:

1. `long names` - Return a list of names that are least `n` chars in length.
2. `starts_with` - Return a list of names that start with `'S'`.
3. `last_names` - Return a list of only last names from the list of tuples.
4. `smoosh` - collapse the list of tuples `people` into a flat list of strings

names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

people = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]

1.
long_enough = [n for n in names if len(n) == 7 or len(n) > 7]
print(long_enough)


2.
starts_with = [l for l in names if l[0] == "S"]
print(starts_with)

3.
last_names = [p[1] for p in people]
print(last_names)

4.

for i in people:
    smoosh = [r for i in people for r in i]
    print(smoosh)
