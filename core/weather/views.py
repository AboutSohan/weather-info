from django.shortcuts import render

def weather_app(city):
    from bs4 import BeautifulSoup as bs
    import requests
    city = city.replace(' ','+')
    url = f'https://www.google.com/search?q=weather+of+{city}'
    # header configuration
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    cookie = 'OTZ=6870401_32_32__32_; SL_G_WPT_TO=en; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; HSID=AKAFOBR6VxsMcy4WN; SSID=AX_viskpkI7gpNnBa; APISID=GQLq07WODqjRRZOk/As3d_o_t1VvA0UIaD; SAPISID=Dhtsvn757aeTHljE/AHKag9KvZ57Wdwq7z; __Secure-1PAPISID=Dhtsvn757aeTHljE/AHKag9KvZ57Wdwq7z; __Secure-3PAPISID=Dhtsvn757aeTHljE/AHKag9KvZ57Wdwq7z; S=billing-ui-v3=7YY4Y5y8dw2NgpYoN7N_0W8R-_5jYwFX:billing-ui-v3-efe=7YY4Y5y8dw2NgpYoN7N_0W8R-_5jYwFX; SID=Twj27FvAe60TOp6PtJTzHhhs8dwXv7WGSL8OEr-K82K4JA24l7BYCS0z48Rg8LFcgzd0UQ.; __Secure-1PSID=Twj27FvAe60TOp6PtJTzHhhs8dwXv7WGSL8OEr-K82K4JA24HWphhwjhur6m3igPXNoF-A.; __Secure-3PSID=Twj27FvAe60TOp6PtJTzHhhs8dwXv7WGSL8OEr-K82K4JA24rBcU-NQcl9k2FzXLl9znpg.; SEARCH_SAMESITE=CgQIz5cB; AEC=ARSKqsIwv3JcPZ3ysjpsit8y4g6V9eADAOhYDu8vQeAuoz6ms1zlfGmUDFo; NID=511=H-Y0kMPEON1Lo8B0xBxmQLZ4KEjVAFosnApFj9e2v-fma-4poNhyt5q3oAxnamhnbCGReCuP6BzzIQzes_yFI-JPkBLw3WAg_djJBNwNw-mLVze7lqvnH_XFXZYnsyhRuWH1jh-aoj4QwOc1QmnvvF7KZOd6zPDoa-lRaSBy8sIBwRnwx72JiN8dMMhtEAS-9J0sDOmfaRGGeZAXifm9l5cNTtRvqx8X7xUNiNzesI7WziEmqyPGALbVnxulAXreUxqCDO4ZHILwakAQp-6PJNF7m0yPQCopd6Eqbe5g7MK-ZDWFnoQE0k0AxANNmv03-xRrpfIqXjHsFTEWE1XXK9VtINsMSr_p31WyF-Y3ngL2AL33Gfu4p3pFPJnIq-7vB1ar6vETuzab1Ivt9lbcmWRQmRuRB4Sg3zKFzLGMq0zmXcUq4MSg5t5uf7S_KpAa5g; 1P_JAR=2023-02-20-02; DV=s-8_mjnyNVdfwEtSPKiaEkqa01TJZhgtVbcxKQal2AAAAPCYhXNegFgGTgAAAOBRX6N8aZALKQAAAF0qnu00FCAWEQAAAA; SIDCC=AFvIBn-i7Ifc4KKt5qgjKGpp_QnSKBMf3i8xmsu7KqH_DXkE0mL2f3FIz4hlovawr8e-tQOOMFU; __Secure-1PSIDCC=AFvIBn9BTketvpqXNuJBa0umlroSo3nfm0y8ZuzC_sfaHBC1synz2wBLonYTtD6-woTKUlRQZ_rt; __Secure-3PSIDCC=AFvIBn8TSCtSxeBci8xJyawUh7dX2YfpkYSotrv08yIk78_Fo5H3TYbQBVDd0b-lMlA2UqQ31S8'
    language = 'en-US,en;q=0.9,id;q=0.8,ar;q=0.7'

    # session creating & header data passing
    session = requests.Session()
    session.headers['accept-language'] = language
    session.headers['cookie'] = cookie
    session.headers['user-agent'] = user_agent
    # data scrapping
    res = session.get(url)
    soup = bs(res.text, 'html.parser')
    # all data
    my_data = {}
    my_data['region'] = soup.find('span', attrs=('class','BBwThe')).text
    my_data['date'] = soup.find('div', attrs=('id','wob_dts')).text
    my_data['weather'] = soup.find('div', attrs=('id','wob_dcp')).text
    my_data['temperature'] = soup.find('span', attrs=('class','wob_t q8U8x')).text
    return my_data


def home_page(request):
    if request.method == "GET" and 'city' in request.GET:
        user_input_data = request.GET.get('city')
        weather_data = weather_app(user_input_data)
        contex = {'weather_data':weather_data}
    else:
        contex = {}
    return render(request,'index.html', contex)