import sqlite3

from parser import get_names_champions, champions_kd


def add_champs_kd_to_db() -> None:
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(
            'CREATE TABLE IF NOT EXISTS kd_champs '
            '(name TEXT PRIMARY KEY, q_kd TEXT, w_kd TEXT, e_kd TEXT, r_kd TEXT)'
    )
    con.commit()

    list_names = get_names_champions()
    list_kd = champions_kd()

    for champ in range(len(list_names)):
        cur.execute(
            f"INSERT INTO kd_champs (name, q_kd, w_kd, e_kd, r_kd) VALUES (?, ?, ?, ?, ?)",
            (list_names[champ],
                ','.join(str(x) for x in list_kd[list_names[champ]][0]),
                ','.join(str(x) for x in list_kd[list_names[champ]][1]),
                ','.join(str(x) for x in list_kd[list_names[champ]][2]),
                ','.join(str(x) for x in list_kd[list_names[champ]][3]))
        )
    con.commit()
    cur.close()
    con.close()


def get_names_champs() -> list[str]:
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM kd_champs")
    data = cur.fetchall()
    return [champ[0] for champ in data]
