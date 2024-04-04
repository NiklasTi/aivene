import requests
from requests.models import Response
from typing import Optional


class Aivene():
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        # self.base_request_url = "https://api.fundus.live"
        self.base_request_url = "https://aivene-main-72f6e2d.d2.zuplo.dev"
        # self.base_request_url = 'http://localhost:8000'
    
    def generate_queries(
        self,
        user_input: str,
        n_queries: Optional[int] = 1,
    ) -> Response:
        
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
            # 'Api-Key': self.api_key,
        }

        # Make the POST request
        response = requests.post(request_url, json=params, headers=headers)
        
        if 200 <= response.status_code < 300:
            return response
        elif response.status_code >= 400:
            # Extract the detailed error message from response
            error_detail = response.json().get('detail', 'An unexpected error occurred. Please try again or contact Aivene support.')
            error_message = f"HTTP error {response.status_code}: {error_detail}"
            print(response.json())
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
            # 'Api-Key': self.api_key,
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