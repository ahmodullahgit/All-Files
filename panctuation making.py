'''
small_case = "My name is Alvi. I live in Dhaka, but my family is from Chilmari in Kurigram. When my sister and I visited Chilmari in June, we had so much fun! My uncle caught a lot of fish. My favourite fish is “Chapila”. It’s a thin , white fish. It’s delicious! We helped our grandmother make the fish every night. We also made rice and vegetables."

panct = small_case.lower()
print(panct)
'''
'''
import string

panct_free = 'my name is alvi. i live in dhaka, but my family is from chilmari in kurigram. when my sister and i visited chilmari in june, we had so much fun! my uncle caught a lot of fish. my favourite fish is “chapila”. it’s a thin , white fish. it’s delicious! we helped our grandmother make the fish every night. we also made rice and vegetables.'

panct_free.translate(str.maketrans('','', string.panctuation))
print(panct_free)

'''
# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "my name is alvi. i live in dhaka, but my family is from chilmari in kurigram. when my sister and i visited chilmari in june, we had so much fun! my uncle caught a lot of fish. my favourite fish is “chapila”. it’s a thin , white fish. it’s delicious! we helped our grandmother make the fish every night. we also made rice and vegetables."
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char

print(no_punct)
