import random
import math
def word_selector():
    words=["apple", "banana", "chocolate", "elephant", "giraffe",
    "umbrella", "kangaroo", "ocean", "penguin", "zebra",
    "sunflower", "mountain", "whisper", "butterfly", "diamond",
    "jazz", "quasar", "velvet", "xylophone", "zephyr",
    "flamingo", "hurricane", "nectar", "paradise", "quokka",
    "tulip", "volcano", "yacht", "wombat", "zodiac",
    "crimson", "emerald", "goblin", "harmony", "ivory",
    "jasmine", "koala", "lagoon", "mango", "ninja",
    "opal", "peacock", "quill", "rainbow", "sapphire",
    "tiger", "unicorn", "violet", "wonder", "xenon",
    "yeti", "zeppelin", "albatross", "breeze", "cactus",
    "dolphin", "eclipse", "firefly", "gazelle", "honey",
    "iguana", "jungle", "knight", "leopard", "moonlight",
    "narwhal", "octopus", "panda", "quicksilver", "raccoon",
    "sunset", "tornado", "urchin", "vampire", "waffle",
    "xylophone", "yogurt", "zealot", "acoustic", "blossom",
    "carousel", "dandelion", "enchanted", "fairy", "gossamer",
    "harmonious", "infinite", "jubilant", "kaleidoscope", "luminous",
    "mystical", "nebula", "oasis", "prismatic", "quixotic",
    "radiant", "serendipity", "tranquil", "universe", "vivid",
    "whimsical", "xanadu", "yonder", "zestful"]
    return random.choice(words)
def main():
    print("Welcome to word guesser game.\n")
    word=word_selector()
    text='_ '*len(word)
    no_of_try=int(math.log(len(word),2))+2
    common_letter=''
    counter=0
    print(f"{'The length of letter is:'}{len(word)}\n{text}")
    print(f'You have {no_of_try} no of attempts.\n')
    while True:
        guess=input("Guess a word: ")
        if guess!=word:
            word1=set(word)
            word2=set(guess)
            common_letter+=str( word1 & word2)
            print("Wrong guess!!\n")
            text=''
            for i in word:
                if i in common_letter:
                    text+=i+' ' 
                else:
                    text+='_ '
            print(text,'\n')
        if guess==word:
            print("You guessed it right!!\n")
            break
        counter+=1
        if no_of_try==counter:
            print("Maximum no of tries met.")
            print("The word was:",word)
            break
    if input("Do you want to play again?(y/n): ")=="y":
        main()
    else:
        print("Thank you for playing.")
if __name__=="__main__":
    main()