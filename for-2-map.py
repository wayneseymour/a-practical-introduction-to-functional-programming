
def unfunc():
    names = ['Mary', 'Isla', 'Sam']

    for i in range(len(names)):
        names[i] = hash(names[i])

    print names


def func():
    print map(lambda x: hash(x), ['Mary', 'Isla', 'Sam'])


def hash_all(xs):
    return map(hash, xs)


unfunc()
func()

print hash_all(['Mary', 'Isla', 'Sam'])
