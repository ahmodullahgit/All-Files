quotes = [
{
"anime": "Ouran High School Host Club",
"character": "Mitsukuni Haninozuka",
"quote": "I'm sorry! I'm sorry, Takashi! I won't forget to brush my teeth again! I won't forget!..."
},
{
"anime": "My Neighbors the Yamadas",
"character": "Noboru Yamada",
"quote": "The reason the Yamadas get along fine is because all three adults are nuts. If one of you were normal it would unbalance the rest."
},
{
"anime": "Fullmetal Alchemist",
"character": "Trisha Elric",
"quote": "You see, I'm sure we can change, because we're weak. And because we die. We have to fight in order to live, and that is what will make us strong."
},
{
"anime": "Bleach",
"character": "Don Kanonji",
"quote": "Run? Is that how you speak to a hero? How little you understand. Allow me to educate you. If a hero were to run from battle... the children could no longer call him a hero."
},
{
"anime": "Ghost Hunt",
"character": "Mai Taniyama",
"quote": "I'm tired if trying, sick of crying, I know I've been smiling, but inside I'm dying."
},
{
"anime": "Avatar: The Last Airbender",
"character": "Sokka",
"quote": "I'm going to spend my vacation AT THE LIBRARY!"
},
{
"anime": "Super Dangan Ronpa 2",
"character": "Chiaki Nanami",
"quote": "Believe in yourself... If you don’t have that... it doesn’t matter how many talents you have, you still won’t be able to hold your head up high..."
},
{
"anime": "Denpa Kyoushi",
"character": "Kagami Junichirou",
"quote": "The school takes no responsibility of your future! You are fully responsible for your own future! That is why you have to find what you want to do! You are all free!"
},
{
"anime": "Bleach",
"character": "Soi Fon",
"quote": "Showing your back in a battle? You've become a fool Yoruichi!"
},
{
"anime": "Fruits Basket",
"character": "Arisa Uotani",
"quote": "Is that the kinda attitude you show to someone concerned about you?! What's gonna happen to the person who wants to see ya, huh?!?! Its obvious... Its obvious you wish to see each other... SO COME AND FREAKIN' SEE ME ALREADY!!"
}
]
for quote in quotes:
    character = quote.get('character')
    latest_quote = quote.get('quote')
    template = f'{character} says, "{latest_quote}".'
    print(template)
    print('*\n*')