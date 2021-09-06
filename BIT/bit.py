class BIT:
    def __init__(self, n):
        self.tree = [0] * (n+1)  # tree[0] is unused
        self.depth = self._bit_length(n)
        self.size = n

    def _bit_length(self, n):
        length = 0
        while n:
            length += 1
            n >>= 1
        return length

    # sum between x[0] and x[i], inclusive
    def range_sum(self, i):
        ans = 0
        i += 1  # add 1 b/c tree[0] is not used
        while i:
            ans += self.tree[i]
            # Resets least significant bit that is 1.
            # Assumes two's complement.
            i -= i & (-i)  
        return ans

    def add(self, i, x):
        i += 1  # add 1 b/c tree[0] is not used
        while i <= self.size:
            self.tree[i] += x
            i += i & (-i)

    # returns minimum index with sum >= target
    def bisect_left(self, target):
        x = 0
        k = 1 << (self.depth - 1)
        while k:
            if x+k <= self.size and self.tree[x+k] < target:
                target -= self.tree[x+k]
                x += k
            k >>= 1
        return x


if __name__ == "__main__":
    import sys
    # minimum testing
    def test(name, size, calls, args, expects):
        bit = BIT(size)
        for i, (call, arg, expect) in enumerate(zip(calls, args, expects)):
            actual = getattr(bit, call)(*arg)
            if actual != expect:
                sys.stderr.write(
                    'FAILED at call {} in test {}: {}({}). expected: {}, actual: {}\n' \
                    .format(i, name, call, ','.join(map(str, arg)), expect, actual))
                return False
        print('{}:\tOK'.format(name))
        return True
    test('first_test',
         3,
         ['bisect_left', 'add', 'bisect_left'],
         [[1], [1, 1], [1]],
         [3, None, 1])
    test('second_test',
         10,
         ['bisect_left', 'bisect_left', 'add', 'bisect_left', 'add', 'bisect_left', 'bisect_left', 'bisect_left'],
         [[0], [1], [1, 1], [1], [0, 1], [0], [1], [2]],
         [0, 10, None, 1, None, 0, 0, 1])
    test('third_test',
         20,
         ['bisect_left', 'bisect_left', 'add', 'bisect_left', 'add', 'bisect_left', 'bisect_left', 'bisect_left', 'add', 'bisect_left', 'bisect_left', 'bisect_left'],
         [[0], [1], [10, 1], [1], [15, 1], [0], [1], [2], [10, -1], [0], [1], [2]],
         [0, 20, None, 10, None, 0, 10, 15, None, 0, 15, 20])
                           
