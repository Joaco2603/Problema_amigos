class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, objeto=None):
        if not hasattr(self, 'initialized'):
            self.objeto = objeto
            self.initialized = True
            
            
class Resultado_amigos:
    def __init__(self):
        self.guests_of_my_guests = [];
    
    
resultado_amigos = Resultado_amigos();
singleton_resultado = Singleton(resultado_amigos);


# print(singleton_resultado.objeto.all_array);
# print(singleton_resultado.objeto.guess_names);
# print(singleton_resultado.objeto.friends_names);
# print(singleton_resultado.objeto.dishes_friends);
# print(singleton_resultado.objeto.guests_of_my_guests);