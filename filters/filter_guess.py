
from patterns.Singleton import singleton_resultado; 


friends_cache = [];
friends = [];
guess_names =[];


def filter_guess(guess):
    singleton_resultado.objeto.data = guess;
    for data in guess:
         friends_cache.append(data.friends.name);
         guess_names.append(data.name);
         
    union_friends();
    seek_guess_friends();
        
        
def union_friends():
    for data in friends_cache:
        for friend in data:
            friends.append(friend);
            
    del friends_cache[:]
    

def seek_guess_friends():
    for index, guess in enumerate(guess_names):
        if guess in friends:
            singleton_resultado.objeto.guests_of_my_guests.append(guess);
            del singleton_resultado.objeto.data[index]

            