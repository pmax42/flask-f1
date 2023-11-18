import mariadb

conn = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         user='root',
         password='root',
         database='f1db')

cur = conn.cursor()

results = cur.execute("SELECT * FROM drivers")

# serialize results into JSON
row_headers=[x[0] for x in cur.description]
rv = cur.fetchall()
json_data=[]
for result in rv:
    json_data.append(dict(zip(row_headers,result)))

# return the results!
print(json_data)