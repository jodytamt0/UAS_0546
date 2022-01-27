import requests
from mysql import connector
# https://jsonplaceholder.typicode.com/posts

config = connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_akademik_0546"
)

def getData():
    endpoint = "posts"
    base_url = "https://api.abcfdab.cfd/"
    response = requests.get(base_url+endpoint)
    return response.json()

def getDataEndpoint(endpoint):
    base_url = "https://api.abcfdab.cfd/"
    response = requests.get(base_url + endpoint)
    return response.json(), response.status_code, response.headers

def parsingData(data, key):
    newLists = []

    for d in data['data']:
        for k, v in d.items():
            if k == key:
                newLists.append(v)

    if len(newLists) != 0:
        return newLists
    else:
        return "Data Not Found, Please Check Your Key!"

def insertData():
    cursor = config.cursor()
    data = data_posts['data']
    cursor.executemany("""
    INSERT INTO tbl_students_0546 (id, nim, nama, jk, jurusan, alamat)
    VALUES (%(id)s, %(nim)s, %(nama)s, %(jk)s, %(jurusan)s, %(alamat)s)""", data)
    config.commit() 

if __name__ == '__main__':
    data = getDataEndpoint("students")
    data_posts, status_code_posts, headers_posts = data
    posts_id = parsingData(data_posts, 'id')
    posts_nim = parsingData(data_posts, 'nim')
    posts_nama = parsingData(data_posts, 'nama')
    posts_jk = parsingData(data_posts, 'jk')
    posts_jurusan = parsingData(data_posts, 'jurusan')
    posts_alamat = parsingData(data_posts, 'alamat')
    insertData()
    print("Data Berhasil Ditambahkan")
