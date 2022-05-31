## Build

podman
```
ansible-builder build --tag juouyang/sqlplus-ee:0.0.2

```
docker
```
ansible-builder build --tag juouyang/sqlplus-ee:0.0.2 --container-runtime docker
```

## Unit Test

```
export ORACLE_IP=10.1.1.126
export ORACLE_PWD=53916262
export ORACLE_SID=ORCLCDB

podman run --rm -it \
    -v $(pwd)/test/test.sql:/test.sql \
    juouyang/sqlplus-ee:0.0.2 \
    sqlplus sys/${ORACLE_PWD}@//${ORACLE_IP}:1521/${ORACLE_SID} as sysdba @/test.sql
```

```
podman run --rm -it \
    -v $(pwd)/test/test.py:/test.py \
    -e ORACLE_IP=10.1.1.126 \
    -e ORACLE_PWD=53916262 \
    -e ORACLE_SID=ORCLCDB \
    juouyang/sqlplus-ee:0.0.2 \
    python3 /test.py
```

```
podman run --rm -it \
    -v $(pwd)/test/project/test.yaml:/runner/project/test.yaml \
    -e ORACLE_IP=10.1.1.126 \
    -e ORACLE_PWD=53916262 \
    -e ORACLE_SID=ORCLCDB \
    -e RUNNER_PLAYBOOK=test.yaml \
    juouyang/sqlplus-ee:0.0.2
```
