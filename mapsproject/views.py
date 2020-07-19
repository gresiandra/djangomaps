from django.shortcuts import render
import json
import urllib.request as ur
from datetime import date

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

    zippedList = sorted(zip(provinsi, positif, sembuh, meninggal), key=lambda pair: pair[1], reverse=True)

    today = str(date.today())
    print("Today's date:", today)

    response1 = ur.urlopen("https://api.covid19api.com/summary")

    json_content1 = json.loads(response1.read())
    print(json_content1['Countries'][77])
    positif_dunia = '{0:,}'.format(json_content1['Global']['TotalConfirmed'])
    sembuh_dunia = '{0:,}'.format(json_content1['Global']['TotalRecovered'])
    meninggal_dunia = '{0:,}'.format(json_content1['Global']['TotalDeaths'])
    positif_indonesia = '{0:,}'.format(json_content1['Countries'][77]['TotalConfirmed'])
    sembuh_indonesia = '{0:,}'.format(json_content1['Countries'][77]['TotalRecovered'])
    meninggal_indonesia = '{0:,}'.format(json_content1['Countries'][77]['TotalDeaths'])

    context = {
        'provinsi':provinsi,
        'positif':positif,
        'sembuh':sembuh,
        'meninggal':meninggal,
        'list':zippedList,
        'positif_indonesia':positif_indonesia,
        'sembuh_indonesia':sembuh_indonesia,
        'meninggal_indonesia':meninggal_indonesia,
        'positif_dunia':positif_dunia,
        'sembuh_dunia':sembuh_dunia,
        'meninggal_dunia':meninggal_dunia,

    }
    return render(request, 'index.html', context)