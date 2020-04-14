import psycopg2


def connect(host):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = {'user': 'postgres',
                  'password': 'postgres',
                  'database': 'postgres',
                  'host': host,
                  'port': 5432}

        # connect to the PostgreSQL server
        print('\n')
        print('=========================================')
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        print('=========================================')
        print('\n')
        return conn

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        exit(1)
