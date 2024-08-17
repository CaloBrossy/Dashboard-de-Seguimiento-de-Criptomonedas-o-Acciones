from flask import Flask, render_template, request #Importamos desde la biblioteca flask
import requests
import pandas as pd

#API CONFIG

API_KEY = 'c8550e8a17285b13eda1eb824004b6fb32c1b2cb3ab5b075d4da9148a1909668' #Defino una variable asi no pego 60 veces esa mierda toda dificil
BASE_URL = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR" #Defino otra variable asi no pego 60 veces esa otra mierda toda dificil

app = Flask (__name__) #Creamos una aplicación que es igual a una instancia de flask (__name__) creo q es por defecto

@app.route("/") #Mi app va a tener una ruta que se va a llamar /
def index(): #Defini una función que se llama index sin ningún parámetro (python cosas no se)
    headers = {
        'Authorization': f'Bearer {API_KEY}' #En nuestro caso la api no requiere una apikey pq ya tiene los parámetros
    }
    response = requests.get(BASE_URL)
    data = response.json()
    price = data['USD']
    price1 = data['JPY']
    price2 = data['EUR']
    return render_template('index.html' , price=price, price2=price2, price1=price1)

#GET --> Obtener información
#POST --> Crear información
#PUT --> Actualizar información
#Delete --> Borrar información :V

if __name__ == '__main__':
    app.run(debug=True) #Si la aplicación es igual main entonces la app correrá en modo de debug