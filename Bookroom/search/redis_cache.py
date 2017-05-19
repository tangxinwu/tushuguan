import redis
import pymysql

def book_data():
    conn_redis = redis.Redis(host='127.0.0.1')

    try:
        re.match(b'book', conn_redis.keys()[0])
    except:
        conn_db = pymysql.connect(host='127.0.0.1', user='root', password='111111',database='bookroom' ,charset='utf8')
        cur1 = conn_db.cursor()
        cur1.execute('select * from search_book')
        data = cur1.fetchall()
        for i in data:
            id = i[0]
            title = i[1]
            tab = i[2]
            update_time = i[3]
            author = i[4]
            publisher = i[5]
            conn_redis.hmset('book:' + str(id),{'title':title,'tab':tab,'update_time':update_time,'author':author,'publisher':publisher})
            conn_redis.expire('book:' + str(id), 100)


if __name__ == '__main__':
    while True:
        book_data()