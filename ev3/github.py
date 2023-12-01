import urequests as requests
import ujson as json

ACCESS_TOKEN = ''

def set_token(new_token):

    global ACCESS_TOKEN

    ACCESS_TOKEN = new_token

def repo_last_push(user, repo):

    global ACCESS_TOKEN

    url = 'https://api.github.com/repos/' + user + '/' + repo

    headers = {
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Expires': '0',
        'Authorization': 'Bearer ' + ACCESS_TOKEN,
        'Content-Type': 'application/json',
        'User-Agent' : 'BMOS'
    }

    response = requests.get(url, headers = headers)
    response = json.loads(response.text)

    pushed_at = response['pushed_at']   

    year = pushed_at[0:4]
    month = pushed_at[5:7]
    day = pushed_at[8:10]
    hours = pushed_at[11:13]
    minutes = pushed_at[14:16]
    seconds = pushed_at[17:19]

    return str(year) + str(month) + str(day) + str(hours) + str(minutes) + str(seconds)

def fetch_file(user, repo, branch, file):

    global ACCESS_TOKEN

    url = 'https://raw.githubusercontent.com/' + user + '/' + repo + '/' + branch + '/' + file

    headers = {
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Expires': '0',
        'Authorization': 'Bearer ' + ACCESS_TOKEN,
        'Content-Type': 'application/json',
        'User-Agent' : 'BMOS'
    }

    response = requests.get(url, headers = headers)
    response = response.text

    return response

