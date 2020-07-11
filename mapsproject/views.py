from django.shortcuts import render
import json
import urllib.request as ur


def index(request):

    a = 1

    response = ur.urlopen("https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/COVID19_Indonesia_per_Provinsi/FeatureServer/0/query?where=1%3D1&outFields=Kode_Provi,Provinsi,Kasus_Posi,Kasus_Semb,Kasus_Meni&outSR=4326&f=json")
    
    json_content = json.loads(response.read())

    while a <= 33:

        print("Provinsi: " + str(json_content['features'][a]['attributes']['Provinsi']))
        print("Positif: " + str(json_content['features'][a]['attributes']['Kasus_Posi']))
        print("Sembuh: " + str(json_content['features'][a]['attributes']['Kasus_Semb']))
        print("Meninggal: " + str(json_content['features'][a]['attributes']['Kasus_Meni']))
        print('')
        
        a=a+1

    context = {

    }
    return render(request, 'index.html', context)