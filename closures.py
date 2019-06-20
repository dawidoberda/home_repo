import logging #biblioteka do uzywania logowania

logging.basicConfig(filename='log_exp.log', level=logging.INFO) #tworzymy plik do logowania

def outer_function(msg):
    message = msg

    def inner_function(name):
        print('{0} {1} nice to meet You !!'.format(msg, name))
        logging.info('Przywitana {0}'.format(name)) #logowanie informacji do pliku

    return inner_function

hi_func = outer_function('Hi') #przypisujemy funkcje z wewnatrz innej funkcji do zmiennej
hello_func = outer_function('Hello')

hi_func('Dawid') #pozniej uzywamy tej zmiennej jak funkcje
hello_func('Mateusz')