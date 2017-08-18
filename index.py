name_lengths = map(len, ["Mary", "Isla", "Sam"])

# print name_lengths

squares = map(lambda x: x * x, [0, 1, 2, 3, 4])

# print squares


import random

def unfunc_random ():
    names = ['Mary', 'Isla', 'Sam']
    code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

    for i in range(len(names)):
        names[i] = random.choice(code_names)

    print names

def f_random ():
    import random

    # names = ['Mary', 'Isla', 'Sam']
    names = ['name A', 'name B', 'Name C']

    # secret_names = map(lambda x: random.choice(['Mr. Pink',
    secret_names = map(lambda x: random.choice(['Mr. 1',
                                                'Mr. 2',
                                                'Mr. 3']),
                       names)
    print "secret names: ", secret_names

# unfunc_random()
f_random()
