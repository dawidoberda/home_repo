courses = ['Polski', 'Matematyka', 'Fizyka', 'Informatyka']

courses.insert(0,'Biologia')

print(courses)

additionalCourses = []
additionalCourses.append('Kolo Filmowe')
additionalCourses.append('Nauka Programowania')
additionalCourses.append('Przedmiot n')

#courses.insert(0,additionalCourses)
courses.extend(additionalCourses)
print(courses)

popped = courses.pop() #sciaga ostatni element z listy (jak stos) ten element jest usuniety z listy
print(popped)
print(courses)

print(courses.index('Fizyka')) #zwraca nr indeksu danego elementu

print('Polski' in courses) #zmienna boolowska sprawdza czy dany element jest w liscie

for indeks, kurs in enumerate(courses, start=1): #zwraca indeks oraz element listy, start=1 oznacza ze poczatkowy indeks bedzie rowny 1 (to jest opcjonalne)
    print(indeks, kurs)

names_1 = {'dawid', 'mateusz', 'jagoda', 'lilianna'}
names_2 = {'stefan', 'mateusz', 'jagoda', 'gabriel'}

print(names_1.intersection(names_2)) #zwraca czesc wspolna dwoch setsow
print(names_1.difference(names_2)) #z wraca roznice pomiedzy dwoma zbiorami
print(names_1.union(names_2)) #laczy dwa setsy