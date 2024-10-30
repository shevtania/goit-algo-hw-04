contacts = {}

def greeting():
    return 'How can I help you?'

def add_contact(*args):
    if len(args) < 2:
        return 'Not enough arguments'
    else:
        name, phone = args
    if name in contacts.keys():
        return 'This person already in contacts. Choose command "change"'
    else:
        contacts[name] = phone
    return "Contact added."

def change_contact(*args):
    if len(args) < 2:
        return 'Not enough arguments'
    name, phone = args
    if name not in contacts.keys():
        return "This person isn't  in your contacts. Choose command 'add'"
    else:
        contacts[name] = phone
    return f'Contact  {name} changed'

def show_phone(name):
    if name not in contacts:
        return f'Person {name} is absent in your contacts. '
    else:
        return f'Name: {name}, phone: {contacts[name]}'     

def show_all():
    if not contacts:
        return 'Your contacts is empty.'
    else:
        
        return '\n'.join([f'Name: {k}, phone {contacts[k]}' for k in contacts.keys()])
    
COMMAND_HANDLER = {
                   'hello': greeting,
                   'add': add_contact,
                   'change': change_contact,
                   'phone': show_phone,
                   'all': show_all
                   }
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in COMMAND_HANDLER:
            result = COMMAND_HANDLER.get(command)(*args)
            print(result)
        
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


