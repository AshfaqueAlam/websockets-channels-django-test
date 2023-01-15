
def get_sorted_by_fields(self, response):
    field_name = self.request.query_params.get('ordering')
    if 'results' in response:
        if '-' in field_name:
            field_name = field_name[1:]
            response['results'] = sorted(response['results'], key=lambda i: i[field_name]if i[field_name] else '', reverse=True)
        else:
            response['results'] = sorted(response['results'], key=lambda i: i[field_name] if i[field_name] else '')
    else:
        if '-' in field_name:
            field_name = field_name[1:]
            response = sorted(response, key=lambda i: i[field_name]if i[field_name] else '', reverse=True)
        else:
            response = sorted(response, key=lambda i: i[field_name] if i[field_name] else '')
    return response
