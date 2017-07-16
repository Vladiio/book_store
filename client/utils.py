

def get_int(msg):
    while True:
        response = input(msg)
        try:
            number = int(response)
        except ValueError:
            print("Only numbers allowed")
        else:
            return number
