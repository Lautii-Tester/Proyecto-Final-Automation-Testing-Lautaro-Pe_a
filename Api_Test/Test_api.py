import requests
import pytest

class TestGetUser:
    @pytest.mark.get
    def test_get_response_data(self, URL_API):
        response = requests.get(URL_API + "users")
        print(response.status_code)
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance (data,list)
        assert len(data) > 0
        
        #Validar los primeros tres usuarios
        for user in data[:3]:
            assert isinstance(user["id"], int), "ID no es un entero"
            assert isinstance(user["name"], str), "Name debe ser una cadena"
            assert "@" in user ["email"], "Email debe tener un @"

class TestPostUser:
    @pytest.mark.post
    def test_post_response_code(self, URL_API):
        new_user = {
            "name": "Bart",
            "username": "Simpsons",
            "email": "Yonofui@Aycaramba.com"
        }
        response = requests.post(URL_API + "users", json=new_user)
        print(response.status_code)
        assert response.status_code == 201

        data = response.json()
        assert isinstance (data,dict)

        assert data["name"] == new_user["name"], "El name no coincide"
        assert data["username"] == new_user["username"], "Userame no coincide"
        assert "@" in data["email"], "Email debe tener un @"


class TestPatchUser:
    @pytest.mark.patch
    def test_patch_response_code(self, URL_API):
        updated_user = {
            "Name": "Bort"
        }
        response = requests.patch(URL_API + "users/1", json=updated_user)
        print(response.status_code)
        assert response.status_code == 200

        data=response.json()
        assert data["name"] == updated_user["name"], "El name no coincide"
