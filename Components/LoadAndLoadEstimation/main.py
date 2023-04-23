from typing import Any

import psutil
import time


def get_system_load():
    load = psutil.cpu_percent()
    time.sleep(1)
    load = psutil.cpu_percent()
    return load


def estimate_load():
    current_load = get_system_load()
    predicted_load = current_load * 2
    return predicted_load


def perform_request() -> Any:
    return


def measure_throughput(num_requests):
    start_time = time.time()
    for i in range(num_requests):
        perform_request()
    end_time = time.time()
    elapsed_time = end_time - start_time
    throughput = num_requests / elapsed_time
    return throughput


def log_response_time(_time):
    print(f"Response time, {time}")


def measure_response_time():
    start_time = time.time()
    response = perform_request()
    end_time = time.time()
    elapsed_time = end_time - start_time
    log_response_time(elapsed_time)
    return response


def log_latency(_time):
    print(f"Response latency, {time}")


def measure_latency(num_requests):
    start_time = time.time()
    latencies = []
    for i in range(num_requests):
        start_request_time = time.time()
        perform_request()
        end_request_time = time.time()
        elapsed_request_time = end_request_time - start_request_time
        latencies.append(elapsed_request_time)
        log_latency(elapsed_request_time)
    end_time = time.time()
    elapsed_time = end_time - start_time
    avg_latency = sum(latencies) / len(latencies)
    return avg_latency


cpu_percent = psutil.cpu_percent(interval=1)
print(cpu_percent)


mem = psutil.virtual_memory()
mem_percent = mem.percent
print(mem_percent)

disk_io = psutil.disk_io_counters()
read_bytes = disk_io.read_bytes
write_bytes = disk_io.write_bytes
print(read_bytes)
print(write_bytes)

net_io = psutil.net_io_counters()
bytes_sent = net_io.bytes_sent
bytes_recv = net_io.bytes_recv
print(bytes_sent)
print(bytes_recv)



