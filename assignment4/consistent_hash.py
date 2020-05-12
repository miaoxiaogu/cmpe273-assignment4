import hashlib
import pickle
from hashlib import md5

class ConsistentHash(object):
    def __init__(self, nodes=None, replicas=2):
        self.ring = dict()
        self.replicas = replicas
        self._sorted_keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)

    def get_key(self, key):
        key_bytes = pickle.dumps(key)
        return int(hashlib.md5(key_bytes).hexdigest(), 16)

    def add_node(self, node):
        for i in range(0, self.replicas):
            key = self.get_key('%s:%s' % (node, i))
            self.ring[key] = node
            self._sorted_keys.append(key)
        self._sorted_keys.sort()

    def remove_node(self, node):
        for i in range(0, self.replicas):
            key = self.get_key('%s:%s' % (node, i))
            del self.ring[key]
            self._sorted_keys.remove(key)

    def get_node(self, string_key):
        key = self.get_key(string_key)
        nodes = self._sorted_keys
        for i in range(0, len(nodes)):
            node = nodes[i]
            if key <= node:
                return self.ring[node]
        return self.ring[nodes[0]]