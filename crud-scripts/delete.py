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

id = input('How ID do you wanna kill? ');
cursor.execute("DELETE FROM users WHERE id='{}'".format(id));
connection.commit();
