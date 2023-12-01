
from helpers.new_guess import newGuess;

def create_friends():
    per1 = newGuess('Juan',['Carito','Angel'],['2','4']);
    per2 = newGuess('Carlitos',['Juan','Carito'],['2','4']);
    per3 = newGuess('Sofia',['Soto','XD'],['2','4']);
    # newGuess('Juan',['Carito','Angel'],['2','4']);
    # newGuess('Juan',['Carito','Angel'],['2','4']);
    return [per1,per2,per3];
    
def create_friends_list(guess,friends,dishes):
    
    if len(guess) != len(friends) or len(guess) != len(dishes):
            raise ValueError("Ingrese los datos de manera adecuada, tiene que ser la misma cantidad de amigos y de platos")
    
    newGuess(guess,friends,dishes);