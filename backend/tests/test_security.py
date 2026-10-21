from app.security import hash_password, verify_password

def test_hash_password():
    assert hash_password("secret123") != "secret123"
    
def test_verify_password_1():
    assert verify_password("secret123", hash_password("secret123")) is True
    
def test_verify_password_2():
    assert verify_password("wrong", hash_password("secret123")) is False