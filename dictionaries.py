student = {'name':'dawid', 'age':'28', 'courses':['Math', 'CompSci']} #definicja slownika (ostatni value to lists)

print(student) #wyswietla pelna liste
print(student['name']) # dostep do zmiennej z danego klucza
print(student.get('name')) #odwolanie do klucza metoda. W przypadku braku danego klucza zwroci none a nie wywali blad
print(student.get('phone','Not found')) #tutaj zamiast none zwroci to co przekazemy w drugim argumencie

student['phone'] = '555-5555' # dodajemy klucz razem z wartoscia

print(student.get('phone','Not found'))

student.update({'name':'mateusz', 'age':'32', 'address': 'chociszewskiego 1/12'})#mozemy zaktualizowac i dodawac pola

print(student)

del student['address']

print(student)
print(student.keys())#mozemy wywolac wszystkie klucze ze slownika
print(student.values())#mozemy wywolac wszystkie wartosc ze slownika
print(student.items()) #zwraca pary klucz-wartosc

for key, value in student.items(): #iterujemy po parach klucz-wartosc
    print(key,value)