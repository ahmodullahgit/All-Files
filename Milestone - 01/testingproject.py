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

# Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT
# Xiaomi Note 5 is made in China The price is 300 USD which is almost equal to 30975 BDT.

mobile_dic = mobile_data.get('data')[0]
name = mobile_dic.get('name')
made = mobile_dic.get('made')
usd_price = mobile_dic.get('price')
exchange = mobile_data.get('exchnage_rate')
price_draft = usd_price.split()
price_str = price_draft[0]
final_price = float(price_str)
bdt_price = round(final_price * exchange)

print(name,'is made in', made,'The price is', usd_price,'which is almost equal to',bdt_price,'BDT.')















# exchange_rate = mobile_data.get('exchnage_rate')
# moblist = mobile_data.get('data')
# mobile_dict = moblist[0]
# name = mobile_dict.get('name')
# made_in = mobile_dict.get('made')
# usd_price = mobile_dict.get('price')
# price2 = usd_price.split()
# price3 = price2[0]
# bdt_price = round(float(price3)*exchange_rate)
# print(name, 'is made in', made_in, 'The price is',usd_price, 'which is equal to',bdt_price,'BDT')


