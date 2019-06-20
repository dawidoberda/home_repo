import logging

#logging level:
#DEBUG -> dokladne informacje, najczesciej potrzebne przy diagnozowaniu problemow
#INFO -> potwierdzenie czy wszystko dziala normalnie
#WARNINGS -> wskaznik dotyczacy tego ze dzieje sie cos nie oczekiwanego albo nie dlugo wystapi jakis problem (np. konczy sie miejsce na dysku)
#ERROR -> informacje ze z jakis powodow program nie mogl wykonac danych operacji
#CRITICAL -> powazny blad dotyczacy funkcjonowania calego programu

#Poziomy sa wymienione w kolejnosci. Tzn jezeli lvl jest ustawiony na WARNINGS to logowane beda WARNINGS, ERROR, CRITICAL ale beda ignorowane DEBUG oraz INFO
#Poziomem ustawionym domyslnie jest WARNINGS

#ponizej tworzymy loggera i ustalamy jego nazwe na nawe danego modulu (tutaj main bo odpalamy bezposrednio)
#jezeli tego nie zrobimy to przy imporcie innego modulu ktory tez loguje bedzie sie nam to klocic
#nawet jezeli czegosc tutaj nie dodamy to wezmie informacje z glownego root loggera. Dopiero bezsposrednie napisanie czegos zmienia danego loggera
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) #nadpisujemy poziom logowania

formmater = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s') #ustawiamy nawy format

file_handler = logging.FileHandler('mainlogger.log') # towrzymy uchwyt do nowego pliku
#mozna tez tworzyc streamHandler ktory bedzie przekazywal do konsoli
file_handler.setFormatter(formmater) #nadpisujemy format

logger.addHandler(file_handler) #nadpisujemy plik .log


#zmiana pozniomu logowania na DEBUG
#zapis do pliku filename
#zmiana formatu loga. szczegolu w dokumentacji
#logging to ustawienie glownego loggera (root)
#logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(name)s:%(message)s') #jezeli ustawilismy inny logger to ten mozna wylaczyc

def add(x,y):
    return x+y

def substract(x,y):
    return x-y


def multiply(x,y):
    return x * y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        #logger.error('Nie mozna dzielic przez 0') #przyklad logowania bledu
        logger.exception('Nie mozna dzielic przez 0')  # mozna tez uzyc exception, zaloguje tez tresc bledu z debuggera
    else:
        return result


num_1 = 10
num_2 = 0

add_results = add(num_1, num_2)
logger.info('wynik dodawania to {}'.format(add_results)) #to bedzie ignorowane jezeli logging level=WARNINGS
#logging.warning('wynik dodawania to {}'.format(add_results)) #to bedzie wyswietlone w konsoli

sub_results = substract(num_1, num_2)
logger.info('wynik odejmowania to {}'.format(sub_results))

multiply_results = multiply(num_1, num_2)
logger.info('wynik mnozenia to {}'.format(multiply_results))

divide_results = divide(num_1, num_2)
logger.info('wynik dzielenia to {}'.format(divide_results))