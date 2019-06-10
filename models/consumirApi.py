import requests

def consumirApi():
    url =  "https://httpbin.org/get"
    r = requests.get('https://httpbin.org/get')
    json_object = r.json()
    #print (json_object)
    host = str(json_object['headers']['Host'] )
    userAgent = str(json_object['headers']['User-Agent'] )
    cadena = "mi host es: "+host+" y mi user-agent es: "+userAgent
    return cadena