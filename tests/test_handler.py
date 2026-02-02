from src.handler import lambda_handler


def test_hello_default():
    result = lambda_handler({}, {})
    assert result["statusCode"] == 200
    assert result["body"] == "Hello, World!"


def test_hello_name():
    result = lambda_handler({"name": "Rohith"}, {})
    assert result["body"] == "Hello, Rohith!"
