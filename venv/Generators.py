#generator
#generator dziala w taki sposob ze przekazuje pojedynczo wartosci
#czyli w pamieci przechowuje naraz jeden rekord z listy -> to bardzo wplywa na wydajnosc
def square_numbers(numbers):
    for i in numbers:
        yield (i * i) #slowo kluczowe yield odpowiada za to ze funkcja jest generatorem


my_numb = square_numbers([1, 2, 3, 4, 5])

print(next(my_numb)) #wywoluje pierwsza wartosc
print(next(my_numb)) #wywoluje nastepna wartosc ze stosu

for num in my_numb: #mozemy po tym generowac
    print(num)
print("=================================")
# second_nums = [x*x for x in [1, 2, 3, 4, 5]] #to jest conprehensiv list
second_nums = (x*x for x in [1, 2, 3, 4, 5]) #to jest conprehensiv generator (zamiast [] jest () )

for second_num in second_nums:
    print(second_num)

print(list(second_nums)) #generatory mozna konwertowac na listy