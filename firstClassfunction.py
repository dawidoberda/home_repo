def square(x):
    return x*x

def cube(x):
    return x*x*x


f = square #mozemy przypisac funkcje do zmiennej i traktowac f jako funkcje

print(f)
print(square)
print(f(5)) #teraz mozna uzywac f jak funkcji


#ponizej przyklad higher order function -> czyli funkcja ktora przyjmuje jako argument inna funkcje lub zwraca funkcje jak wynik

def my_map(funct,arg_list): #przekazujemy funkcje jako pierwszy argument
    results = []
    for i in arg_list:
        results.append(funct(i))   #dla kazdego wyrazu wywolujemy funkcje ktora zostala podana jako pierwszy argument

    return results


squares = my_map(square, [1, 2, 3, 4, 5])
cubes = my_map(cube, [1, 2, 3, 4, 5])

print(squares)
print(cubes)

#przyklad zwracania funkcji (to sie nazywa closure)

def logger(msg):

    def log_message(): #tworzymy wewnetrzna funkcje
        print('Log: ',msg)

    return log_message  #zwracamy to funkcje jako wynik zewnetrznej (bez nawiasow)

log_hi = logger('Hi') #zapisujemy funkcje do zmiennej (ale zapisze sie ta funkcja wewnetrzna)
log_hi() #tak wiec mozemy uzywac teraz log hi jak funkcji (jak w przypadku f)

#przyklad praktyczny

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1('First Line')
print_h1('Second Line')