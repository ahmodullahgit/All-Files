"""
i = 0
while True:
    year = int(input('Enter a year: '))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print('Great! You entered a leap year.')
        i += 1
        continue
    else:
        print("Oops! You didn\'t enter leap year.")

    ask = input('Type "Quit" to Exit or Press "Enter" to Continue: ')
    if ask.title() == "Quit":
        break
"""
mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'}
    ],
    'exchnage_rate': 103.25
}
import random
i = 0
while i < len(mobile_data.get('data')):
    mobile_list = mobile_data.get('data')
    name = mobile_list[i].get('name')
    made = mobile_list[i].get('made')
    price_usd = mobile_list[i].get('price')
    # exchange = mobile_data.get('exchnage_rate')
    price = price_usd.split()
    price.remove('USD')
    price_final = ''.join(price)
    price_bdt = round(float(price_final) * mobile_data.get('exchnage_rate'))
    for mobile in mobile_data:
        templete =[
            f'Introducing the latest featured {name} from the tech land {made}. Grab it soon only on {price_usd} which is almost equal to {price_bdt} BDT'
            f'{name} made in {made}. price is {price_usd} which is almost equal to {price_bdt} BDT'
        ]
    i = i + 1
    print(random.choice(templete))