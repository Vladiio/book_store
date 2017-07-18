from client.commands import commander


class Menu:
    def __init__(self):
        self.changes = False
        self.commands = {
            "lsc": commander.display_category_list,
            "lsb": commander.display_book_list,
            "gb": commander.display_book,
            "ac": commander.add_category,
            "ab": commander.add_book,
            "q": commander.quit,
        }
        self.template = "\n\tShow categories: {0:<10}" \
                        "\n\tShow books:      {1:<10}" \
                        "\n\tGet book:        {2:<10}" \
                        "\n\tAdd new cat:     {3:<10}" \
                        "\n\tAdd new book:    {4:<10}" \
                        "\n\tQuit:            {5:<10}\n"

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

