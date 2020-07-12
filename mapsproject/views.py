from django.shortcuts import render
import json
import urllib.request as ur


def index(request):

    a = 0

    response = ur.urlopen("https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/COVID19_Indonesia_per_Provinsi/FeatureServer/0/query?where=1%3D1&outFields=Kode_Provi,Provinsi,Kasus_Posi,Kasus_Semb,Kasus_Meni&outSR=4326&f=json")
    
    json_content = json.loads(response.read())

    while a <= 33:
        provinsi = json_content['features'][a]['attributes']['Provinsi']
        kasus_positif = json_content['features'][a]['attributes']['Kasus_Posi']
        kasus_sembuh = json_content['features'][a]['attributes']['Kasus_Semb']
        kasus_meninggal = json_content['features'][a]['attributes']['Kasus_Meni']
        
        if(a == 0):
            aceh = []
            aceh.append(provinsi)
            aceh.append(kasus_positif)
            aceh.append(kasus_sembuh)
            aceh.append(kasus_meninggal)
        
        elif(a == 1):
            sumut = []
            sumut.append(provinsi)
            sumut.append(kasus_positif)
            sumut.append(kasus_sembuh)
            sumut.append(kasus_meninggal)

        a=a+1

    context = {
        'aceh':aceh,
        'sumut':sumut,
    }
    return render(request, 'index.html', context)