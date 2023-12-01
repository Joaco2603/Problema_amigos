
from patterns.Singleton import singleton_resultado; 


friends_cache = [];
friends = [];
guess_names =[];


def filter_guess(guess):
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
    print(guess_names);
    for guess in guess_names:
        if guess in friends:
            singleton_resultado.objeto.guests_of_my_guests.append(guess);
            guess_names.remove(guess)
            print(guess_names)
            print(singleton_resultado.objeto.guests_of_my_guests)
            