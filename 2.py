import psycopg2, psswd as psswd
from datetime import timedelta


conn = psycopg2.connect(
    host='localhost',
    database='test',
    user='arelyxl',
    password=psswd.PASSWORD,
    port=5432   
)

cur = conn.cursor()

cur.execute('''
            SELECT pid, ROUND(EXTRACT(EPOCH FROM (now() - backend_start))/60) as duration 
            FROM pg_stat_activity 
            WHERE datid notnull AND ROUND(EXTRACT(EPOCH FROM (now() - backend_start))/60) > 1;
            ''')
print('# SE EJECUTO EL COMANDO SQL')
with open("LOG/pids.txt", 'w') as f:
    for pid, duration in cur.fetchall():
        f.write(f'{pid}\n')
        print(f'PID: {pid}, Duracion: {duration} minutos')
cur.close()
conn.close()

