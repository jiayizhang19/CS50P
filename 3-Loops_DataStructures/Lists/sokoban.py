"""
.pop() will remove the last item within the list and return that value.
.clear() will clear all the items within the list.
"""

def main():
    history = []
    while True:
        action = input("Action: ")
        if action == "Undo":
            undone = history.pop()
            print(f"Undone: {undone}")
        elif action == "Restart":
            history.clear()
        else:
            history.append(action)
        print(history)


main()