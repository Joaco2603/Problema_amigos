from model.guess import Guess;
from model.friends import Frieds;

def newGuess(guess,list_friends,dishes):
    friends = Frieds(list_friends,dishes)
    guess_information = Guess(guess,friends);
    print(guess_information.name);
    print(guess_information.friends.name);
    print(guess_information.friends.dishes);