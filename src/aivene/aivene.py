import requests
from requests.models import Response
from typing import Optional


class Aivene():
    def __init__(self, api_key: str) -> None:
        """
        Initializes a new instance of the `Aivene` class.

        Args:
            api_key (str): The API key used for authentication.

        Returns:
            None

        This constructor initializes the `api_key` attribute with the provided `api_key` parameter. It also sets the `base_request_url` attribute to the value "https://aivene-main-72f6e2d.d2.zuplo.dev".

        """
        self.api_key = api_key
        self.base_request_url = "https://aivene-main-72f6e2d.d2.zuplo.dev"
    
    def generate_queries(
        self,
        user_input: str,
        n_queries: Optional[int] = 1,
    ) -> Response:
        """
        Generates queries based on the given user input.

        Args:
            user_input (str): The input from the user.
            n_queries (Optional[int], optional): The number of queries to generate. Defaults to 1.

        Returns:
            Response: The response from the API containing the generated queries.

        Raises:
            Exception: If the response status code is >= 400 or if no response is received from the server.

        This function sends a POST request to the Aivene API's generate_queries endpoint with the provided user input and number of queries. It removes any keys with None values from the params dictionary. The request is made with the provided API key in the authorization header. If the response status code is between 200 and 299 (inclusive), the response is returned. If the status code is >= 400, an exception is raised with the corresponding error message. If no response is received from the server, an exception is raised with the message "No response received from the server".
        """
        
        params = {
            'user_content': user_input,
            'n_queries': n_queries,
        }

        # Remove keys with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Request setup
        request_url = f"{self.base_request_url}/generate_queries"
        headers = {
            'authorization': f"Bearer {self.api_key}",
        }

        # Make the POST request
        response = requests.post(request_url, json=params, headers=headers)
        
        if 200 <= response.status_code < 300:
            return response
        elif response.status_code >= 400:
            # Extract the detailed error message from response
            error_detail = response.json().get('detail', 'An unexpected error occurred. Please try again or contact Aivene support.')
            error_message = f"HTTP error {response.status_code}: {error_detail}"
            raise Exception(error_message)
        else:
            # Handle the case where response is None
            raise Exception("No response received from the server")
    
    def search(
        self,
        keyword: str,
        url: Optional[str] = None,
        depth: Optional[int] = 50,
        max_crawl_pages: Optional[int] = 1,
        location_name: Optional[str] = None,
        location_code: Optional[int] = 2840,
        location_coordinate: Optional[str] = None,
        language_name: Optional[str] = 'English',
        language_code: Optional[str] = 'en',
        se_domain: Optional[str] = None,
        device: Optional[str] = 'desktop',
        os: Optional[str] = 'windows',
        raw_response: Optional[bool] = False
    ) -> Response:
        """
        Sends a POST request to the Aivene API's search endpoint with the provided keyword and optional parameters.

        Args:
            keyword (str): The keyword to search for.
            url (Optional[str], optional): The URL to search within. Defaults to None.
            depth (Optional[int], optional): The depth of the search. Defaults to 50.
            max_crawl_pages (Optional[int], optional): The maximum number of pages to crawl. Defaults to 1.
            location_name (Optional[str], optional): The name of the location. Defaults to None.
            location_code (Optional[int], optional): The code of the location. Defaults to 2840.
            location_coordinate (Optional[str], optional): The coordinate of the location. Defaults to None.
            language_name (Optional[str], optional): The name of the language. Defaults to 'English'.
            language_code (Optional[str], optional): The code of the language. Defaults to 'en'.
            se_domain (Optional[str], optional): The search engine domain. Defaults to None.
            device (Optional[str], optional): The device type. Defaults to 'desktop'.
            os (Optional[str], optional): The operating system. Defaults to 'windows'.
            raw_response (Optional[bool], optional): Whether to return the raw response. Defaults to False.

        Returns:
            Response: The response from the API containing the search results.

        Raises:
            Exception: If the response status code is >= 400 or if no response is received from the server.

        This function sends a POST request to the Aivene API's search endpoint with the provided keyword and optional parameters. It removes any keys with None values from the params dictionary. The request is made with the provided API key in the authorization header. If the response status code is between 200 and 299 (inclusive), the response is returned. If the status code is >= 400, an exception is raised with the corresponding error message. If no response is received from the server, an exception is raised with the message "No response received from the server".
        """
        
        params = {
            'keyword': keyword,
            'url': url,
            'depth': depth,
            'max_crawl_pages': max_crawl_pages,
            'location_name': location_name,
            'location_code': location_code,
            'location_coordinate': location_coordinate,
            'language_name': language_name,
            'language_code': language_code,
            'se_domain': se_domain,
            'device': device,
            'os': os,
            'raw_response': raw_response
        }

        # Remove keys with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Request setup
        request_url = f"{self.base_request_url}/search"
        headers = {
            'authorization': f"Bearer {self.api_key}",
        }

        # Make the POST request
        response = requests.post(request_url, json=params, headers=headers)
        
        if 200 <= response.status_code < 300:
            return response
        elif response.status_code >= 400:
            # Extract the detailed error message from response
            error_detail = response.json().get('detail', 'An unexpected error occurred. Please try again or contact Aivene support.')
            error_message = f"HTTP error {response.status_code}: {error_detail}"
            raise Exception(error_message)
        else:
            # Handle the case where response is None
            raise Exception("No response received from the server")
    
    def search_queries(
        self,
        user_input: str,
        n_queries: Optional[int] = 1,
        url: Optional[str] = None,
        depth: Optional[int] = 50,
        max_crawl_pages: Optional[int] = 1,
        location_name: Optional[str] = None,
        location_code: Optional[int] = 2840,
        location_coordinate: Optional[str] = None,
        language_name: Optional[str] = 'English',
        language_code: Optional[str] = 'en',
        se_domain: Optional[str] = None,
        device: Optional[str] = 'desktop',
        os: Optional[str] = 'windows',
        raw_response: Optional[bool] = False
    ) -> Response:
        """
        Searches for queries based on the given user input.

        Args:
            user_input (str): The input from the user.
            n_queries (Optional[int], optional): The number of queries to search for. Defaults to 1.
            url (Optional[str], optional): The URL to search within. Defaults to None.
            depth (Optional[int], optional): The depth of the search. Defaults to 50.
            max_crawl_pages (Optional[int], optional): The maximum number of pages to crawl. Defaults to 1.
            location_name (Optional[str], optional): The name of the location. Defaults to None.
            location_code (Optional[int], optional): The code of the location. Defaults to 2840.
            location_coordinate (Optional[str], optional): The coordinate of the location. Defaults to None.
            language_name (Optional[str], optional): The name of the language. Defaults to 'English'.
            language_code (Optional[str], optional): The code of the language. Defaults to 'en'.
            se_domain (Optional[str], optional): The search engine domain. Defaults to None.
            device (Optional[str], optional): The device type. Defaults to 'desktop'.
            os (Optional[str], optional): The operating system. Defaults to 'windows'.
            raw_response (Optional[bool], optional): Whether to return the raw response. Defaults to False.

        Returns:
            Response: The response from the API containing the search results.

        Raises:
            Exception: If the response status code is >= 400 or if no response is received from the server.

        This function sends a POST request to the Aivene API's search_queries endpoint with the provided user input and optional parameters. It removes any keys with None values from the params dictionary. The request is made with the provided API key in the authorization header. If the response status code is between 200 and 299 (inclusive), the response is returned. If the status code is >= 400, an exception is raised with the corresponding error message. If no response is received from the server, an exception is raised with the message "No response received from the server".
        """
        
        params = {
            'user_content': user_input,
            'n_queries': n_queries,
            'url': url,
            'depth': depth,
            'max_crawl_pages': max_crawl_pages,
            'location_name': location_name,
            'location_code': location_code,
            'location_coordinate': location_coordinate,
            'language_name': language_name,
            'language_code': language_code,
            'se_domain': se_domain,
            'device': device,
            'os': os,
            'raw_response': raw_response
        }

        # Remove keys with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Request setup
        request_url = f"{self.base_request_url}/search_queries"
        headers = {
            'authorization': f"Bearer {self.api_key}",
        }

        # Make the POST request
        response = requests.post(request_url, json=params, headers=headers)
        
        if 200 <= response.status_code < 300:
            return response
        elif response.status_code >= 400:
            # Extract the detailed error message from response
            error_detail = response.json().get('detail', 'An unexpected error occurred. Please try again or contact Aivene support.')
            error_message = f"HTTP error {response.status_code}: {error_detail}"
            raise Exception(error_message)
        else:
            # Handle the case where response is None
            raise Exception("No response received from the server")