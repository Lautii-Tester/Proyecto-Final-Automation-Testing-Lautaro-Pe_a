import pytest

#Configuarion de URL base para API Testing

@pytest.fixture
def URL_API():
    return "https://jsonplaceholder.typicode.com/"