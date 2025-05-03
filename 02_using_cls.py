class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def counts(cls):
        print(f'Total Number of Objects Created : {cls.count}')
c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()        
Counter.counts()