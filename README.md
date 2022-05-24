## Build

```
ansible-builder build --tag juouyang/sqlplus-ee:0.0.1 --container-runtime docker
```

## Unit Test

test.sql
```
select
   vsql.sql_id,
   vsql.sql_text
from
   v$sql      vsql,
   v$session  sess
where
   vsql.sql_id = sess.sql_id;

quit;
/
```


```
export ORACLE_IP=10.1.1.126
export ORACLE_PWD=53916262
export ORACLE_SID=ORCLCDB

docker run --rm -it \
    -v $(pwd)/test.sql:/test.sql \
    juouyang/sqlplus-ee:0.0.1 \
    sqlplus sys/${ORACLE_PWD}@//${ORACLE_IP}:1521/${ORACLE_SID} as sysdba @/test.sql
```