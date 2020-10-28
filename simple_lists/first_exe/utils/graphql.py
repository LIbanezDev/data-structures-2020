import requests


def request_graph(query, entityName):
    query = {
        "operationName": "GET_DATA",
        "query": "query GET_DATA { " + query + " }"
    }
    res = requests.post('http://localhost:3000/api/graphql', json=query)
    return res.json()["data"][entityName]
