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
        
        elif(a == 2):
            sumbar = []
            sumbar.append(provinsi)
            sumbar.append(kasus_positif)
            sumbar.append(kasus_sembuh)
            sumbar.append(kasus_meninggal)
        
        elif(a == 3):
            riau = []
            riau.append(provinsi)
            riau.append(kasus_positif)
            riau.append(kasus_sembuh)
            riau.append(kasus_meninggal)
        
        elif(a == 4):
            jambi = []
            jambi.append(provinsi)
            jambi.append(kasus_positif)
            jambi.append(kasus_sembuh)
            jambi.append(kasus_meninggal)
        
        elif(a == 5):
            sumsel = []
            sumsel.append(provinsi)
            sumsel.append(kasus_positif)
            sumsel.append(kasus_sembuh)
            sumsel.append(kasus_meninggal)
        
        elif(a == 6):
            bengkulu = []
            bengkulu.append(provinsi)
            bengkulu.append(kasus_positif)
            bengkulu.append(kasus_sembuh)
            bengkulu.append(kasus_meninggal)
        
        elif(a == 7):
            kep_bangkabelitung = []
            kep_bangkabelitung.append(provinsi)
            kep_bangkabelitung.append(kasus_positif)
            kep_bangkabelitung.append(kasus_sembuh)
            kep_bangkabelitung.append(kasus_meninggal)
        
        elif(a == 8):
            lampung = []
            lampung.append(provinsi)
            lampung.append(kasus_positif)
            lampung.append(kasus_sembuh)
            lampung.append(kasus_meninggal)
        
        elif(a == 9):
            kep_riau = []
            kep_riau.append(provinsi)
            kep_riau.append(kasus_positif)
            kep_riau.append(kasus_sembuh)
            kep_riau.append(kasus_meninggal)
        
        elif(a == 10):
            jakarta = []
            jakarta.append(provinsi)
            jakarta.append(kasus_positif)
            jakarta.append(kasus_sembuh)
            jakarta.append(kasus_meninggal)
        
        elif(a == 11):
            jabar = []
            jabar.append(provinsi)
            jabar.append(kasus_positif)
            jabar.append(kasus_sembuh)
            jabar.append(kasus_meninggal)
        
        elif(a == 12):
            jateng = []
            jateng.append(provinsi)
            jateng.append(kasus_positif)
            jateng.append(kasus_sembuh)
            jateng.append(kasus_meninggal)
        
        elif(a == 13):
            yogyakarta = []
            yogyakarta.append(provinsi)
            yogyakarta.append(kasus_positif)
            yogyakarta.append(kasus_sembuh)
            yogyakarta.append(kasus_meninggal)
        
        elif(a == 14):
            jatim = []
            jatim.append(provinsi)
            jatim.append(kasus_positif)
            jatim.append(kasus_sembuh)
            jatim.append(kasus_meninggal)
        
        elif(a == 15):
            banten = []
            banten.append(provinsi)
            banten.append(kasus_positif)
            banten.append(kasus_sembuh)
            banten.append(kasus_meninggal)
        
        elif(a == 16):
            bali = []
            bali.append(provinsi)
            bali.append(kasus_positif)
            bali.append(kasus_sembuh)
            bali.append(kasus_meninggal)
        
        elif(a == 17):
            ntb = []
            ntb.append(provinsi)
            ntb.append(kasus_positif)
            ntb.append(kasus_sembuh)
            ntb.append(kasus_meninggal)
        
        elif(a == 18):
            ntt = []
            ntt.append(provinsi)
            ntt.append(kasus_positif)
            ntt.append(kasus_sembuh)
            ntt.append(kasus_meninggal)
        
        elif(a == 19):
            kalbar = []
            kalbar.append(provinsi)
            kalbar.append(kasus_positif)
            kalbar.append(kasus_sembuh)
            kalbar.append(kasus_meninggal)
        
        elif(a == 20):
            kalteng = []
            kalteng.append(provinsi)
            kalteng.append(kasus_positif)
            kalteng.append(kasus_sembuh)
            kalteng.append(kasus_meninggal)
        
        elif(a == 21):
            kalsel = []
            kalsel.append(provinsi)
            kalsel.append(kasus_positif)
            kalsel.append(kasus_sembuh)
            kalsel.append(kasus_meninggal)
        
        elif(a == 22):
            kaltim = []
            kaltim.append(provinsi)
            kaltim.append(kasus_positif)
            kaltim.append(kasus_sembuh)
            kaltim.append(kasus_meninggal)
        
        elif(a == 23):
            kaltara = []
            kaltara.append(provinsi)
            kaltara.append(kasus_positif)
            kaltara.append(kasus_sembuh)
            kaltara.append(kasus_meninggal)
        
        elif(a == 24):
            sulut = []
            sulut.append(provinsi)
            sulut.append(kasus_positif)
            sulut.append(kasus_sembuh)
            sulut.append(kasus_meninggal)
        
        elif(a == 25):
            sulteng = []
            sulteng.append(provinsi)
            sulteng.append(kasus_positif)
            sulteng.append(kasus_sembuh)
            sulteng.append(kasus_meninggal)
        
        elif(a == 26):
            sulsel = []
            sulsel.append(provinsi)
            sulsel.append(kasus_positif)
            sulsel.append(kasus_sembuh)
            sulsel.append(kasus_meninggal)
        
        elif(a == 27):
            sultengg = []
            sultengg.append(provinsi)
            sultengg.append(kasus_positif)
            sultengg.append(kasus_sembuh)
            sultengg.append(kasus_meninggal)
        
        elif(a == 28):
            gorontalo = []
            gorontalo.append(provinsi)
            gorontalo.append(kasus_positif)
            gorontalo.append(kasus_sembuh)
            gorontalo.append(kasus_meninggal)
        
        elif(a == 29):
            sulbar = []
            sulbar.append(provinsi)
            sulbar.append(kasus_positif)
            sulbar.append(kasus_sembuh)
            sulbar.append(kasus_meninggal)
        
        elif(a == 30):
            maluku = []
            maluku.append(provinsi)
            maluku.append(kasus_positif)
            maluku.append(kasus_sembuh)
            maluku.append(kasus_meninggal)
        
        elif(a == 31):
            maluku_utara = []
            maluku_utara.append(provinsi)
            maluku_utara.append(kasus_positif)
            maluku_utara.append(kasus_sembuh)
            maluku_utara.append(kasus_meninggal)
        
        elif(a == 32):
            papua = []
            papua.append(provinsi)
            papua.append(kasus_positif)
            papua.append(kasus_sembuh)
            papua.append(kasus_meninggal)
            print(papua)
        
        elif(a == 33):
            papua_barat = []
            papua_barat.append(provinsi)
            papua_barat.append(kasus_positif)
            papua_barat.append(kasus_sembuh)
            papua_barat.append(kasus_meninggal)

        a=a+1

    context = {
        'aceh':aceh,
        'sumut':sumut,
        'sumbar':sumbar,
        'riau':riau,
        'jambi':jambi,
        'sumsel':sumsel,
        'bengkulu':bengkulu,
        'kep_bangkabelitung':kep_bangkabelitung,
        'lampung':lampung,
        'kep_riau':kep_riau,
        'jakarta':jakarta,
        'jabar':jabar,
        'jateng':jateng,
        'yogyakarta':yogyakarta,
        'jatim':jatim,
        'banten':banten,
        'bali':bali,
        'ntb':ntb,
        'ntt':ntt,
        'kalbar':kalbar,
        'kalteng':kalteng,
        'kalsel':kalsel,
        'kaltim':kaltim,
        'sulut':sulut,
        'sulteng':sulteng,
        'sulsel':sulsel,
        'sultengg':sultengg,
        'gorontalo':gorontalo,
        'sulbar':sulbar,
        'maluku':maluku,
        'maluku_utara':maluku_utara,
        'papua':papua,
        'papua_barat':papua_barat,

    }
    return render(request, 'index.html', context)