#przyklad dekoratora
#dekorator to funkcja ktora przyjmuje jako argument funkcje i zwraca funkcje
#calym sensem uzywania dekoratorow jest to ze mozemy dodawac funkcjonalnosci do funkcji bez zmieniania jej kodu zrodlowego
def prefix_dekorator(prefix): #kolejne zagniezdzenie aby dekorator mogl przyjac argument
    def decorator_func(oryginal_func):
        def wrapper_func(*args, **kwargs): #args i kwargs sa potrzebne aby mozna bylo dekorowac tez funkcje z ktore przyjmuja argumenty
            print(prefix, 'Ta czesc zostanie wywolana przed funkcja {}'.format(oryginal_func.__name__)) #dodanie linijki kodu.(rozszerzenie funkcjonalnosci
            return oryginal_func(*args, **kwargs)
        return wrapper_func
    return decorator_func

#zamiast uzywania funkcji dekoratora mozna stworzyc klase dekoratora ( o identycznym dzialaniu)
# class decorator_class(object):
#
#     def __init__(self, oryginal_func):
#         self.oryginal_func = oryginal_func
#
#     def __call__(self, *args, **kwargs):
#         print('Ta czesc zostanie wywolana przed funkcja {}'.format(self.oryginal_func.__name__)) #dodanie linijki kodu.(rozszerzenie funkcjonalnosci
#         return self.oryginal_func(*args, **kwargs)

# #Pierwszy sposob: (z przypisaniem do zmiennej)
# #funkcja ktora bedzie dekorowana
# def display():
#     print('display function ran')
#
# dekorated_display = decorator_func(display) #przypisanie funkcji z dekoratora do zmiennej
#
# dekorated_display()

#metoda druga (w ktorej uzywamy @ i nadpisujemy funkcje zachowujac jej nazwe
@prefix_dekorator('Testing') #mozemy wywolac dekorator z parametrem
# @decorator_class
def display():
    print('display function ran')

@prefix_dekorator('Testing')
# @decorator_class
def display_info(name, age):
    print('argumenty w tej funkcji to : ({},{})'.format(name, age))


display() #tutaj wywolujemy ja bezposrednio bo jest nadpisana
display_info('Dawid', '29')