def add(datatype, *args):
    if datatype == 'int':
        res = 0
    elif datatype == 'str':
        res = ''

    for item in args:
        res += item

    print(res)


add('int', 5, 6)
add('str', 'Hi ', 'Geeks')