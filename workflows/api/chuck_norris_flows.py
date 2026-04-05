import allure
from data.api.chuck_norris_data import *
from extensions.api_actions import APIActions
from playwright.sync_api import APIRequestContext,APIResponse


class ChuckNorrisFlows:
    def __init__(self, request_context:APIRequestContext):
        self.api = APIActions(request_context)


    @allure.step("Flow: Fetching a random joke")
    def get_random_joke(self):
        # Using the address from the Page Object inside the API method
        return self.api.get(RANDOM_PATH)


    @allure.step("Flow: Searching jokes with query: {query}")
    def search_joke(self, query: str):
        params = {"query": query}
        return self.api.get(SEARCH_PATH, params=params)
    
    @allure.step("rodaom jokes:")
    def get_random_joke(self):
        return self.api.get("/jokes/random")
    

    @allure.step("search query jokes")
    def search_joke(self, query):
        params = {"query": query}
        return self.api.get("/jokes/search", params=params)
    

    @allure.step("get categories of jokes:")
    def get_categories(self):
        return self.api.get(CATEGORIES_PATH)
    


    #test 11
    @allure.step("Flow: Attempting to create a joke (Negative Test)")
    def try_to_create_joke(self, joke_text: str):
         # Try sending without the payload, only the POST method to a GET endpoint
        # This will usually return an error status response that the logger can handle
        return self.api.post("/jokes/random", {joke_text})
    