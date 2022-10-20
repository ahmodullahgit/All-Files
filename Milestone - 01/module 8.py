"""
my_text = 'Hello, i\'m md ahmodullah, from noyagola, chapainawabgonj'
my_word_text = my_text.split(" ")
print(my_word_text)

my_list = ' '.join(my_word_text)
print(my_list)
"""
"""
biodata = ['Hello', "i'm", 'md', 'ahmodullah', 'from', 'noyagola', 'chapainawabgonj']
for bio in biodata:
    print(bio)
"""
"""
#numbers = [10, 20, 30, 40, 50, 60, 70]
sum = 0
for number in range(10,71,10):
    sum += number
print(sum)

wp = [{"id":1,"name":"Igor","url":"","description":"","link":"https:\/\/math.berkeley.edu\/wp\/blog\/author\/admin\/","slug":"admin","avatar_urls":{"24":"https:\/\/secure.gravatar.com\/avatar\/8d7a6e0f54977dbc6b6aa9f632f20ce3?s=24&d=identicon&r=g","48":"https:\/\/secure.gravatar.com\/avatar\/8d7a6e0f54977dbc6b6aa9f632f20ce3?s=48&d=identicon&r=g","96":"https:\/\/secure.gravatar.com\/avatar\/8d7a6e0f54977dbc6b6aa9f632f20ce3?s=96&d=identicon&r=g"},"meta":[],"_links":{"self":[{"href":"https:\/\/math.berkeley.edu\/wp\/wp-json\/wp\/v2\/users\/1"}],"collection":[{"href":"https:\/\/math.berkeley.edu\/wp\/wp-json\/wp\/v2\/users"}]}}]
print(wp)
print(type(wp))
"""
print('*************************************************')
thislist = ["apple", "orange"]
thislist.append("banana")
print(thislist)
