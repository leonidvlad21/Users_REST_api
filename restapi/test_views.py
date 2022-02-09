
import requests as req
s_url = "http://127.0.0.1:8000/restapi/usersets/"
d_heads = {'Content-Type': 'application/json'}
d_json = {"name": "test2name", "email": "test2@mail.com", "password": "test_psw"}
last_id = 0

def get_data(id_value):
    response = req.get(s_url)
    response_body = response.json()
    for item in response_body:
        if item["id"] == id_value:
            return item["name"]
    
def test_UsersList():
    response = req.get(s_url)
    assert response.status_code == 200
    response_body = response.json()
    assert len(response_body) > 0

def test_post():
    response = req.post(s_url, headers=d_heads, json=d_json)
    assert response.status_code == 200
    response_data = response.json()['data']
    new_id = response_data['id']
    new_name = get_data(new_id)
    assert new_name == response_data['name']
    return new_id

def test_update():
    last_id = test_post()
    assert last_id > 0;
    response = req.get(s_url+str(last_id)+'/')
    response_data = response.json()['data']
    last_name = response_data['name']
    response = req.patch(s_url+str(last_id)+'/', json={'name':last_name+' updated'})
    assert response.status_code == 200
    response_data = response.json()['data']
    updated_name = response_data['name']
    assert updated_name == last_name+' updated'
    
"""
prev.:
def test_User():
    response = req.post("http://127.0.0.1:8000/restapi/usersets/", \
                        headers={'Content-Type': 'application/json'}, \
json={"name": "test2name", "email": "test2@mail.com", "password": "test_psw"})
    assert response.status_code == 200

def test_id():
    response = req.get("http://127.0.0.1:8000/restapi/usersets/1/")
    assert response.status_code == 200
    response_body = response.json()
    print(response_body["data"])
    assert response_body["data"]["id"] == 1
"""
