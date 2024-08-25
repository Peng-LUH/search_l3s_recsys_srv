import os
import json, requests
from requests.exceptions import JSONDecodeError
import sys
import sys
from collections import Counter

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

sys.path.append('..')
from dotenv import load_dotenv
load_dotenv()

from swagger_client import l3s_gateway_client_v110
from swagger_client import sse_search_client

sse_search_config = sse_search_client.Configuration()

sse_search_config.host = os.getenv('MLS_SEARCH_HOST')
print("*"*80)
print("sse-search-service-host: ", sse_search_config.host)
print("*"*80)

l3s_gateway_config = l3s_gateway_client_v110.Configuration()

l3s_gateway_config.host = os.getenv('L3S_GATEWAY_HOST')
print("*"*80)
print("l3s-gateway-service-host: ", l3s_gateway_config.host)
print("*"*80)
 
client_sse_search = sse_search_client.ApiClient(configuration=sse_search_config)
sse_brufenet_api = sse_search_client.BerufeNetApi(api_client=client_sse_search)
sse_user_api = sse_search_client.UserApi(api_client=client_sse_search)
sse_skill_api = sse_search_client.SkillApi(api_client=client_sse_search)

sse_career_pro_api = sse_search_client.CareerProfileApi(api_client=client_sse_search)
sse_learning_pro_api=sse_search_client.LearningProfilesApi(api_client=client_sse_search)
sse_learning_history_pro_api = sse_search_client.LearningHistoryApi(api_client=client_sse_search)

client_l3s_gateway = l3s_gateway_client_v110.ApiClient(configuration=l3s_gateway_config)
gateway_searcher_api = l3s_gateway_client_v110.SearchServiceApi(api_client=client_l3s_gateway)



class LearningGoalsRec(object):
    def __init__(self) -> None:
        super().__init__()


    def get_learning_goals(self, id):

        response = requests.get(os.getenv("MLS_SEARCH_HOST")+"/career-profiles/{id}".format(id=id))
        career_profile = response.json()

        interest = career_profile["professionalInterests"]
        return interest    

    def recommend(self, k, user_id):
        learning_goals = self.get_learning_goals(user_id)
        result_list = []
        for goal,_ in learning_goals:   

            response = gateway_searcher_api.get_search_service(user_id, goal)

            #response = gateway_searcher_api.get_search_service(user_id="1", query=skill, entity_type="all", num_results=2)
            if len(response.results)!=0:
                for item in response.results:
                    entity_id_type = {}
                    entity_id_type["entity_type"] = item.entity_type
                    entity_id_type["entity_id"] = item.entity_id
                    if entity_id_type not in result_list:
                        result_list.append(entity_id_type)

        return result_list
 
