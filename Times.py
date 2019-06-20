import  datetime   #podstawowa biblioteka do pracy z czasem
import pytz

#sa daty naive ktore nie maja narzedzi do rozpoznowania np. time zone
#sa daty aware ktore takie narzedzia maja

d = datetime.date(2019, 4, 8) # podstawowy sposob tworzenia daty
today = datetime.date.today() # zwraca dzisiejsza date
today_year = today.year # mozna pobierac tylko rok, dzien, miesiac
print(today_year)

print(today.weekday()) # zwraca nr dnia gdzie poniedzialek to 0
print(today.isoweekday()) #zwraca nr dnia gdzie poniedzialek to 1

t_delta = datetime.timedelta(days=7) # zmienna ktorej mozna uzywac do dzialania na datach, tutaj przechowuje roznice 7dni
print(today + t_delta) #przy uzycie timedelta dodajemy 7dni do dzisiejszej daty

my_birthDay = datetime.date(2019,9,4)

#tutaj zaczac kopiowanie
#TODO: dodac to do tutoriala

til_myBirthDay = my_birthDay - today #dzialania na 2 datach zwracaja time delta

print(til_myBirthDay)
print(til_myBirthDay.total_seconds()) #metoda ktora zwraca ilosc sekund

print('')
print('=======================')
print('')

t = datetime.time(9,45,3) #tworzy zmienna przechowujaca godzine
print(t)
print(t.hour) #mozna wywolywac tylko godzine,min,sekunde,lub mikrosekunde

print('')
print('=======================')
print('')

dt = datetime.datetime(2019,5,10,17,45,15) # tworzy zmienna przechowujaca zarowno date jak i czas
print(dt)
print(dt.date()) #mozna wywolywac tylko date
print(dt.time()) #mozna wywolywac tylko czas
print(dt.day) #mozna zwracac tylko dzien
print(dt.hour) #mozna wyciagac tylko godzine

new_delta = datetime.timedelta(hours=6) #delta godzinowa
print(dt + new_delta) #mozna dodawc tylko godziny

dt_withzone = datetime.datetime(2019,5,10,12,45,21,tzinfo=pytz.UTC) #tworzy zmienna czasowa ktora uwzglednia strefy czasowe (stefa to +0.00)
dt_warsawTimezone = dt_withzone.astimezone(pytz.timezone('Europe/Warsaw')) #zwraca dana date po uwzwglednieniu zmiany czasu dla strefy czasowej (tutaj Warszawa)
print(dt_withzone)
print(dt_warsawTimezone)

# for tz in pytz.all_timezones: # wyswietla wszystkie strefy czasowe
#     print(tz)