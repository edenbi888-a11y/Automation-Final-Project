import json
from typing import Optional
import allure
from playwright.sync_api import APIRequestContext

class APIActions:
    def __init__(self, request_context: APIRequestContext):
        """
        Initialize APIActions with a Playwright APIRequestContext.
        """
        self.request_context = request_context


    @allure.step("Send GET request to {url}")
    def get(self, url: str, params: Optional[dict] = None, headers: Optional[dict] = None):
        """
        Send a GET request to the specified URL with optional parameters and headers.
        """
        response = self.request_context.get(url, params=params, headers=headers)
        self._log_response(response)  # Log the response
        return response
    

    @allure.step("Send POST request to {url}")
    def post(self, url: str, payload: dict, headers: Optional[dict] = None):
        """
        Send a POST request to the specified URL with a JSON payload and optional headers.
        """
        response = self.request_context.post(url,
                                             data=json.dumps(payload),
                                             headers=headers or {"Content-Type": "application/json"}
                                             )
        self._log_response(response)  # Log the response
        return response


    @allure.step("Send PUT request to {url}")
    def put(self, url: str, payload: dict, headers: Optional[dict] = None):
        """
        Send a PUT request to the specified URL with a JSON payload and optional headers.
        """
        response = self.request_context.put(url,
                                            data=json.dumps(payload),
                                            headers=headers or {"Content-Type": "application/json"}
                                            )
        self._log_response(response)  # Log the response
        return response
    

    @allure.step("Send DELETE request to {url}")
    def delete(self, url: str, headers: Optional[dict] = None):
        """
        Send a DELETE request to the specified URL with optional headers.
        """
        response = self.request_context.delete(url, headers=headers)
        self._log_response(response)  # Log the response
        return response


    # def _log_response(self, response):
    #     """
    #     Log response details to Allure report.
    #     """
    #     allure.attach(
    #         json.dumps(response.json(), indent=4),
    #         name=f"API Response - {response.status}",
    #         attachment_type=allure.attachment_type.JSON
    #     )
    #     assert response.ok, f"API request failed with status {response.status} - {response.text()}"
    def _log_response(self, response):
        """
        Safe logging for Allure + console (no crash on non-JSON)
        """
        try:
            body = response.json()
            formatted_body = json.dumps(body, indent=4)
            attachment_type = allure.attachment_type.JSON
        except Exception:
            body = response.text()
            formatted_body = body
            attachment_type = allure.attachment_type.TEXT

        # Allure attachment
        allure.attach(
            formatted_body,
            name=f"Response {response.status}",
            attachment_type=attachment_type
        )

        # Console log
        print(f"Status Code: {response.status}")
        print(f"Response Body: {body}")