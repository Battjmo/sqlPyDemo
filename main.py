import psycopg2
import psycopg2.extras
import numpy

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



# dryer
removeDups("sample1", "games", 'game_id')

    




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


