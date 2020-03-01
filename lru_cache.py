class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None
        self.prev = None


class LRU_cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head



    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = p


    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p



    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1

    def set(self, key, value):
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]


cache = LRU_cache(3)

cache.set('a', 'apple')
cache.set('b', 'ball')
cache.set('c', 'cat')
cache.set('d', 'dog')
print(cache.get('a'))
print(cache.get('c'))