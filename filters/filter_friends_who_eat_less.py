from patterns.Singleton import singleton_resultado;

def filter_friends_who_eat_less():
    print(singleton_resultado.objeto.data);
    for guess in singleton_resultado.objeto.data:
        for name, dishes in guess.friends.name,guess.friends.dishes:
            dictionary_friends = dict(name=name,dishes=dishes);
            print(dictionary_friends);