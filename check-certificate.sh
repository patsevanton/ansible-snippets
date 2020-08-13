#!/bin/bash

declare -a arr=("account.tools.mycompany.ru" "cert.tools.mycompany.ru" "chat.tools.mycompany.ru" "confluence-backup.tools.mycompany.ru" "confluence.tools.mycompany.ru" "grafana.tools.mycompany.ru" "grid.tools.mycompany.ru" "inventory.tools.mycompany.ru" "jitsi.tools.mycompany.ru" "kibana.tools.mycompany.ru" "racktables.tools.mycompany.ru" "rancher.tools.mycompany.ru" "selenoid.tools.mycompany.ru" "sonar.tools.mycompany.ru" "teamcity.tools.mycompany.ru" "testrail.tools.mycompany.ru" "upsource.tools.mycompany.ru" "youtrack.tools.mycompany.ru" "zabbix.tools.mycompany.ru")

for i in "${arr[@]}"
do
   echo "$i"
   echo | openssl s_client -servername "$i" -connect "$i":443 2>/dev/null | openssl x509 -noout -issuer
done


