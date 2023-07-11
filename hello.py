# pylint: disable=missing-docstring

import sys

def full_name(first_name, last_name):
    """returns the full name"""
    if len(first_name) <= 1:
        return f"{last_name.capitalize()}"
    elif len(last_name) <= 1:
        return f"{first_name.capitalize()}"
    else:
        return f"{first_name.capitalize()} {last_name.capitalize()}"




if __name__ == "__main__":
    if len(sys.argv) == 1:
        # => ['hello.py']
        print(f'Hello{full_name("", "")}!')
    elif len(sys.argv) == 2:
        # => ['hello.py', 'John' ]
        print(f'Hello {full_name(sys.argv[1], "")}!')
    else:
        # => ['hello.py', 'John', 'Lennon']
        print(f"Hello {full_name(sys.argv[1], sys.argv[2])}!")
