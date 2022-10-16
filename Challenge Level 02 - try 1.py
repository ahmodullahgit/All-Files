name = input('Enter your name: ')
salary = int(input('Enter your salary: '))
year_of_experience = int(input('Enter your year of service: '))
gender = input('Enter male/female: ')

if gender == "male":
    pronoun = 'His'
elif gender == 'female':
    pronoun = 'Her'

if year_of_experience > 5:
    print(pronoun,'net bonus is', salary * 0.05)
else:
    print(pronoun, 'not eligible for bonus.')
