from django.shortcuts import render
import json
import urllib.request as ur


def index(request):

    a = 0

    response = ur.urlopen("https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/COVID19_Indonesia_per_Provinsi/FeatureServer/0/query?where=1%3D1&outFields=Kode_Provi,Provinsi,Kasus_Posi,Kasus_Semb,Kasus_Meni&outSR=4326&f=json")
    
    json_content = json.loads(response.read())
    provinsi = []
    positif = []
    sembuh = []
    meninggal = []

    while a <= 33:
        
        nama_provinsi = json_content['features'][a]['attributes']['Provinsi']
        kasus_positif = json_content['features'][a]['attributes']['Kasus_Posi']
        kasus_sembuh = json_content['features'][a]['attributes']['Kasus_Semb']
        kasus_meninggal = json_content['features'][a]['attributes']['Kasus_Meni']
    
        
        provinsi.append(nama_provinsi)
        positif.append(kasus_positif)
        sembuh.append(kasus_sembuh)
        meninggal.append(kasus_meninggal)

        a=a+1

    zippedList = zip(provinsi, positif, sembuh, meninggal)
    print(zippedList)

    context = {
        'provinsi':provinsi,
        'positif':positif,
        'sembuh':sembuh,
        'meninggal':meninggal,
        'list':zippedList

    }
    return render(request, 'index.html', context)