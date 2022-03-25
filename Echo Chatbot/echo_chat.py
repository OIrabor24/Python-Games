print("Lets talk! enter 'quit' to end the chat!")

while True:
    user = input("You: ")

    print(f"EchoBot: {user}")

    if user == 'quit':
        break 