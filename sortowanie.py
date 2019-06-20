li = [9, 6, 8, 2, 1, 7, 4, 3, 5, 10]

s_li = sorted(li) #tworzy przesortowana liste z innej listy
r_li = sorted(li,reverse=True) #sortuje w odwrotnej kolejnosci

print(s_li)
print(r_li)

negative_li = [-4, -3, -2, 1, 5, 6]
sorted_nli = sorted(negative_li, key = abs) #sortuje wg wartosci bezwzglednej

print(sorted_nli)