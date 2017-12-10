import requests

POST_ADD_USER_URL = "http://videocenter.schule.de/adduser.php?domain=Anmeldung&used_table=kunden"


def addUser(lname, fname, street, postalCode, place, tel, born, sex, note):
    user = {''}
    response = requests.post(POST_ADD_USER_URL, data=user)


