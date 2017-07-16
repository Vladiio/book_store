from client import commands


class Menu:
    def __init__(self):
        self.changes = False
        self.commands = {
            "/show_cats": commands.display_categories,
            "/show_books": commands.display_books,
            "/add_book": commands.add_book,
            "/q": commands.quit,
        }
        self.template = "\n\tShow categories: {0:<10}" \
                        "\n\tShow books:      {1:<10}" \
                        "\n\tAdd new book:    {2:<10}" \
                        "\n\tQuit:            {3:<10}\n"

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
                action(self)

