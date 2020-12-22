class SquidLogLine(object):
    def __init__(self):
        list_a = ['a', 'b', 'c']
        list_b = [10, 20, 30]
        
        print(list(map(lambda x, y: ord(x) + y, list_a, list_b)))
        list(map(lambda x, y: setattr(self, x, y), list_a, list_b))
        print(self.a)

s = SquidLogLine()
