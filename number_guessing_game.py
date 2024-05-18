import random
def selected_number(lower,higher):
    return random.randint(lower,higher)
def guess_function(number,guess):
    if guess>number:
        print("Too high")
    elif guess<number:
        print("Too low")
def main():
    lower=input("Enter the lower number of range.\n")
    higher=input("Enter the higher number of range.\n")
    number=selected_number(int(lower),int(higher))
    no_of_guess=0
    while True:
        guess=input("Enter your guess.\n")
        guess_function(number,int(guess))
        no_of_guess+=1
        if no_of_guess==7:
            print("You have exhausted all your guesses.")
            print("The number is",number)
            break
        if int(guess)==int(number):
            print("You guessed it right")
            break
    choice=input("Do you want to continue(y/n):")
    if choice=='y':
        main()
    else:
        print("Thank you for playing.")
if __name__ == '__main__':
    main() 