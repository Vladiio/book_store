from client.commands import commander


class Menu:
    def __init__(self):
        self.changes = False
        self.commands = {
            "lsc": commander.display_category_list,
            "lsb": commander.display_book_list,
            "gc": commander.display_category,
            "gb": commander.display_book,
            "ac": commander.add_category,
            "ab": commander.add_book,
            "q": commander.quit,
        }
        self.template = "\n\tShow categories: {:<10}" \
                        "\n\tShow books:      {:<10}" \
                        "\n\tGet category:    {:<10}" \
                        "\n\tGet book:        {:<10}" \
                        "\n\tAdd new cat:     {:<10}" \
                        "\n\tAdd new book:    {:<10}" \
                        "\n\tQuit:            {:<10}\n"

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

