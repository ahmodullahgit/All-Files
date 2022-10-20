







# i = 0
# while i < len(mobile_data.get('data')):
#     mobile_list = mobile_data.get('data')
#     name = mobile_list[i].get('name')
#     made = mobile_list[i].get('made')
#     price_usd = mobile_list[i].get('price')
#     # exchange = mobile_data.get('exchnage_rate')
#     price = price_usd.split()
#     price.remove('USD')
#     price_final = ''.join(price)
#     price_bdt = round(float(price_final) * mobile_data.get('exchnage_rate'))
#
#     sen_one = [f'Introducing the latest featured {name} from the tech land {made}.',
#                f'the latest featured intrued by us {name} from the tech land {made}.',
#                f'we are coming with some latest model  {name} from the tech land {made}.']
#     sen_two = [f'Grab it soon only on {price_usd} which is almost equal to {price_bdt} BDT',
#                f'Take it as soon as possible {price_usd} which is almost equal to {price_bdt} BDT',
#                f'dont hurry e+we hav eenogh  {price_usd} which is almost equal to {price_bdt} BDT',]
#     # templete_list = [f'Introducing the latest featured {name} from the tech land {made}. Grab it soon only on {price_usd} which is almost equal to {price_bdt} BDT',
#     #             f'kivju ljon jsdf {name} from the tech land {made}. Grab it soon only on {price_usd} which is almost equal to {price_bdt} BDT',
#     #             f'wecome to nothong {name} from the tech land {made}. Grab it soon only on {price_usd} which is almost equal to {price_bdt} BDT' ]
#     templete_list = random.choice(sen_one) + random.choice(sen_two)
#     i = i + 1
#     print(templete_list)
'''
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

mobile_dict = mobile_data.get('data')[2]
name = mobile_dict.get('name')
made_in = mobile_dict.get('made')
usd_price = mobile_dict.get('price')
exchange_rate = mobile_data.get('exchnage_rate')
exchange = mobile_data.get('exchnage_rate')
print(name, made_in, usd_price, exchange_rate,exchange)


def greeting(name, name2):
    g1 = f'hello, {name}'
    g2 = f'hello, {name2}'
    g3 = f'hello, {name}'
    return g1, g2, g3

print(greeting('kalu', 'falu'))
'''
"""
post_data = [
    {
        "userId":  "Alex Gates",
        "id": 1,
        "title": "sunt aut facere repellat provident",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    },
    {
        "userId":  "Alex Gates",
        "id": 2,
        "title": "qui est esse ",
        "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
    },
    {
        "userId":  "Alex Gates",
        "id": 3,
        "title": "ea molestias quasi exercitationem ",
        "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
    },
    {
        "userId":  "Alex Gates",
        "id": 4,
        "title": "eum et est occaecati ",
        "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
    },
    {
        "userId":  "Alex Gates",
        "id": 5,
        "title": " nesciunt quas odio",
        "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
    },
    {
        "userId":  "Alex Gates",
        "id": 6,
        "title": "dolorem eum magni eos aperiam quia ",
        "body": "ut aspernatur corporis harum nihil quis provident sequi\nmollitia nobis aliquid molestiae\nperspiciatis et ea nemo ab reprehenderit accusantium quas\nvoluptate dolores velit et doloremque molestiae"
    }, ]
for data in post_data:
    url = data.get('title')
    new_url = url.replace(" ", "-").strip("-")
    data.update({'slug': new_url})
print(post_data[3])
"""

numbers = [2, 6, 9, 8, 8, 15, 1, 5, 88]


def multiply_list(list):
    result = 1
    for number in list:
        result *= number
    return result

result = multiply_list(numbers)
# print(result)

def check_prime(number):
    if (number == 1):
        return False
    elif(number == 2):
        return True
    else:
        for x in range(2,number):
            if (number % x) == 0:
                return False
            else:
                return True

print(check_prime(75))



