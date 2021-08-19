import json
import requests

BASE_URL = "http://localhost:8000/"

def login(username, password):
    head = {'accept': 'application/json', 'Content-Type': 'application/json'}
    authjson = json.dumps({'username': username, 'password': password})
    # authjson = json.dumps(authdata)
    path = "%sapi/auth/" %BASE_URL

    try:
        r = requests.post(
            path,
            headers=head,
            data=authjson,
            verify=False,
            timeout=(30, 30))

    except Exception as x:
        print('EXCEPTION: Failed to connect restful api. Failure reason:', x.__class__.__name__)
        print('Exception:', x)
    except requests.exceptions.RequestException as err:
        print("Error", err)
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    finally:
        return None

    return r.json()['access_token']


def get(token, url):
    head = {'accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %token}
    path = '%s%s' %(BASE_URL, url)
    try:
        r = requests.get(
            path,
            headers=head,
            verify=False,
            timeout=(30, 30))

    except Exception as x:
        print('EXCEPTION: Failed to connect restful api. Failure reason:', x.__class__.__name__)
        print('Exception:', x)
    except requests.exceptions.RequestException as err:
        print("Error", err)
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    finally:
        print(r)

    content_type = r.headers['Content-Type']

    if (r.status_code == 202):
        location = r.headers['Location']
        return location

    if (content_type == 'application/json'):
        respdata = r.json()

    elif (content_type == 'text/plain'):
        respdata = r.text

    return respdata


def post(token, data, path):
    head = {'accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %token}
    input_json = json.dumps(data)

    r = requests.post(
        path,
        data = input_json,
        headers = head,
        verify = False,
        timeout=(30, 30))

    return r.json()

def delete(token, url):
    head = {'accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer %s' %token}
    path = '%s%s' % (BASE_URL, url)

    r = requests.delete(
        path,
        headers = head,
        verify = False,
        timeout=(30, 30))

    return  str(r.status_code)

def get_body(key, value, type):
    return {"data": [ { "key": key, "val": val, "valType": type } ] }

if __name__ == '__main__':
    # body_post = {"data": [ { "key": "key1", "val": "val1", "valType": "str" } ] }
    # created_object = {'id': 2, 'values': [{'key': 'key1', 'val': 'val1', 'valType': 'str'}]}

    token = login('test','1234')
    created_object = post(token, body_post, '%sapi/poly/' %BASE_URL)
    get_objects = get(token, '%sapi/poly' %(BASE_URL))
    get_specific_object = get(token, '%sapi/poly/%s' % (BASE_URL, created_object['id']))
    del_objects = delete(token, '%sapi/poly/%s' % (BASE_URL, created_object['id']))
    # del_objects = delete(token, '%sapi/poly/%s' % (BASE_URL,3))
    # print(get_objects)
