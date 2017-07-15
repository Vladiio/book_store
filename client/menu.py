from client import commands


class Menu:
    def __init__(self):
        self.commands = {
            "/show": commands.display_books,
            "/q": commands.quit,
        }

    def run(self):
        while True:
            print("""
\tShow books:\t /show
\tQuit\t\t /q
                  """
                  )
            response = input("Your choice: ")
            try:
                action = self.commands[response]
            except KeyError:
                print(f"{response} is invalid command")
            else:
                action()

