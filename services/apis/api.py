from dataclasses import dataclass

import requests


@dataclass
class Api:
    __url_base_request: str

    def getUrlBaseRequest(self) -> str:
        return self.__url_base_request

    def _makeRequest(self, method: str, path: str, **kwards):
        return requests.request(method, path, **kwards)

    def getRequest(self, path: str, **kwards) -> requests.Response:
        try:
            return self._makeRequest('GET', self.getUrlBaseRequest() + path, **kwards)
        except requests.exceptions.RequestException as error:
            return error

    def postRequest(self, path: str, **kwards) -> requests.Response:
        try:
            return self._makeRequest('POST', self.getUrlBaseRequest() + path, **kwards)
        except requests.exceptions.RequestException as error:
            return error

    def putRequest(self, path: str, **kwards) -> requests.Response:
        try:
            return self._makeRequest('PUT', self.getUrlBaseRequest() + path, **kwards)
        except requests.exceptions.RequestException as error:
            return error

    def patchRequest(self, path: str, **kwards) -> requests.Response:
        try:
            return self._makeRequest('PATCH', self.getUrlBaseRequest() + path, **kwards)
        except requests.exceptions.RequestException as error:
            return error

    def deleteRequest(self, path: str, **kwards) -> requests.Response:
        try:
            return self._makeRequest('DELETE', self.getUrlBaseRequest() + path, **kwards)
        except requests.exceptions.RequestException as error:
            return error
