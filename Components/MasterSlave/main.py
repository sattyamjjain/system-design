import redis

master = redis.Redis(host="my-master-redis-host", port=6379)
slave1 = redis.Redis(host="my-slave-redis-host-1", port=6379)
slave2 = redis.Redis(host="my-slave-redis-host-2", port=6379)

master.set("my-key", "my-value")

value = slave1.get("my-key")
if value is None:
    value = slave2.get("my-key")

master_config = {"slaveof": None}

slave1_config = {"slaveof": ("my-master-redis-host", 6379)}
slave2_config = {"slaveof": ("my-master-redis-host", 6379)}

master.config_set(**master_config)
slave1.config_set(**slave1_config)
slave2.config_set(**slave2_config)
