

def get_int(msg, default=None):
    msg = msg if default is None else msg + f" ({default})"
    while True:
        response = input(msg + ": ")
        if response == "":
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
        if response == "":
            return default
        elif len(response) <= 3:
            print("Category length must be "
                  "longer than 3 characters")
        else:
            return response

