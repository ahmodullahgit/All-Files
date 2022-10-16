







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

