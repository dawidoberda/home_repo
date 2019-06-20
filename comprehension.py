#skrocony sposob tworzenie list

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = [n for n in nums] #list compregension, kopiowanie innej listy
print(my_list)

my_list2 = [n*n for n in nums]
print(my_list2)

my_list3 = [n for n in nums if n%2==0] #mozemy tez dodawac warunki, tutaj zwroci tylko parzyste
print(my_list3)

my_list4 = [(letter, num) for letter in 'abcd' for num in range(4)] #mozemy zagniezdzac wewnatrz funkcje
print(my_list4)

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverin', 'Deadpool']

my_dict = {name: hero for name, hero in zip(names, heros)} #comprehension slownika
print(my_dict)

