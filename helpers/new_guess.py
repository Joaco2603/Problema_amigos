from model.guess import Guess;
from model.friends import Frieds;

def newGuess(guess,list_friends,dishes):
    friends = Frieds(list_friends,dishes);
    guess_information = Guess(guess,friends);
    return guess_information;