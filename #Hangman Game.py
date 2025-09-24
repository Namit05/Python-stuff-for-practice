#Hangman Game
import random

words = (
    "lion", "tiger", "elephant", "giraffe", "zebra", "kangaroo", "panda", "koala", "cheetah", "leopard",
    "hippopotamus", "rhinoceros", "wolf", "fox", "bear", "camel", "deer", "monkey", "gorilla", "chimpanzee",
    "dog", "cat", "rabbit", "hamster", "squirrel", "otter", "seal", "whale", "dolphin", "shark",
    "octopus", "crab", "lobster", "starfish", "penguin", "ostrich", "peacock", "sparrow", "parrot", "eagle",
    "falcon", "owl", "pigeon", "crow", "woodpecker", "rooster", "hen", "duck", "goose", "turkey",
    "buffalo", "cow", "bull", "sheep", "goat", "horse", "donkey", "mule", "yak", "reindeer",
    "bat", "snake", "crocodile", "alligator", "turtle", "tortoise", "frog", "toad", "lizard", "gecko",
    "iguana", "chameleon", "ant", "bee", "wasp", "butterfly", "moth", "dragonfly", "ladybug", "grasshopper",
    "termite", "cockroach", "spider", "scorpion", "jellyfish", "stingray", "squid", "seahorse", "clam", "snail",
    "slug", "earthworm", "hedgehog", "porcupine", "armadillo", "sloth", "anteater", "platypus", "walrus", "sealion",

    "india", "china", "japan", "russia", "brazil", "argentina", "chile", "colombia", "peru", "venezuela",
    "mexico", "canada", "usa", "france", "germany", "italy", "spain", "portugal", "greece", "turkey",
    "egypt", "southafrica", "nigeria", "kenya", "ethiopia", "uganda", "tanzania", "morocco", "algeria", "tunisia",
    "iran", "iraq", "afghanistan", "pakistan", "bangladesh", "srilanka", "nepal", "bhutan", "maldives", "thailand",
    "vietnam", "cambodia", "myanmar", "malaysia", "singapore", "indonesia", "philippines", "australia", "newzealand", "fiji",
    "saudiarabia", "qatar", "kuwait", "uae", "oman", "yemen", "israel", "palestine", "jordan", "lebanon",
    "sweden", "norway", "finland", "denmark", "iceland", "poland", "czech", "slovakia", "hungary", "austria",
    "switzerland", "belgium", "netherlands", "luxembourg", "ireland", "uk", "scotland", "wales", "england", "croatia",
    "serbia", "romania", "bulgaria", "slovenia", "latvia", "lithuania", "estonia", "georgia", "armenia", "azerbaijan",

    "burger", "pizza", "sandwich", "fries", "hotdog", "taco", "burrito", "quesadilla", "nachos", "shawarma",
    "falafel", "kebab", "sushi", "ramen", "noodles", "dumpling", "springroll", "pakora", "samosa", "kachori",
    "vada", "idli", "dosa", "uttapam", "paratha", "naan", "roti", "bhatura", "chole", "pavbhaji",
    "bhelpuri", "sevpuri", "panipuri", "kachumbari", "shawaya", "manchurian", "cutlet", "roll", "wrap", "toast",
    "momo", "pasta", "lasagna", "spaghetti", "donut", "croissant", "waffle", "pancake", "crepe", "muffin",
    "cupcake", "brownie", "cookie", "popcorn", "chips", "pretzel", "bagel", "cheeseburger", "doubleburger", "friedchicken",
    "chickenwings", "nuggets", "fishandchips", "submarine", "salad", "coleslaw", "milkshake", "smoothie", "icecream", "gelato",
    "sundae", "popsicle", "kulfi", "jalebi", "rasgulla", "gulabjamun", "laddu", "barfi", "halwa", "peda",



    "newyork", "losangeles", "chicago", "houston", "miami", "toronto", "vancouver", "montreal", "london", "paris",
    "berlin", "madrid", "barcelona", "rome", "milan", "amsterdam", "brussels", "vienna", "prague", "budapest",
    "warsaw", "moscow", "saopaulo", "riodejaneiro", "buenosaires", "capetown", "johannesburg", "cairo", "nairobi", "lagos",
    "mumbai", "delhi", "bangalore", "hyderabad", "chennai", "kolkata", "pune", "ahmedabad", "jaipur", "lucknow",
    "kanpur", "surat", "nagpur", "patna", "bhopal", "indore", "kochi", "thiruvananthapuram", "bhubaneswar", "guwahati",
    "tokyo", "osaka", "seoul", "beijing", "shanghai", "hongkong", "singapore", "bangkok", "kualalumpur", "jakarta",
    "manila", "dubai", "doha", "riyadh", "istanbul", "athens", "zurich", "stockholm", "oslo", "helsinki"
)

hangman_art={0: ("   ",
                 "   ",
                 "   "),
             1: (" o ",
                 "   ",
                 "   "),
              2: (" o ",
                  " | ",
                  "   "),
             3: (" o ",
                 "/| ",
                 "   "),
              4: (" o ",
                  "/|\\",
                  "   "),
              5: (" o ",
                  "/|\\",
                  "/  "),
             6: (" o ",
                 "/|\\",
                 "/ \\")}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))
    
def display_answer (answer):
    print(" ".join(answer))

def main():
    answer=random.choice(words)
    hint=["_"] * len(answer)
    wrong_guesses=0
    guessed_letters=set()
    is_running=True

    while is_running :
        display_man(wrong_guesses)
        display_hint(hint)
        guess=input("Enter a letter :").lower()

        if len(guess) !=1 or not guess.isalpha():
            print("Invalid input!")
            continue

        if guess in guessed_letters :
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)
    
    
        if guess in answer:
            for i in range (len(answer)):
                if answer[i]==guess :
                    hint[i]=guess

        else :
            wrong_guesses+=1

        if  "_" not in hint :
            display_man(wrong_guesses)
            display_answer(answer)
            print("You win!!!")
            is_running=False
        
        elif wrong_guesses >= len(hangman_art)-1 :  
             display_man(wrong_guesses)
             display_answer(answer)
             print("You lose!!!")
             is_running=False





if __name__=="__main__":
    main()