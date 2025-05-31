stack = []

while True:
    cmd = input(">> ").strip().upper()

    if cmd.startswith("PUSH "):
        value = cmd.split(" ", 1)[1]
        stack.append(value)
    elif cmd == "POP":
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is empty.")
    elif cmd == "PRINT":
        print("Stack:", stack)
    elif cmd == "EXIT":
        break
    else:
        print("Unknown command.")
