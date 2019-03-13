#!/bin/python

import psycopg2
from config import config

def delete_part(part_id):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('DELETE FROM parts WHERE part_id =  %s', (part_id,))
        rows_deleted = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted

if __name__ == '__main__':
    deleted_rows = delete_part(2)
    print('the number os deleted rows: ', deleted_rows)
