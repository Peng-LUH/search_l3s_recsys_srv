# search_l3s_recysy


## This is the repository of recommendation system for MLS platform.

### :file_folder: File Structure

```
├── search_l3s_recsys/
│    ├── api/
│       ├── digitalisation_topics/
│       ├── interests/
│       ├── learning_goals/
│       ├── random/
│       ├── trends/
├── swagger_client/
│       ├── json_file/
│       ├── l3s_gateway_client_v110/
│       ├── sse_search_client/
├── Dockerfile
├── requirements.txt
├── run.py
└── README.md
```

## Swagger Clients
The recommendation service is dependent on the l3s-gateway service (mainly the search) and sse user service.

Currently, it has l3s-gateway client with version 1.1.0 

## Api endpoints structure
Each api endpoint has mainly 3 files. 
```
├── endpoint_name/
│    ├── dto.py  (for the expected input and response)
│    ├── endpoints.py (for defining the endpoint path, process input and output)
│    ├── logic.py  (main logic file behind the api endpoint)
```


