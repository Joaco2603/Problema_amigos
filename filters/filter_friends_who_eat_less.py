from patterns.Singleton import singleton_resultado;

Repetition = [];

def filter_friends_who_eat_less():
    for guess in singleton_resultado.objeto.data:
        for name, dishes in zip(guess.friends.name,guess.friends.dishes):
            Repetition.append(name);
            dictionary_friends = dict(name=name,dishes=dishes)
            print(Repetition);