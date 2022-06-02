## Preparations

* container runtime: docker or podman
* python packages:
    ```
    pip install ansible-builder
    pip install ansible-runner # to verify container image of ee
    ```

Run Oracle Database 19.3.0 using Container
```
export VOLUME_ROOT=/Users/ju/oracle-db/oradata    # persistent data

docker run -d \
  --name oracle-db \
  -p 1521:1521 \
  -p 5500:5500 \
  -e ORACLE_SID=ORCLCDB \
  -e ORACLE_PWD=53916262 \
  -v ${VOLUME_ROOT}:/opt/oracle/oradata \
  juouyang/oracle-db:19.3.0-se2
```

## Build

docker
```
ansible-builder build --tag juouyang/oracle-ee:0.0.3 --container-runtime docker -v 3
```

## Unit Test

```
export ORACLE_IP=192.168.23.102
export ORACLE_PWD=53916262
export ORACLE_SID=ORCLCDB
```

sqlplus
```
docker run --rm -it \
    -v $(pwd)/test/test.sql:/test.sql \
    juouyang/oracle-ee:0.0.3 \
    sqlplus sys/${ORACLE_PWD}@//${ORACLE_IP}:1521/${ORACLE_SID} as sysdba @/test.sql
```

oratop
```
docker run --rm -it \
    -v $(pwd)/test/test.exp:/test.exp \
    -e REMOTE_LOGIN_PASSWORDFILE=EXCLUSIVE \
    -e ORACLE_IP=${ORACLE_IP} \
    -e ORACLE_PWD=${ORACLE_PWD} \
    -e ORACLE_SID=${ORACLE_SID} \
    juouyang/oracle-ee:0.0.3 \
    /test.exp
```

python
```
docker run --rm -it \
    -v $(pwd)/test/test.py:/test.py \
    -e ORACLE_IP=${ORACLE_IP} \
    -e ORACLE_PWD=${ORACLE_PWD} \
    -e ORACLE_SID=${ORACLE_SID} \
    juouyang/oracle-ee:0.0.3 \
    python3 /test.py
```

playbook
```
# edit test/env/extravars

docker run --rm -it \
    -v $(pwd)/test/project/test.yaml:/runner/project/test.yaml \
    -v $(pwd)/test/env/extravars:/runner/env/extravars \
    -e RUNNER_PLAYBOOK=test.yaml \
    juouyang/oracle-ee:0.0.3
```

ansible-runner

```
# edit test/env/extravars

ansible-runner run \
    --process-isolation test \
    --process-isolation-executable docker \
    --container-image juouyang/oracle-ee:0.0.3 \
    --playbook test.yaml \
    --debug
```
