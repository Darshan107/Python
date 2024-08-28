# there are different ways of formatting strings: 

def string_formatting():
    greet_old = 'Hello %s' # the place holder allows the string to be like a template
    output = greet_old % 'Darshan'
    print(f'For old formatting,\n{output = }') # old way of formatting, deprecated

    greet_positional = 'Hello {}'
    output = greet_positional.format('Darshan')
    print(f'\nFor positional formatting,\n{output = }')
    greet_positional2 = 'Hello {} {}'
    output = greet_positional2.format('Darshan', 'Timilsina')
    print(f'For positional formatting,\n{output = }')

    greet_positional_index = 'Hello {0}! Your full is {0} {1} right?'
    output = greet_positional_index.format('Darshan', 'Timilsina')
    print(f'\nFor positional index formatting,\n{output = }')
    output = greet_positional_index.format('Sheela', 'Timilsina')
    print(f'For positional index formatting diffent values,\n{output = }')

    greet_keyword = 'Hello {fname}! Your full is {fname} {lname} right?'
    greet_keyword.format(fname='Darshan', lname = 'Timilsina')
    print(f'\nFor keyword formatting,\n{output = }')
    print('================================================\n')

string_formatting()


# format method is widely used for string formatting where {} is used as placeholder and can contain index or variables.

def fstring_formatting():
    fname = 'Darshan'
    lname = 'Timilsina'
    print(f'Hello, {fname}. Your full name is {fname} {lname} right? ')

fstring_formatting()