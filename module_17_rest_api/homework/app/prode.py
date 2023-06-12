DATA = [
    {'id': 0, 'title': 'A Byte of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 3, 'title': 'War and Peace', 'author': 'Leo Tolstoy'},
]
values_column = tuple(DATA)


x=(12, 7, 8)
y = ('t','y','u')
qry = str()
for key, obj_class in zip(x, y):
    qry += f"{key} = '{obj_class}',"
s = f"{x} = '{y}',"
print(s)
# y=f"{'?,' * len(tuple(x))}"[:-1]
# qry = f"{x} VALUES ({'?, ' * len(tuple(x))})"
# print(y.split(','
# print(y)
