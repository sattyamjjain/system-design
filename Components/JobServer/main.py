from flask import Flask, request, jsonify
from queue import Queue
import threading

app = Flask(__name__)
job_queue = Queue()


def worker():
    while True:
        job = job_queue.get()
        print(f"Executing job {job['id']} with data {job['data']}")
        job_queue.task_done()


@app.route("/job", methods=["POST"])
def create_job():
    data = request.get_json()
    if "data" not in data:
        return jsonify({"error": "Invalid data"}), 400
    job_id = job_queue.qsize() + 1
    job = {"id": job_id, "data": data["data"]}
    job_queue.put(job)
    return jsonify({"id": job_id}), 201


if __name__ == "__main__":
    for i in range(4):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()
    app.run(debug=True)
