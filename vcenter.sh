#!/bin/bash

curl -X POST http://videocenter2.schule.de/storeAndRouteSQLQuery.php \
	-u leit:tiel \
	-H "Content-Type: application/x-www-form-urlencoded" \
       	-H "Referer: http://videocenter.schule.de/abfrageformular.php?domain=Geschaeftsfuehrung" \
	-H "Authorization: Basic bGVpdDp0aWVs" \
	-d $1
