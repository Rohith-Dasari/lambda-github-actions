def lambda_handler(event, context):
    name = event.get("name", "World")
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": f"Hello, {name}!",
    }
