#!/bin/ python 

import psycopg2
from config import config

def get_vendors():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name')
        print('The number of parts: ', cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()
 
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_parts():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT part_id, part_name FROM parts ORDER BY part_name')
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


def get_parts_vendors():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(
        '''
        SELECT part_name, vendor_name
        FROM parts
        INNER JOIN vendor_parts ON vendor_parts.part_id = parts.part_id
        INNER JOIN vendors ON vendors.vendor_id = vendor_parts.vendor_id
        ORDER BY part_name;      
        '''
        )
        for row in iter_row(cur, 10):
            print(row)
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    #get_vendors()
    #get_parts()
    get_parts_vendors()
