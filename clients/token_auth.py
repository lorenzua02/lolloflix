import requests


def singup(acc_data: dict) -> None:
    registration_endpoint = "http://127.0.0.1:8000/auth/users/"
    response = requests.post(registration_endpoint, data=acc_data)
    print(response, response.text)


def login(login_cred: dict) -> str:
    login_endpoint = "http://127.0.0.1:8000/auth/token/login/"
    response = requests.post(login_endpoint, data=login_cred)
    status_code = response.status_code
    print(f"Status Code: {response.status_code}")
    if status_code == 200:
        token = response.json()["auth_token"]
        print(f"Auth Token: {token}")
        return token


def client(auth_token: str, endpoint: str) -> None:
    token_h = f"Token {auth_token}"
    headers = {"Authorization": token_h}
    response = requests.get(endpoint, headers=headers)
    status_code = response.status_code
    print(f"Status Code: {response.status_code}")
    if status_code == 200:
        print(response.json())


if __name__ == "__main__":
    account_data = {
        "username": "mytestuserx",
        "email": "test@myrest.comx",
        "password": "verystrongpassword",
        "re_password": "verystrongpassword",
    }
    singup(account_data)

    login_credentials = {"username": "mytestuserx", "password": "verystrongpassword"}
    auth_token = login(login_credentials)

    # data_endpoint = "http://127.0.0.1:8000/api/profiles/"
    # client(auth_token, data_endpoint)
