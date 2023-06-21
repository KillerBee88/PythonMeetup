import sqlite3

BASE = 'meetup.db'


def sql_register_new_user(tg_id, name):
    with sqlite3.connect(BASE) as db:
        cur = db.cursor()
        query = f"""
            INSERT INTO 'users' (tg_id, name)
            VALUES ('{tg_id}', '{name}')
            """
        cur.execute(query)
        db.commit()
        db.close()


def sql_add_new_spiker(tg_id, start_date, duration=None, subject=None, delay=None):

    end_date = calculate_end_date(start_date, duration)

    with sqlite3.connect(BASE) as db:
        cur = db.cursor()
        query = f"""
        INSERT INTO 'speakers' (user_id, start_date, end_date, subject, delay)
        VALUES ('{tg_id}','{start_date}','{end_date}','{subject}','{delay}')
        """
        cur.execute(query)
        db.commit()
        db.close()


def sql_register_messages(guest, speaker, message):
    with sqlite3.connect(BASE) as db:
        cur = db.cursor()
        query = f"""
            INSERT INTO 'messages' (guest, speaker, message)
            VALUES ('{guest}', '{speaker}', '{message}')
            """
        cur.execute(query)
        db.commit()
        db.close()


def sql_get_user_data(tg_id) -> dict:
    with sqlite3.connect(BASE) as db:
        cur = db.cursor()
        query = f"SELECT * FROM 'users' WHERE tg_id is '{tg_id}'"
        cur.execute(query)
        cur.execute(query)
        result = cur.fetchone()
        db.close()

        formated_result = {
            'tg_id': result[0],
            'name': result[1],
            'phone': result[2]
            }
        return formated_result


def sql_put_user_phone(tg_id, phone):
    conn = sqlite3.connect(BASE)
    cur = conn.cursor()
    exec_text = f"UPDATE 'users' SET phone={phone} WHERE tg_id={tg_id}"
    cur.execute(exec_text)
    conn.commit()
    conn.close()


def calculate_end_date(start, duration):
    start_sep = start.split(':')
    duration_sep = duration.split(':')
    print(start_sep)
    print(duration_sep)
    print(start_sep[1])
    if int(start_sep[1]) + int(duration_sep[1]) <= 60:
        start_sep[0] = str(int(start_sep[0]) + int(duration_sep[0]))
        start_sep[1] = str(int(start_sep[1]) + int(duration_sep[1]))
    else:
        start_sep[0] = str(int(start_sep[0]) + int(duration_sep[0])+1)
        start_sep[1] = str(int(start_sep[1]) + int(duration_sep[1])-60)
    end_date = start_sep
    return end_date


print(calculate_end_date('13:45', '1:20'))
