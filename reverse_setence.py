def reverse_setence(setence):
    stack = []
    reversed_setence = ""

    for word in setence.split():
        stack.append(word)

    while len(stack)> 0:
        reversed_setence += stack.pop() +""

    return reversed_setence.strip()

setence = "selamat pagi, bagaimana hari-hari anda?"
print(reverse_setence(setence))
