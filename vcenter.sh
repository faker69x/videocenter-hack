#!/bin/bash

curl -X POST http://130.73.201.41/storeAndRouteSQLQuery.php \
	-u leit:tiel -L \
	-H "Content-Type: application/x-www-form-urlencoded" \
       	-H "Referer: http://videocenter.schule.de/abfrageformular.php?domain=Geschaeftsfuehrung" \
	-H "Cookie: Video001=0%2C0%2C0%2C1%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0; Video001-selected=15; PHPSESSID=lhms5884h0qiqojrmb4acm3qshbaccg0" \
	-H "Authorization: Basic bGVpdDp0aWVs" \
	-d "sql_abfrage=SELECT+*+FROM+kunden%2C+videos%2C+ausleihe+WHERE+ausleihe.kunr+LIKE+%27%251%25%27+GROUP+BY+kunden.kustras++ORDER+BY+kunden.kuort&domain=Geschaeftsfuehrung&num=0&limit=10000&submit=Query+abschicken%21"
