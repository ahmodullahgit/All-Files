# dollar rate conversion using python

def dollar_bdt(dollar, exchange):
    bdt = dollar * exchange
    return bdt
print(dollar_bdt(189, 102.25))

def phone_price(phone, exchange):
    price = phone * exchange
    return price

result1 = round(phone_price(200, 101.85))
result2 = round(phone_price(250, 101.85))
result3 = round(phone_price(300, 101.85))
result4 = round(phone_price(180, 101.85))

print('The xiomi phone price',result1)
print('The Samsung phone price',result2)
print('The Iphone 13 phone price',result3)
print('The Redmi phone price',result4)


