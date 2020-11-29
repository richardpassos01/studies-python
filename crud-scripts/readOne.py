import mysql.connector;

connection = mysql.connector.connect(
    host='localhost',
    user='richard',
    password='123456',
    database='database_test',
    charset='utf8',
);

cursor = connection.cursor(
    dictionary=True
);

id = input('Fala tu: ');

cursor.execute("SELECT * FROM users WHERE id={}".format(id));
users = cursor.fetchall();

print(users);
