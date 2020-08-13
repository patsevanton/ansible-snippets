# замена IP сервера
В файле inventory сначала вам сделать список IP или доменные имена серверов откуда вам нужен доступ.
В файле conn_vars.yaml вам нужно указать список сервер:порт, к которому нужен доступ с серверов из inventory.

# запуск ansible-playbook
## Если у вас есть доступ только по доменной учетке:
```bash
ansible-playbook -b -k -e ansible_ssh_user='ваша учетка в Acitve Directory' connect.yaml
```
## Если у вас есть доступ по ключу:
```bash
ansible-playbook -b connect.yaml
```
## Если имя учётки не совпадает с именем пользователя от которого запускаете playbook
```bash
ansible-playbook -b -e ansible_ssh_user='имя учётки' connect.yaml
```
