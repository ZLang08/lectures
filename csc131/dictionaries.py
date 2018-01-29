import string


def get_personal_data() -> dict:
    """
    :return: Returns a dictionary of personal information.
    """
    personal_data = {'name': 'Zach', 'role': 'student'}
    return personal_data


def main() -> int:
    default_dict = dict()
    print(default_dict)
    initialized_dict = dict([('name', 'Zach'), ('a_role', 'prankster')])
    print(initialized_dict)
    simple_init_dict = dict(name='Zach', a_role='student')
    print(simple_init_dict)
    simple_init_dict['a_role'] = 'prankster'
    print(simple_init_dict)
    my_comprehension = {x: x**2 for x in range(5)}
    print(my_comprehension)

    s = "a little lamb, it's fleece".translate({ord(i): None for i in string.punctuation})
    print(s)

    return 0


if __name__ == '__main__':
    main()
