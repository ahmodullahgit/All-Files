"""
def greetings(name):
    print(f'Hi, {name}. What\'s up!! I can guess your wife name. Want to see it?')
    comment = input('type anything to leave or Press "Enter" if you want to see it : ')
    if comment == '':
        print(f'Got it! Your wife name is Mrs. {name}')
    elif comment == 'Kashib Khan':
        print('Oops! Sorry! There is no one who can guess Kashib Khan\'s wife name!!')

greetings('Ahmod')
"""

# Voter Check Programme
def voter_check(age):
    if age >= 18:
        print('You\'re a voter.')
    else:
        print('You\'re not eligible for voting.')

voter_check(17)
voter_check(22)
voter_check(37)
