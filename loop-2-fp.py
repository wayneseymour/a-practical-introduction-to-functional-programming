def loop_avg_height():
    people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

    height_total = 0
    height_count = 0
    for person in people:
        if 'height' in person:
            height_total += person['height']
            height_count += 1

    if height_count > 0:
        average_height = height_total / height_count

        print "    ### average_height", average_height
        # => 120


def functional_avg_height(xs):
    pass
    # transformations
    # heights = map(lambda x: x['height'], xs)
    # print "    ### heights", heights



loop_avg_height()

functional_avg_height([{'name': 'Mary', 'height': 160},
            {'name': 'Isla', 'height': 80},
            {'name': 'Sam'}])

