import requests

def get_request(url,headers,query_list):
	
	querystring ={"league":str(query_list[0]), "season":str(query_list[1]), "page":str(query_list[2])}
	# 2. Generate GET request and pass data onto response variable
	response = requests.request("GET", url, headers=headers, params=querystring)

	# 3 retrieve response data and parse
	responsedata = response.json()
	return responsedata
