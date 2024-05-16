import os
import json, requests
from requests.exceptions import JSONDecodeError
import sys
import unicodedata
import base64
import base64
import sys
from pathlib import Path
from flask import abort

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

sys.path.append('..')


from search_l3s_recsys.swagger_client import l3s_gateway_client
# from swagger_client import l3s_gateway_client
l3s_gateway_config = l3s_gateway_client.Configuration()

 
client_l3s_gateway = l3s_gateway_client.ApiClient(configuration=l3s_gateway_config)
gateway_searcher_api = l3s_gateway_client.SearchServiceApi(api_client=client_l3s_gateway)

sys.path.append(os.getcwd())


from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv("OPENAI_API_KEY")
API_ENDPOINT = os.getenv("API_ENDPOINT")
l3s_gateway_config.host = os.getenv('L3S_GATEWAY_HOST')

                   
assert os.getenv("L3S_GATEWAY_HOST") is not None, abort(501, "Environment variable 'L3S_GATEWAY_HOST' is not defined. Please update/add env variable.")


class Trends(object):

    def __init__(self) -> None:
        super().__init__()

    def get_jwt(self):
        """fetch the jwt token object"""
        headers = {
            'User-Agent': 'Jobsuche/2.9.2 (de.arbeitsagentur.jobboerse; build:1077; iOS 15.1.0) Alamofire/5.4.4',
            'Host': 'rest.arbeitsagentur.de',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        }

        data = {
        'client_id': 'c003a37f-024f-462a-b36d-b001be4cd24a',
        'client_secret': '32a39620-32b3-4307-9aa1-511e3d7f48a8',
        'grant_type': 'client_credentials'
        }

        response = requests.post('https://rest.arbeitsagentur.de/oauth/gettoken_cc', headers=headers, data=data, verify=False)

        return response.json()    
    
    def search(self, jwt, what, where, radius):
        """search for jobs. params can be found here: https://jobsuche.api.bund.dev/"""
        params = (
            ('angebotsart', '1'),
            ('page', '1'),
            ('pav', 'false'),
            ('size', '100'),
            ('umkreis', radius),
            ('was', what),
            ('wo', where),
        )

        headers = {
            'User-Agent': 'Jobsuche/2.9.2 (de.arbeitsagentur.jobboerse; build:1077; iOS 15.1.0) Alamofire/5.4.4',
            'Host': 'rest.arbeitsagentur.de',
            'Authorization': f'Bearer {jwt}',
            'Connection': 'keep-alive',
            "Content-Type": "application/json"
        }

        response = requests.get('https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/app/jobs',
                                headers=headers, params=params, verify=False)
        
        
        return response.json()
    
    def job_details(self,jwt, job_ref):

        headers = {
            'User-Agent': 'Jobsuche/2.9.3 (de.arbeitsagentur.jobboerse; build:1078; iOS 15.1.0) Alamofire/5.4.4',
            'Host': 'rest.arbeitsagentur.de',
            'OAuthAccessToken': jwt,
            'Connection': 'keep-alive',
        }

        response = requests.get(
            f'https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v2/jobdetails/{(base64.b64encode(job_ref.encode())).decode("UTF-8")}',
            headers=headers, verify=False)

        return response.json()
    
    def formal_skills(self, jwt, offers):
        skills = {}
        for offer in offers:
            details = self.job_details(jwt, offer["refnr"])
            if "fertigkeiten" in details:
                skills[offer["refnr"]] = {"job_title" : details["beruf"], "skills" : details["fertigkeiten"]}
        return skills

    def create_formal_skill_histogram(self, skills_compilation):
        """ key_format := <skill_name>|<skill_level>|<context>   

            value_format := <number_of_occurencies>"""
        histogram = {}
        for k, v in skills_compilation.items():
            for skills_container in v["skills"]:
                context = skills_container["hierarchieName"]
                skill_sets = skills_container["auspraegungen"]
                for level, skills in skill_sets.items():
                    for skill in skills:
                        entry = skill #+"|"+level+"|"+context
                        if entry in histogram:
                            histogram[entry] += 1
                        else:
                            histogram[entry] = 1
        return histogram
    


    def recommend(self, top_k_trending_skills):
        result_list = []
        for skill in top_k_trending_skills:     
            response = gateway_searcher_api.get_search_service(owner= "1", user_id="1", query=skill, entity_type="all", num_results=2)
            if len(response.results)!=0:
                for item in response.results:
                    entity_id_type = {}
                    entity_id_type["entity_type"] = item.entity_type
                    entity_id_type["entity_id"] = item.entity_id
                    if entity_id_type not in result_list:
                        result_list.append(entity_id_type)

        return result_list







