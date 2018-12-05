import psycopg2
import psycopg2.extras
import numpy as np
from matplotlib import pyplot as plt

# try:
#     conn = psycopg2.connect(
#         "dbname='sample1' user='thelampshade' host='localhost' password='dbpass'")
# except:
#     print("I am unable to connect to the database")


def removeDups(dbName='sample1', tableName='games', uniqueCol='id', user='thelampshade', host='localhost',
    password='dbpass'):
    try:
        conn = psycopg2.connect(f"dbname='{dbName}' user='{user}' host='{host}' password='{password}'")
    except:
        print("I am unable to connect to the database")
        return False
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cur.execute(f"""delete from {tablename}
            where {uniqueCol} not in (
                select min({uniqueCol})
                from {tableName}
                group by title, system
            );""")
    except:
        print("Can't SELECT from games 1")
        return False
    conn.commit()
    try:
        cur.execute("""SELECT * from games""")
    except:
        print("I can't SELECT from games 2")
    rows = cur.fetchall()
    print("\nShow me the databases:\n")
    for row in rows:
        print("   ", row)
    cur.close()
    conn.close()


def graphConsoles(dbName='sample1', tableName='games', graphCategory='system', user='thelampshade', host='localhost',
    password='dbpass'):
    try:
        conn = psycopg2.connect(
        f"dbname='{dbName}' user='{user}' host='{host}' password='{password}'")
    except:
        print("I am unable to connect to the database")
        return False
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cur.execute(f"""SELECT system, count(*)
        FROM {tableName}
        group by {graphCategory}
        ;""")
    except:
        print("query failed")
    data = cur.fetchall()
    columns = []
    rows = []
    for entry in data:
        columns.append(entry[0])
        rows.append(entry[1])
    plt.bar(columns, rows, align='center')
    plt.title(f'{tableName} by {graphCategory}')
    plt.xlabel(graphCategory)
    plt.ylabel('COUNT')
    plt.show()
    



# dryer
# removeDups("sample1", "games", 'game_id')
graphConsoles("sample1", "games", 'system')


    




# gamedict = ({"title": "Rock n'' Roll Racing", "system": "SNES", },
#             {"title": "Blackthorne", "system": "SNES"},
#             {"title": "The Lost Vikings", "system": "SNES"})

# cur.executemany(
#     """INSERT INTO games(title,system) VALUES (%(title)s, %(system)s)""", gamedict)

# conn.commit()

# try:
#     cur.execute("""SELECT * from games""")
# except:
#     print("I can't SELECT from games")

# rows = cur.fetchall()

# print("\nShow me the databases:\n")

# for row in rows:
#     print("   ", row)

# cur.close()
# conn.close()

   # result = []
# for value in cur.fetchall():
#     tmp = {}
#     for (index, column) in enumerate(value):
#         tmp[columns[index][0]] = column
#     result.append(tmp)
# rows = [item for sublist in rows for item in sublist]
# print(rows)
