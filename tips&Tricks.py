#Ternary Conditionals
#If w jednej linijce
condition = True
x = 1 if condition else 0
print(x)

#Enumerate
#pozwala przypisac index wartosci z listy ktore iterujemy
names = ['dawid', 'mateusz', 'jagoda', 'barbara', 'figa']
for index, name in enumerate(names, start=1):
    print(index, name)

#unpacking

a, _ = (1,2) #mozemy uzyc "_" aby jasno zaznaczyc ze nie bedziemy uzywac drugiej wartosci z listy
print(a)

a, b, *c, d = (1, 2, 3, 4, 5) # to daje mozliwosc przypisania calej reszty z listy do jednej zmiennej
#lub wstawic jeszcze dodatkowe zmienne na koniec (d)
print(a)
print(b)
print(c)
print(d)

#Setattr/Getattr
class Person():
    pass

person = Person()

person.first = 'Dawid' # w pythonie mozna do klas dynamicznie dodawac pola
person.last = 'Oberda'

#mozna to tez zrobic setattr i uzyc zmiennej zamiast w prost deklarowac:
second_key = 'second'
second_value = 'Mateusz'

setattr(person, second_key, second_value) #ustawiamy zmienna jako nowe pole klasy

print(person.first, person.second, person.last) # i pozniej normalnie sie do nich odwolywac

#mozna tez pole z klasy zapisac do zmiennej:

second = getattr(person, second_key) #zapisujemy pole z klasy person do zmiennej

print(second)

#GetPass
#funkcja do wprowadzania hasel (tak aby nie bylo tego widac na ekranie)

from getpass import getpass
username = input('Username: ')
password = getpass('Password: ')
print('Logging in..')