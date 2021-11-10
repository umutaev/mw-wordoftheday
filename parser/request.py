import logging

import requests
from requests.models import HTTPError


module_logger = logging.getLogger("parser.request")


class Request:
    def __init__(self, **kwargs) -> None:
        self.logger = logging.getLogger("parser.request.Request")
        self.__timeout = kwargs.get("timeout", 5)
        self.__url = kwargs.get(
            "url", "https://www.merriam-webster.com/word-of-the-day")

    def check_connection(self) -> bool:
        r = requests.head(self.__url, timeout=self.__timeout)
        return r == 200

    def request_page(self) -> str:
        try:
            r = requests.get(self.__url, timeout=self.__timeout)
        except requests.exceptions.ConnectionError as e:
            self.logger.critical(
                f"Connection error while requesting {self.__url}")
            raise e
        self.logger.info(
            f"Page {self.__url} requested. Response {r.status_code}.")
        if not r.status_code == 200:
            raise HTTPError  # TODO: Replace with more appropriate approach
        return r.text

    def __repr__(self) -> str:
        return f"<Request object to {self.__url} with timeout={self.__timeout}.>"

    def __str__(self) -> str:
        return self.request_page()
