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

sse_search_config.host = os.getenv('SSE_SEARCH_HOST')
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



client_l3s_gateway = l3s_gateway_client_v110.ApiClient(configuration=l3s_gateway_config)
gateway_searcher_api = l3s_gateway_client_v110.SearchServiceApi(api_client=client_l3s_gateway)



class TrendSkillsBfn(object):
    def __init__(self) -> None:
        super().__init__()


    def job_by_query(self, query):
        response = sse_brufenet_api.berufe_net_controller_get_jobs_by_search_string(query)
        assert len(response)>0, "No jobs found."
        job_ids = []
        for job in response:
            job_ids.append(job["id"])

        return job_ids

    def trending_skills(self, query, k):
        job_list = self.job_by_query(query)
        skills = {}
        for job_id in job_list:
            response = sse_brufenet_api.berufe_net_controller_get_digital_competencies_by_job_id(job_id)
            for comp in response:
                if not comp['textContent'] in skills:
                    skills[comp['textContent']]=1
                else:
                    skills[comp['textContent']]+=1    


        top_skills = Counter(skills).most_common(k)

        return top_skills    

    def recommend(self, query, k):
        top_k_trending_skills = self.trending_skills(query, k)
        result_list = []
        for skill,_ in top_k_trending_skills:   

            response = gateway_searcher_api.get_search_service("1", skill)

            #response = gateway_searcher_api.get_search_service(user_id="1", query=skill, entity_type="all", num_results=2)
            if len(response.results)!=0:
                for item in response.results:
                    entity_id_type = {}
                    entity_id_type["entity_type"] = item.entity_type
                    entity_id_type["entity_id"] = item.entity_id
                    if entity_id_type not in result_list:
                        result_list.append(entity_id_type)

        return result_list
 


# trendskills = TrendSkillsBfn()

# top_skills = trendskills.recommend("bahn", 5)

# print(top_skills)

