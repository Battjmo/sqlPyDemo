import psycopg2
import psycopg2.extras
import numpy

# try:
#     conn = psycopg2.connect(
#         "dbname='sample1' user='thelampshade' host='localhost' password='dbpass'")
# except:
#     print("I am unable to connect to the database")

def removeDups(dbName, tableName):
    try:
        conn = psycopg2.connect(f"dbname='{dbName}' user='thelampshade' host='localhost' password='dbpass'")
    except:
        print("I am unable to connect to the database")
        return False
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cur.execute("""delete from games
            where game_id not in (
                select min(game_id)
                from games
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


removeDups("sample1", "games")

    




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


