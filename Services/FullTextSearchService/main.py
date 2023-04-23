from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(["http://localhost:9200"])


class Document:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content


def index_document(document):
    es.index(
        index="documents",
        body={"id": document.id, "title": document.title, "content": document.content},
    )


@app.route("/search", methods=["GET"])
def search_documents():
    query = request.args.get("q", "")
    results = es.search(
        index="documents",
        body={
            "query": {"multi_match": {"query": query, "fields": ["title", "content"]}}
        },
    )["hits"]["hits"]
    documents = [
        Document(r["_source"]["id"], r["_source"]["title"], r["_source"]["content"])
        for r in results
    ]
    return jsonify({"documents": [doc.__dict__ for doc in documents]})


if __name__ == "__main__":
    for doc in [
        Document(
            1, "Lorem Ipsum", "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        ),
        Document(2, "Python Tutorial", "Learn Python programming with this tutorial."),
        Document(3, "Flask Web Framework", "Build web applications with Flask."),
    ]:
        index_document(doc)
    app.run(debug=True)
