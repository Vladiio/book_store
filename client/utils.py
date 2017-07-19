

def get_book_info():
    title = get_string("Title")
    author = get_string("Author")
    price = get_int("Price")
    category_id = get_int("Category id")
    return dict(category_id=category_id,
                title=title, author=author,
                price=price) 


def get_int(msg, default=None):
    msg = msg if default is None else msg + f" ({default})"
    while True:
        response = input(msg + ": ")
        if response == "" and default is not None:
            return default
        try:
            number = int(response)
        except ValueError:
            print("Only numbers allowed")
        else:
            return number


def get_string(msg, default=None):
    msg = msg if default is None else msg + f" ({default})"
    while True:
        response = input(msg + ": ")
        if response == "" and default is not None:
            return default
        elif len(response) <= 3:
            print("Length must be "
                  "longer than 3 characters")
        else:
            return response.lower()

