mport requests


def recurse(subreddit, hot_list=[], after=None):
    """List with titles of all hot Articles """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(
                                url,
                                headers=headers,
                                params=params,
                                allow_redirects=False
                            )
    if response.status_code == 200:
        data = response.json().get('data')
        if data is not None:
            children = data.get('children')
            if children is not None:
                for child in children:
                    hot_list.append(child.get('data').get('title'))
                after = data.get('after')
                if after is not None:
                    return recurse(subreddit, hot_list, after)
                else:
                    return hot_list
        else:
            return hot_list
    else:
        return None
mport requests


def recurse(subreddit, hot_list=[], after=None):
    """List with titles of all hot Articles """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(
                                url,
                                headers=headers,
                                params=params,
                                allow_redirects=False
                            )
    if response.status_code == 200:
        data = response.json().get('data')
        if data is not None:
            children = data.get('children')
            if children is not None:
                for child in children:
                    hot_list.append(child.get('data').get('title'))
                after = data.get('after')
                if after is not None:
                    return recurse(subreddit, hot_list, after)
                else:
                    return hot_list
        else:
            return hot_list
    else:
        return None
mport requests


def recurse(subreddit, hot_list=[], after=None):
    """List with titles of all hot Articles """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(
                                url,
                                headers=headers,
                                params=params,
                                allow_redirects=False
                            )
    if response.status_code == 200:
        data = response.json().get('data')
        if data is not None:
            children = data.get('children')
            if children is not None:
                for child in children:
                    hot_list.append(child.get('data').get('title'))
                after = data.get('after')
                if after is not None:
                    return recurse(subreddit, hot_list, after)
                else:
                    return hot_list
        else:
            return hot_list
    else:
        return None
mport requests


def recurse(subreddit, hot_list=[], after=None):
    """List with titles of all hot Articles """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(
                                url,
                                headers=headers,
                                params=params,
                                allow_redirects=False
                            )
    if response.status_code == 200:
        data = response.json().get('data')
        if data is not None:
            children = data.get('children')
            if children is not None:
                for child in children:
                    hot_list.append(child.get('data').get('title'))
                after = data.get('after')
                if after is not None:
                    return recurse(subreddit, hot_list, after)
                else:
                    return hot_list
        else:
            return hot_list
    else:
        return Noneing a REST API, and a given emp_ID, return info about their TODO list.
"""
import requests
import sys


if __name__ == "__main__":
    """ main section """
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee = requests.get(
        BASE_URL + f'/users/{sys.argv[1]}/').json()
    EMPLOYEE_NAME = employee.get("name")
    employee_todos = requests.get(
        BASE_URL + f'/users/{sys.argv[1]}/todos').json()
    serialized_todos = {}

    for todo in employee_todos:
        serialized_todos.update({todo.get("title"): todo.get("completed")})

    COMPLETED_LEN = len([k for k, v in serialized_todos.items() if v is True])
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, COMPLETED_LEN, len(serialized_todos)))
    for key, val in serialized_todos.items():
        if val is True:
            print("\t {}".format(key))
