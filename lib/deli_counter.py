def line(katz_deli):
    if len(katz_deli) > 0:
        message = "The line is currently:"

        for index, name in enumerate(katz_deli):
            message += f" {index + 1}. {name}"

        print(message)
    else:
        print("The line is currently empty.")


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    line_length = len(katz_deli)
    print(f"Welcome, {name}. You are number {line_length} in line.")


def now_serving(katz_deli):
    if len(katz_deli) > 0:
        print(f"Currently serving {katz_deli[0]}.")
        del katz_deli[0]
    else:
        print("There is nobody waiting to be served!")
