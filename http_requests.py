import requests     #biblioteka do http requestow

# r = requests.get('https://xkcd.com/353/')   #tworzy obiek z dana strona
#
# #print(r.text) #zwraca zawartosc strony jak text. W tym wypadku zwroci html !
#
# drawing = requests.get('https://imgs.xkcd.com/comics/python.png')   #tworzy obiek z dana strona tutaj z samym rysunkiem
#
# # with open('content.png','wb') as f: #otwieramy plik w content menager jako wb - write byte
# #     f.write(drawing.content) #content zapisuje zawartosc w bitach, czyli tworzy rysunek
#
# print(r.status_code) #zwraca status http tutaj zwroci 200 czyli ze wszystko OK  (https://pl.wikipedia.org/wiki/Kod_odpowiedzi_HTTP)
# print(r.ok) #sprawdza czy wszystko jest OK ze strona i jezeli jest to zwraca true
# print(r.headers) #zwraca naglowki ze strony


# payload = {'page':2, 'count':25} # zapisujemy dane w formie slownika
# r = requests.get('https://httpbin.org/get', params=payload) #zamiast konstruowac caly adres mozemy czesc przekazac jako params
#
# print(r.url) #drukuje adres z zapytania
#
# print(r.text)

# data_to_send = {'username':'Dawid', 'password':'testing'} #dane do wyslania
# r = requests.post('https://httpbin.org/post', data=data_to_send) #metoda sluzaca do wysylania danych
#
# r_dict = r.json() # mozna zapisac json do slownika
# print(r_dict['form'])

#niektore autentykowanie nie robi sie przez form authentication ale przez basic authentication
r = requests.get('https://httpbin.org/basic-auth/dawid/testing', auth=('dawid','testing'), timeout=3)
print(r)
print(r.text)