

def split_line_into_item_and_mark(line):
    item = ''
    mark = ''
    # Remove the two lines above and write your code to the solution
    return [item, mark]



def mark_to_bool(mark):
    # Delete the line below and and write your code to the solution
    return False



def filter_out_ticked_items(items, marks):
    # Delete the line below and and write your code to the solution
    return items



def get_list_of_items_to_get(shopping_list):
    # Delete the line below and and write your code to the solution
    return []

# BELOW THIS IS EXTENSION QUESTIONS. MAKE SURE YOU HAVE ALL TESTS PASSING FOR THE FUNCTIONS
# BEFORE THIS.
def turn_shopping_list_to_dict(items, marks):
    # Delete the line below and and write your code to the solution
    return {}


def buy_item(shopping_dict, item):
    # Delete the line below and and write your code to the solution
    return shopping_dict


def make_shopping_list_string(shopping_dict):
    # Delete the line below and and write your code to the solution
    return ''


def get_unbought_items(shopping_dict):
    # Delete the line below and and write your code to the solution
    return []


# BELOW THIS ARE ALL FUNCTIONS YOU SHOULD NOT TOUCH!!. IF YOU ARE INTERESTED
# ABOUT HOW THESE FUNCTIONS WORK, FEEL FREE TO ASK ME.

def get_shopping_list():
    shopping_list = []
    while True:
        line = input()
        if line == '':
            return '\n'.join(shopping_list)
        else:
            words = line.split(' ')
            if len(words) != 2 or words[-1] not in {'x', '/'}:
                print('This is not a valid shopping list item, please enter something else.')
                continue
            shopping_list += [line]


def split_string(s, character):
    assert len(character) == 1, \
        'you must use a single character to split a string, e.g. \'a\', not {}'.format(character)
    return s.split(character)


def shopping_list_program():
    print('Enter your shopping list below. <item-name> <tick(/) or cross(x)>')
    print('To finish, press Enter on an empty line')
    shopping_list = get_shopping_list()
    items_to_get = get_list_of_items_to_get(shopping_list)
    print('Need to get: \n{}'.format('\n'.join(items_to_get)))


def advanced_shopping_list_program():
    pass


def test(f, *input_expecteds):
    print('testing {}:'.format(f.__name__))
    for inputs, expected in input_expecteds:
        actual = f(*inputs)
        satisfied = False
        if type(expected) == list:
            satisfied = (set(expected) == set(actual)) and (len(expected) == len(actual))
        elif type(expected) == dict:
            satisfied = expected == actual
        else:
            satisfied = expected == actual

        if not satisfied:
            print(
                'ERROR: {}({}) returned {}, when it should return {}'.format(
                    f.__name__,
                    ','.join([to_arg(arg) for arg in inputs]),
                    actual,
                    expected
                )
            )
    print('DONE\n')


def to_arg(arg):
    if type(arg) == str:
        return '\'{}\''.format(arg).replace('\n', '\\n')
    else:
        return str(arg)


test(
    split_line_into_item_and_mark,
    (['oranges /'], ['oranges', '/']),
    (['apples x'], ['apples', 'x'])
)
test(
    mark_to_bool,
    (['x'], False),
    (['/'], True),
)
test(
    filter_out_ticked_items,
    ([['oranges'], ['/']], ['oranges']),
    ([['oranges', 'apples'], ['/', 'x']], ['oranges']),
    ([['a', 'b', 'c', 'd'], ['/', 'x', '/', 'x']], ['a', 'c']),
)
test(
    filter_out_ticked_items,
    ([['oranges'], ['/']], ['oranges']),
    ([['oranges', 'apples'], ['/', 'x']], ['oranges']),
    ([['a', 'b', 'c', 'd'], ['/', 'x', '/', 'x']], ['a', 'c']),
)
test(
    get_list_of_items_to_get,
    (['food x'], ['food']),
    (['food /'], []),
    (['food /\nthings x\nstuff x'], ['things', 'stuff']),
)
print('EXTENSION FUNCTIONS:')
test(
    turn_shopping_list_to_dict,
    ([['orange'], ['x']], {'orange': False}),
    ([['orange', 'apple'], ['x', '/']], {'orange': False, 'apple': True}),
)
test(
    buy_item,
    ([{'apple': False}, 'apple'], {'apple': True}),
    ([{'apple': True}, 'apple'], {'apple': True}),
    ([{'apple': True, 'pears': False}, 'pears'], {'apple': True, 'pears': True})
)
# for dict ordering non-determinism
list_dict = {'apple': False, 'pears': True}
marks = {
    True: '/',
    False: 'x'
}
expected = '\n'.join(['{} {}'.format(item, marks[v]) for item, v in list_dict.items()])
test(
    make_shopping_list_string,
    ([{'apple': False}], 'apple x'),
    ([list_dict], expected)
)
test(
    get_unbought_items,
    ([{'apple': False}], ['apple']),
    ([{'apple': False, 'pears': True}], ['apple']),
    (
        [{'pears': True, '£50-steam-voucher': False, 'apple': False,}],
        ['apple', '£50-steam-voucher'])
)
