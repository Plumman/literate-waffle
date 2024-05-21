def test_home(client):
    response = client.get("/")
    print(response.data)
    assert b"Hello World!" in response.data


def test_match(client, app):
    match_id=1
    response = client.get(f"/match/{match_id}")
    
    assert response.status_code == 200
    data = response.get_json()
    print("sdfdsdsf ", data)
    assert data['message'] == "No match"

