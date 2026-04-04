
from datetime import date
import pytest
import allure
import time
import json
from extensions.api_verifications import APIVerify
from data.api.chuck_norris_data import *
from workflows.api.chuck_norris_flows import ChuckNorrisFlows

@allure.epic("API Tests")
@allure.feature("Chuck Norris Jokes")
class TestChuckNorrisAPI:

    @allure.description("1. Verify random joke returns 200 OK")
    def test01_get_random_joke_status(self, chuck_norris_flows:ChuckNorrisFlows):
        response =chuck_norris_flows.get_random_joke()
        APIVerify.status_code(response, STATUS_CODE_OK)


    @allure.description("2. Verify joke JSON contains 'value' key")
    def test02_joke_has_content(self, chuck_norris_flows:ChuckNorrisFlows):
        response =chuck_norris_flows.get_random_joke()
        APIVerify.json_key_exists(response.json(), JOKE_VALUE)



    @allure.description("test03. Data Driven Search: Verify results for multiple queries")
    @pytest.mark.parametrize("query, should_have_results", SEARCH_QUERIES) # כאן הטסט נהיה עוצמתי
    def test03_search_jokes_dynamic(self, chuck_norris_flows:ChuckNorrisFlows, query,should_have_results):
        response = chuck_norris_flows.search_joke(query)
        data = response.json()
        print("\nFormatted Response:")
        print(json.dumps(data, indent=2))
        APIVerify.verify_search_results(data,query,should_have_results)

        

    @allure.description(" test04:Verify categories list matches expected data")
    def test04_categories_list_valid(self, chuck_norris_flows:ChuckNorrisFlows):
        response =chuck_norris_flows.get_categories()
        data = response.json()
        print("\n formzated response")
        print(json.dumps(data, indent=2))
        APIVerify.list_contains_all(response.json(), EXPECTED_CATEGORIES)



    @allure.description("test05. Verify response headers content-type is JSON")
    def test05_api_header_type(self,chuck_norris_flows:ChuckNorrisFlows):
        response = chuck_norris_flows.get_random_joke()
        data = response.json()
        print("\n formated response")
        print(json.dumps(data , indent =2))
        APIVerify.string_contains(response.headers["content-type"], "application/json")



    @allure.description("test06. Verify joke ID is a string (Data Type check)")
    def test06_joke_id_type(self, chuck_norris_flows:ChuckNorrisFlows):
        response =chuck_norris_flows.get_random_joke()
        data  = response.json()
        print("\n")
        print(json.dumps(data , indent=2))
        APIVerify.instance_of(response.json()["id"], str)



    @allure.description("test07. Verify icon_url starts with HTTPS")
    def test07_icon_url_secure(self, chuck_norris_flows:ChuckNorrisFlows):
        response = chuck_norris_flows.get_random_joke()
        data = response.json()
        print("\n formated response:")
        print(json.dumps(data,indent =2))
        APIVerify.string_contains(response.json()["icon_url"], "https")


    @allure.description("test08. Verify specific category 'dev' returns correct category")
    def test08_category_consistency(self, chuck_norris_flows:ChuckNorrisFlows):
        response = chuck_norris_flows.get_categories()
        APIVerify.status_code(response, STATUS_CODE_OK)
        APIVerify.verify_equals(response.json(), ALL_CATEGORIES)

       
    @allure.description("test09. Performance SLA(Service Level Agreement): Response time less than 1 second")
    def test09_api_performance_sla(self, chuck_norris_flows:ChuckNorrisFlows):
        start_time = time.time()#time before send request
        chuck_norris_flows.get_random_joke()
        duration = time.time() - start_time 
        APIVerify.is_less_than(duration, 1.0)


    @allure.description("10. Verify URL in response matches base URL domain")
    def test10_url_domain_validation(self, chuck_norris_flows:ChuckNorrisFlows):
        response = chuck_norris_flows.get_random_joke()
        url_value = response.json()["url"]
        data = response.json()
        print("\n reformated")
        print(json.dumps(data , indent =2))
        
        # שימוש במתודה string_contains שכבר הוספנו קודם
        APIVerify.string_contains(url_value, "api.chucknorris.io/jokes/")

        
    @allure.description("11. Negative Test: Verify POST is not allowed")
    def test11_post_not_allowed(self, chuck_norris_flows:ChuckNorrisFlows):
        joke_text = "Chuck Norris can divide by zero."
        
        # 1. ניסיון לבצע POST
        response = chuck_norris_flows.try_to_create_joke(joke_text)
        APIVerify.status_code(response, 405)
     