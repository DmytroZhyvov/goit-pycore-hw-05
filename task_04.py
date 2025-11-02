def input_error(func):
    """Error handling function"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError):
            return 'Enter the argument for the command'
        except KeyError:
            return 'Check the argument'
    return inner


@input_error
def parse_input(user_input):
    """Parse user input"""

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    """Add contact to list of contacts"""

    name, phone = args
    if name in contacts:
        return 'Contact already exists. Try again.'
    else:
        contacts[name] = phone
        return 'Contact added.'


@input_error
def change_contact(args, contacts):
    """Change contact phone number"""

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return 'Contact updated.'
    else:
        return 'Contact does not exist. Try again.'


@input_error
def show_phone(args, contacts):
    """Show contact phone number"""

    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return 'Contact does not exist. Try again.'

@input_error
def show_all(contacts):
    """Show all contacts"""

    if contacts:
        result = ", ".join([f"{name}: {phone}" for name, phone in contacts.items()])
        return result
    else:
        return "No contacts found."


def main():
    contacts = {}

    print('Welcome to the assistant bot!')

    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print('Goodbye!')
            break

        elif command == 'hello':
            print('How can I help you?')

        elif command == 'add':
            print(add_contact(args, contacts))

        elif command == 'change':
            print(change_contact(args, contacts))

        elif command == 'phone':
            print(show_phone(args, contacts))

        elif command == 'all':
            print(show_all(contacts))

        else:
            print('Invalid command! Try again.')


if __name__ == "__main__":
    main()
