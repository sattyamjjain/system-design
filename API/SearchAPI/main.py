import json
from typing import List

data = [
    {
        "id": 1,
        "title": "Lorem ipsum",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "tags": ["lorem", "ipsum", "dolor"],
    },
    {
        "id": 2,
        "title": "Dolor sit amet",
        "description": "Dolor sit amet, consectetur adipiscing elit.",
        "tags": ["dolor", "sit", "amet"],
    },
    {
        "id": 3,
        "title": "Consectetur adipiscing elit",
        "description": "Praesent et massa vel ante commodo commodo a eu massa.",
        "tags": ["consectetur", "adipiscing", "elit"],
    },
]


def search(query: str) -> List[dict]:
    _results = []
    for document in data:
        if (
            query.lower() in document["title"].lower()
            or query.lower() in document["description"].lower()
            or query.lower() in [tag.lower() for tag in document["tags"]]
        ):
            _results.append(document)
    return _results


results = search("Lorem")
print(json.dumps(results, indent=2))
