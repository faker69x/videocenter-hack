#!/bin/bash

curl -X POST http://130.73.201.41/storeAndRouteSQLQuery.php \
	-u leit:tiel -L \
	-H "Content-Type: application/x-www-form-urlencoded" \
       	-H "Referer: http://videocenter.schule.de/abfrageformular.php?domain=Geschaeftsfuehrung" \
	-H "Authorization: Basic bGVpdDp0aWVs" \
	-d $1
