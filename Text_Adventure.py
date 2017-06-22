start = '''
You are playing as Shrek.  One day, Shrek wanted to
show that he wasn't just a scary ogre, and had many layers
an onion. SO, Shrek left his beloved swamp for the towering,
poison-ivy covered castle to save the enchanting princess.
'''


print(start)


print("Type 'start' to embark on your adventure to save the princess.")
user_input = input()
if user_input == "start":
    print("You enter the forest.")
    print("After walking for a while, you are feeling tired. Would you like to take a nap or continue on?")
    print("Type 'take a nap' or type 'continue on'")
    user_input = input()
    if user_input == "take a nap":
        print("You have decided to take a nap and as a result you have been captured my Lord Farquaad's knights.")
        print("Game Over.")
    elif user_input == "continue on":
        print("You have continued walking and you have reached the bridge.")
        print("Your friend the gingerbread man is being threatened by Lord Farquaad.Would you like to save him?")
        print("Type 'yes' or 'no.'")
        user_input = input()
        if user_input == "yes":
            print("You were able to save your friend, but you failed to save the Princess")
            print("Game Over.")
        elif user_input == "no":
            print("You have decided to continue across the bridge.")
            print("You have reached the outskirts of the castle, but there is a dragon guarding the castle doors.Would you like to fight or run away?")
            print("Type 'fight' or 'run away'")
            user_input = input()
            if user_input == "fight":
                print("You have defeated the dragon and saved the day by rescuing Princess Fiona.  She is falling madly in love with you and both of you have decided to get married and you lived Happily Ever After...")
            elif user_input == "run away":
                print("You couldn't escape and got burned alive by the dragon:(")
                print("Game Over.")
