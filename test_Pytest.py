import pytest

@pytest.yield_fixture()
def anyThing():
    print("Before method anything")
    yield
    print("After method anything")

@pytest.fixture()
def setUp():
    print("This is a setUp method")

def test_Login_Email(setUp,anyThing):
    print("Ths is a login email test")



def test_Login_Facebook(setUp,anyThing):
    print("Ths is a login facebook test")



def test_Login_Twitter(setUp,anyThing):
    print("Ths is a login twitter test")
