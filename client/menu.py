from client import commands


class Menu:
    def __init__(self):
        self.commands = {
            "/show_cats": commands.display_categories,
            "/show_books": commands.display_books,
            "/q": commands.quit,
        }
        self.template = "\n\tShow categories: {0:<10}" \
                        "\n\tShow books:      {1:<10}" \
                        "\n\tQuit:            {2:<10}\n"

    def run(self):
        while True:
            args = self.commands.keys()
            print(self.template.format(*args))
            response = input("Your choice: ")
            try:
                action = self.commands[response]
            except KeyError:
                print(f"{response} is invalid command")
            else:
                action()

