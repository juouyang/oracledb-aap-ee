import cx_Oracle
import os

oracle_ip =os.environ['ORACLE_IP']
oracle_pwd = os.environ['ORACLE_PWD']
oracle_sid = os.environ['ORACLE_SID']

dsn_tns = cx_Oracle.makedsn(f'{oracle_ip}', '1521', service_name=f'{oracle_sid}')
conn = cx_Oracle.connect(user=r'sys', password=f'{oracle_pwd}', mode=cx_Oracle.SYSDBA, dsn=dsn_tns)

c = conn.cursor()
c.execute('SELECT INSTANCE_NAME, STATUS, DATABASE_STATUS FROM V$INSTANCE')
for row in c:
    print (row)
conn.close()