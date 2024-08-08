def send_messages(messages, sent_messages):
    """Send each message and display them.
    Move each message to sent_messages."""
    while messages:
        message = messages.pop()
        print(f'{message}')
        sent_messages.append(message)



messages = ['Hi, how are you?', "I'm learning Python", 'Can you play the piano?',]
sent_messages = []

send_messages(messages, sent_messages)
print(sent_messages)
print(messages)
