from client import commands


class Menu:
    def __init__(self):
        self.commands = {
            "/show_cats": commands.display_categories,
            "/show_books": commands.display_books,
            "/q": commands.quit,
        }
        self.template = "\nShow all categories: {0}\n" \
                        "Show books from category" \
                        "Quit: {1}\n"

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

