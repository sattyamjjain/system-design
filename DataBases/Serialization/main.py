import json

data = {
    "name": "John Smith",
    "age": 35,
    "interests": ["music", "travel", "photography"],
}

serialized_data = json.dumps(data)
print(serialized_data)

deserialized_data = json.loads(serialized_data)
print(deserialized_data)
