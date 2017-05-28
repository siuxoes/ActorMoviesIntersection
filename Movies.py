addMore = True
nombreActores = []
times = 1

import requests, json
headers = {'User-agent':'Mozilla/5.0'}

while addMore:
    actor = input("Introduce el nombre de un actor que desea buscar: ")
    URL = "http://suggestqueries.google.com/complete/search?client=firefox&q="
    URL +=actor.upper()
    response = requests.get(URL, headers=headers)
    result = json.loads(response.content.decode('utf-8'))
    respuesta =input("Según Google, el primer resultado del actor introducido es: {0} , ¿es correcto? Si/No: ".format(result[1][0].upper()))
    while respuesta.lower() not in ["si","no","s","n"]:
        respuesta = input(
            "Según Google, el primer resultado del actor introducido es: {0} , ¿es correcto? Si/No: ".format(
                result[1][0].upper()))
    if respuesta.lower() in ["si", "s"]:
        nombreActores.append(result[1][0].upper())
    if len(nombreActores) > 0:
        print()
        print("Listado de actores actuales: ")
        lista = [[i, j] for i, j in enumerate(nombreActores)]
        for x in lista:
            x[0] += 1
            print("{0} - {1}".format(str(x[0]),x[1]))
        print()
    if len(nombreActores) >= 2:
        respuesta = input("¿Desea añadir más actores? Si / No ")
        while respuesta.lower() not in ["si", "no", "s", "n"]:
            respuesta = input("¿Desea añadir más actores? Si / No ")
        if respuesta.lower() in ['n', 'no']:
            addMore = not addMore

import urllib.request
import requests

def get_peoples_id(listaEntrada):
    listaSalida = []
    for persona in listaEntrada:
        persona = urllib.request.quote(persona)
        URL = "https://api.themoviedb.org/3/search/person?api_key=6571f3c9bf9f6be28a99b58842d35298&language=en-US&query=" + persona +"&page=1&include_adult=false"
        r = requests.get(URL)
        if r.ok:
            print("okey!")
        print(r)
        d = r.json()

        listaSalida.append(d["results"][0]["id"])
    return listaSalida

def get_movies_list(listaEntrada):
    listaSalida = []

    for actor_lista in listaEntrada:
        actor_lista = str(actor_lista)
        URL = url = "https://api.themoviedb.org/3/person/" + actor_lista + "?api_key=6571f3c9bf9f6be28a99b58842d35298&append_to_response=credits"
        r = requests.get(url)
        if r.ok:
            print("okey!")
        print(r)

        d = r.json()
        r.close()
        print(d)
        movies = d["credits"]["cast"]
        movies_dict = {}
        for x in movies:
            movies_dict[x["id"]] = x["original_title"]
        listaSalida.append(movies_dict)
    return listaSalida



listaIdActores = get_peoples_id(nombreActores)
listaPeliculas = get_movies_list(listaIdActores)

for x in listaPeliculas:
    print(x)
def intersection_List(listaEntrada):
    return set(listaEntrada[0]).intersection(*listaEntrada)

listaPeliculasComunes = intersection_List(listaPeliculas)

print()
print("COINCIDENCIAS ENTRE LOS ACTORES:")
print()
seq = 1
for x in nombreActores:
    print(" " * 19 + str(seq)+"\t" + x)
    seq += 1
print()

seq = 1
print("PELICULAS: ")
for x in listaPeliculasComunes:
    print("{0:20} \t {1:50}".format(seq, listaPeliculas[0][x]))
    seq+=1

# actores = [2231, 3223]
# url = 'https://api.themoviedb.org/3/person/2231?api_key=6571f3c9bf9f6be28a99b58842d35298&append_to_response=credits'
#
# r = requests.get(url)
# if r.ok:
#     print("okey!")
# print(r)
#
# d = r.json()
# r.close()
# movies = d["credits"]["cast"]
# movies_dict = {}
# for x in movies:
#     movies_dict[x["id"]] = x["original_title"]
#
#
#
# url = 'https://api.themoviedb.org/3/person/3223?api_key=6571f3c9bf9f6be28a99b58842d35298&append_to_response=credits'
#
# re = requests.get(url)
# if re.ok:
#     print("okey!")
# print(re)
#
# x = re.json()
#
# re.close()
# movies_2 = x["credits"]["cast"]
# movies_dict_2 = {}
# for x in movies_2:
#     movies_dict_2[x["id"]] = x["original_title"]
#
# variable = ""
# print("COINCIDENCIAS ENTRE LOS ACTORES:")
# seq = 1
# for actor in actores:
#     url = "https://api.themoviedb.org/3/person/" + str(actor) + "?api_key=6571f3c9bf9f6be28a99b58842d35298&language=en-US"
#     url.format(str(actor))
#     re = requests.get(url)
#     x = re.json()
#     name = x["name"]
#     print("{0}\t{1}".format(str(seq), name))
#     seq+=1
#
# for (key, value) in set(movies_dict.items()) & set(movies_dict_2.items()):
#     print ('{0:20}: {1:50} está en las dos listas'.format(key, value))
#
# import google
#
# #d = google.search("hola")
# #print(next(d))
#
# import requests, json
# URL="http://suggestqueries.google.com/complete/search?client=firefox&q=samuel l"
# headers = {'User-agent':'Mozilla/5.0'}
# response = requests.get(URL, headers=headers)
# result = json.loads(response.content.decode('utf-8'))
# print(result[1][0])
