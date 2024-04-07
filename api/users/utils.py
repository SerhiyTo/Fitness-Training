from django.http import QueryDict


def query_params_to_dict(query_from_request: QueryDict) -> dict:
    filter_params = {}
    for key, value in query_from_request.items():
        filter_params[key] = value
    return filter_params
