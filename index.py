
from helpers.create_friends import create_friends;
from filters import filter_guess, filter_friends_who_eat_less;

def main():
    friends = create_friends();
    filter_guess(friends);
    filter_friends_who_eat_less()
    
    
main();