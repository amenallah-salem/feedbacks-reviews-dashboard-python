import requests
import psycopg2
with requests.get('http://127.0.0.1:5000/data/10') as data:
    connection=psycopg2.connect(
        dbname='stream-feedback', user='postgres', password='amenallah123'   
    )
    buffer=''
    for chunk in data:
        if chunk.endswith(b'\n'):
            t = eval(buffer)
            print(t)
            buffer=''
        else:
            buffer=chunck.decode()
    print(r.text)