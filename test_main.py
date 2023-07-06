from main import app
from fastapi.testclient import TestClient
from fastapi import status

client = TestClient(app)


def make_query_url(offset=0, limit=5,sort_by:str=None):
    url = "?"
    if offset != 0:
        url += f"offset={offset}"
    if limit != 5:
        url += f"&limit={limit}"
    if sort_by:
        url += f"&sort_by={sort_by}"
    return url


def test_list_info_success():
    INFO_LIST_URL = "/info/list"
    # 1. success, all param use default value
    query_url = make_query_url()
    print(query_url)
    response = client.get(
        INFO_LIST_URL + query_url,
        headers={"x-token": "xxx"},
    )
    assert response.status_code == status.HTTP_200_OK

    # fail, offset < 0
    query_url = make_query_url(offset = -1)
    print(query_url)
    response = client.get(
        INFO_LIST_URL + query_url,
        headers={"x-token": "xxx"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # fail, limit < 0
    query_url = make_query_url(limit = -1)
    response = client.get(
        INFO_LIST_URL + query_url,
        headers={"x-token": "xxx"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # fail, wrong sort_by type
    query_url = make_query_url(sort_by="wrong type")
    response = client.get(
        INFO_LIST_URL + query_url,
        headers={"x-token": "xxx"},
    )
    print(f"xxx:{response.status_code}")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    

