favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll_invites = {
    'bob', 'lucy', 'edward', 'phil', 'vicky',
}

for name in poll_invites:
    if name in favorite_languages:
        print(f'Hi {name.title()}, thank you for responding to the poll.')
    else:
        print(f'Hi {name.title()}, would you like to take part in the poll?')

