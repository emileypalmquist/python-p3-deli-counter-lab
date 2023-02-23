def line(queue):
    if not queue:
        print("The line is currently empty.")
    else:
        line_readout = "The line is currently:"
        for count, person_name in enumerate(queue, start=1):
            line_readout += f" {count}. {person_name}"

        print(line_readout)


def take_a_number(queue, name):
    queue.append(name)
    position = len(queue)
    greeting = f"Welcome, {name}. You are number {position} in line."
    print(greeting)


def now_serving(queue):
    if not queue:
        print("There is nobody waiting to be served!")
    else:
        name_removed = queue.pop(0)
        print(f"Currently serving {name_removed}.")
