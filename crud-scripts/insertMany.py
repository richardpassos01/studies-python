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

rangeValue = range(2)

for i in rangeValue:
    name = input('Say my name:');
    age = input('Say my age:');
    cursor.execute("INSERT INTO users(name, age) VALUES ('{}', {})".format(name, age));
    connection.commit();
