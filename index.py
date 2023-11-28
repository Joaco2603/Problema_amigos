
from helpers.create_friends import create_friends;
from filters import filter_guess;


def main():
    friends = create_friends();
    filter_guess(friends);
    
main();