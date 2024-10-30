import json

from decouple import config

from services.apis.api import Api


class PloomesApi(Api):
    def __init__(self, url: str):
        super().__init__(url)
        self.__user_key = config('PLOOMES_USER_KEY')

    def getUserKey(self) -> str:
        return self.__user_key

    def getHeaders(self) -> dict:
        return {'User-Key': self.getUserKey()}

    def __getQueryStringIfExists(self, separator: str, query_string: str, **kwargs) -> str:
        if query_string in kwargs:
            match query_string:
                case 'filter':
                    return f'{separator}$filter={kwargs["filter"]}'
                case 'expand':
                    return f'{separator}$expand={kwargs["expand"]}'
                case 'select':
                    return f'{separator}$select={kwargs["select"]}'
                case 'top':
                    return f'{separator}$top={kwargs["top"]}'
                case 'skip':
                    return f'{separator}$skip={kwargs["skip"]}'
                case 'orderby':
                    return f'{separator}$orderby={kwargs["orderby"]}'

        else:
            return ''

    def __getCompletePath(self, table: str, **kwargs):
        query_strings = ['filter', 'expand', 'select', 'top', 'skip', 'orderby']
        separator = '?'
        path = f'{table}'
        for query_string in query_strings:
            parametro = self.__getQueryStringIfExists(separator, query_string, **kwargs)
            path += parametro

            if separator == '?' and parametro != '':
                separator = '&'

        return path

    def getAllDatas(self, table: str, **kwargs) -> dict:
        path = self.__getCompletePath(table, **kwargs)
        request = self.getRequest(path=path, headers=self.getHeaders())
        request = json.loads(request.text)

        return request

    def getData(self, table: str, **kwargs) -> dict:
        path = self.__getCompletePath(table, **kwargs)
        request = self.getRequest(path=path, headers=self.getHeaders())
        if request.status_code >= 400:
            return {}

        request = json.loads(request.text)
        return request['value'][0] if len(request['value']) > 0 else None

    def updateData(self, table: str, instance_ploomes: dict, instance: dict) -> str:
        table = table + f"({instance_ploomes['Id']})"
        path = self.__getCompletePath(table)

        self.patchRequest(path, headers=self.getHeaders(), json=instance)

        return instance_ploomes['Id']

    def createData(self, table: str, data: dict) -> int:
        path = self.__getCompletePath(table)

        create_data = self.postRequest(path, headers=self.getHeaders(), json=data)

        if create_data.status_code >= 400:
            return -1

        elif create_data.status_code == 200:
            create_data = json.loads(create_data.text)
            return create_data['value'][0]['Id']
