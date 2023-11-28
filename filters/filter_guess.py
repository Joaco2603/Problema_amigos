
friends_cache = [];
friends = [];
guess_names =[];
guests_of_my_guests = [];


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
    
    for guess in guess_names:
        if guess in friends:
            print(guess);
            guests_of_my_guests.append(guess);
    
    # if friends[0].find("Ca") != -1:
    #     print("No");
    # else:
    #     print("Si");