import multiprocessing


def process_batch(batch):
    result = []
    for item in batch:
        result.append(item.upper())
    return result


def batch_process(_input_data, batch_size=10):
    batches = [
        _input_data[i : i + batch_size] for i in range(0, len(_input_data), batch_size)
    ]
    with multiprocessing.Pool() as pool:
        results = pool.map(process_batch, batches)
    return [item for batch_result in results for item in batch_result]


input_data = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon",
]
output_data = batch_process(input_data, batch_size=3)
print(output_data)
