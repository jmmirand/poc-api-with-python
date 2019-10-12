from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from apis import api2


import os

# Comprobar que las variables de entornos necesias existen
strMensajeVaribleError = "ERROR , NO SE HA DEFINIDO LA VARIABLE : "


def checkEnviroment():
    bCheckEnvironment = True
    listVariables = ["API_CONFIG"]

    for variable in listVariables :
        if ( variable not in os.environ):
            print(strMensajeVaribleError + variable)
            bCheckEnvironment = False
        else:
            print ( "Variable Configured " + variable  +  " : " + os.environ[variable])


    return bCheckEnvironment


bEntorno = checkEnviroment()

if (bEntorno):

    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    api2.init_app(app)

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)
