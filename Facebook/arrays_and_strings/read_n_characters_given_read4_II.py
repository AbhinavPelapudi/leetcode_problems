class Solution(object):
    def __init__(self):
        self.rest = collections.deque()
    def read(self, buf, n):
        cur = collections.deque()
        for i in xrange(n):
            if self.rest: buf[i] = self.rest.popleft(); continue
            if not cur:
                while len(cur) < 4: cur.append('')
                if not read4(cur): break
            buf[i] = cur.popleft()
        else:
            while cur: self.rest.append(cur.popleft())
            return n
        return i