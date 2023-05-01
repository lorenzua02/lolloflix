from token_auth import singup


if __name__ == "__main__":
    for i in range(10):
        creds = {
            "username": f"testuser_no{i}",
            "email": f"testuser_no{i}@gmail.com",
            "password": "ciao",
            "re_password": "ciao",
        }
        singup(creds)
