def add(a, b):
    return a + b

print reduce(add, [0, 1, 2, 3, 4])

sentences = ['Mary read a story to Sam and Isla.',
             'Isla cuddled Sam.',
             'Sam chortled.']

def unfunc(xs):
    sam_count = 0
    for sentence in xs:
        sam_count += sentence.count('Sam')

    print sam_count


def func(xs):
    return reduce(lambda a, b: a + b.count('Sam'), xs, 0)

unfunc(sentences)
print func(sentences)
