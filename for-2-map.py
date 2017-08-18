
def unfunc ():
    names = ['Mary', 'Isla', 'Sam']

    for i in range(len(names)):
        names[i] = hash(names[i])

    print names

def func ():
    print map(lambda x: hash(x), ['Mary', 'Isla', 'Sam'])

unfunc()
func()
