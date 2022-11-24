import logging
import urllib.request
import json
from pickle import load

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    args = list()
    args.append(req.get_json().get('linguistica'))
    args.append(req.get_json().get('logicoMatematico'))
    args.append(req.get_json().get('espacial'))
    args.append(req.get_json().get('corporal'))
    args.append(req.get_json().get('musical'))
    args.append(req.get_json().get('interpessoal'))
    args.append(req.get_json().get('intrapessoal'))
    args.append(req.get_json().get('naturalista'))


    if args:
        profession = dict(first_profession = multipleInteligence(args))
        print(profession)
        return func.HttpResponse(json.dumps(profession),
                                 mimetype="application/json")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

def multipleInteligence(args):
    linguistica = float(args[0])
    logicoMatematico = float(args[1])
    espacial = float(args[2])
    corporal = float(args[3])
    musical = float(args[4])
    interpessoal = float(args[5])
    intrapessoal = float(args[6])
    naturalista = float(args[7])

    model = load(urllib.request.urlopen('https://apieleicoesrga6e1.blob.core.windows.net/pkl/dtree.pkl'))

    predict = model.predict([[linguistica, logicoMatematico, espacial,
                            corporal, musical, interpessoal, intrapessoal, naturalista]])

    return predict[0]


