import random


class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.num_servers = len(servers)
        self.server_statuses = [True] * self.num_servers

    def choose_server(self):
        available_servers = [i for i in range(self.num_servers) if self.server_statuses[i]]
        if not available_servers:
            return None
        return random.choice(available_servers)

    def handle_request(self, request):
        server_index = self.choose_server()
        if server_index is None:
            raise Exception("No available servers")
        server = self.servers[server_index]
        return server.handle_request(request)

    def set_server_status(self, server_index, status):
        self.server_statuses[server_index] = status
