#not blank function


def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response !="":
            return response
        else:
            print("sorry, this can't be blank")



# Main Routine goes here
name = not_blank("what is your name?")
