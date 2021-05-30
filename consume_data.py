import requests
import psycopg2
with requests.get('http://127.0.0.1:5000/data/10') as data:
    connection=psycopg2.connect(dbname="stream-feedback", user="postgres", password="amenallah123")
    cur=connection.cursor()
    print(f"INSERTING in postergrsql values")
    buffer=" "
    for chunk in data.iter_content(chunk_size=1):
        if chunk.endswith(b'\n'):
            t=eval(buffer)
            cur.excute(sql, t[0],t[1],t[2],t[4],t[5],t[6])
            buffer=" "
        else:
            buffer += chunk.decode()
    print(data.text)
    connection.close()