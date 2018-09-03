import requests
import json

access_token="EAAFbgC771Y0BAMHjzjQhnfScgu8eVDTlAO5TINnVDlunYLjhZCMDh3LPRP9ltEKMy4KWeWacDtxxI0vOS8MTiJhIe4rMI6KzZBBaF2PIDgEhDUo60ADkRwkO4FP7UlACHySJVx9NPx4Sh6RuKg89QeyhZCoHwZBGuK4aIky7BgZDZD"
def get_pg_data(page_id):
	url = 'https://graph.facebook.com/'+str(page_id)+'/feed?limit=100&access_token'+access_token
	data=requests.get(url)
	response=data.text
	print response

get_pg_data('382081078908301')