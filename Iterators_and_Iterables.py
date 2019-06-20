#iterable - to cos po czym mozna iterowac np. lista

nums = [1, 2, 3]

print(dir(nums)) #jezeli cos jest iterable to w dir musi byc metoda __iter__

#iterator - to obiekt ktory wie gdziej jest podczas iteracji
#iterator bedzie mial np. metode next()

i_nums = iter(nums) #to jest tworzenie obiektu iteratora, w tle tak naprawde wywoluje __iter__

# print(next(i_nums)) #teraz iterator ma metode next() ktora wywoluje nastepna wartosc i zapamietuje miejsce w ktorym skonczyl
# print(next(i_nums))
# print(next(i_nums))#jak wyjedziemy poza zakres to dostaniemy execption StopIteration

while True: #to w zasadzie jest to co dzieje sie w tle dla petli for jak iterujemy po jakiejs liscie
    try:
        iteam = next(i_nums)
        print(iteam)
    except StopIteration:
        break

#tworzenie klasy ktora bedzie miala iterator

class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

numbers = MyRange(1,10) #tworzymy obiekt naszej klasy

for number in numbers: #i teraz mozna po nim normalnie iterowac
    print(number)