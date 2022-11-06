import pydbgen
import psycopg2
import uuid
import names
import random, string
import datetime
from random_word import RandomWords


def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

connection = psycopg2.connect(user="postgres",
                              password="postgres",
                              host="127.0.0.1",
                              port="5432")
connection.autocommit=True
cursor = connection.cursor()
cursor.execute(
"""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
tables = cursor.fetchall()
print(tables)
for table in tables:
    print(table[0])
    cursor.execute(f"""SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table[0]}';""")

    collumns = cursor.fetchall()
    # print('collumns ', collumns)
    cursor.execute(f"SELECT "
                   f"tc.table_schema, "
                   f"tc.constraint_name, "
                   f"tc.table_name, "
                   f"kcu.column_name, "
                   f"ccu.table_schema AS foreign_table_schema, "
                   f"ccu.table_name AS foreign_table_name, "
                   f"ccu.column_name AS foreign_column_name "
                   f"FROM "
                   f"information_schema.table_constraints AS tc  "
                   f"JOIN information_schema.key_column_usage AS kcu ON "
                   f"tc.constraint_name = kcu.constraint_name AND tc.table_schema = kcu.table_schema "
                   f"JOIN information_schema.constraint_column_usage AS ccu ON ccu.constraint_name = tc.constraint_name "
                   f"AND ccu.table_schema = tc.table_schema "
                   f"WHERE "
                   f"tc.constraint_type = 'FOREIGN KEY' "
                   f"AND tc.table_name='{table[0]}';")

    fk = cursor.fetchall()
    for i in range(0, random.randint(1, 200)):
        values = []
        querry = 'INSERT INTO public.' + str(table[0]) +'('
        for data in collumns:
            querry = querry + str(data[0]) + ','
        querry = querry[:len(querry)-1] + ') VALUES('
        for data in collumns:
            is_foreign = False
            for forkey in fk:

                if (data[0] == forkey[3]):

                    try:
                        get_querry = 'SELECT ' + forkey[6] + ' FROM ' + 'public.' + forkey[5] + ' ORDER BY RANDOM() LIMIT 1'
                        # print(get_querry)
                        cursor.execute(get_querry)

                        forkey_value = cursor.fetchall()
                        is_foreign = True

                    except Exception as e:
                        is_foreign = False
                        print(e)

            if (is_foreign):
                if (table[0] == 'lineup' and data[0] == 'profile_uuid'):
                    if (random.random() > 0.5):
                        values.append('NULL')
                    else:
                        values.append('\'' + forkey_value[0][0] + '\'')
                else:
                    values.append('\'' + forkey_value[0][0] + '\'')
            else:

                if (data[1] == 'uuid' or data[1] == 'project_uuid' or data[1] == 'country_uuid'):
                    values.append('\'' + str(uuid.uuid4()) + '\'')
                if (data[1] == 'character varying' or data[1] == 'text'):
                    if (data[0] == 'email'):
                        values.append(str(RandomWords().get_random_word()) + '@gmail.ru')
                    elif(data[0] == 'firstname'):
                        values.append(names.get_first_name())
                    elif (data[0] == 'lastname'):
                        values.append(names.get_last_name())
                    elif (data[0] == 'patronymic'):
                        values.append(names.get_first_name() + 'vich')
                    elif (data[0] == 'gender'):
                        if (random.randint(1,2) < 1.5):
                            values.append("male")
                        else:
                            values.append("other")
                    elif (data[0] == 'phone'):
                        values.append(str(random.randint(1000000, 9999999)))
                    elif (data[0] == 'inn'):
                        values.append(str(random.randint(1000000000, 9999999999)))
                    elif (data[0] == 'phone'):
                        values.append(str(random.randint(1000000, 9999999)))
                    elif (data[0] == 'code'):
                        values.append(str(randomword(2)))
                    elif (data[0] == 'is_visible'):
                        values.append(str('visible'))
                    else:
                        values.append(str(RandomWords().get_random_word()))
                    values[len(values) - 1] = '\'' + values[len(values) - 1] + '\''

                if (data[1] == 'integer'):
                    values.append(random.randint(0, 1000000))
                if (data[1] == 'timestamp without time zone'):
                    values.append('\'' + str(datetime.datetime.now()) + '\'')
            querry = querry + str(values[len(values) - 1]) + ','
        querry = querry[:len(querry)-1] + ');'
        print(querry)
        try:
            cursor.execute(querry)
        except Exception as e: print(e)





