from django.conf import settings
from rest_framework.response import Response

def response_modify_decorator_list_or_get_after_execution_for_onoff_pagination(func):
    def inner(self, request, *args, **kwargs):
        response = func(self, request, *args, **kwargs)
        data_dict = {}

        if 'results' in response.data:
            data_dict = response.data
        else:
            data_dict['results'] = response.data
        data_dict['status_code'] = response.status_code
        query = self.request.query_params.get('query', None)
        if query:
            data_dict['query'] = str(self.queryset.query)
        if response.data:
            data_dict['request_status'] = 1
            data_dict['msg'] = settings.MSG_SUCCESS
        elif len(response.data) == 0:
            data_dict['request_status'] = 1
            data_dict['msg'] = settings.MSG_NO_DATA
        else:
            data_dict['request_status'] = 0
            data_dict['msg'] = settings.MSG_ERROR

        response.data = data_dict
        return response
    return inner
