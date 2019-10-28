import yaml

class AccountIterator:
    def __init__(self, spec):
        self.iterator = iter(spec.keys())

    def next(self):
        n = self.iterator.next()
        if n == '__default__':
            n = self.iterator.next()
        return n

class AccountEntry:
    def __init__(self, spec):
        self.spec = spec

    def __getitem__(self, name):
        # FIXME: should do automatic computations here
        return self.spec[name]

    def __iter__(self):
        return iter(self.spec)

class AccountConfig:
    def __init__(self, spec):
        self.spec = spec
        if 'accounts' not in spec:
            spec['accounts'] = {}

    def __getitem__(self, name):
        if name in self.spec['accounts']:
            return AccountEntry(self.spec['accounts'][name])
        return None

    def __iter__(self):
        return AccountIterator(self.spec['accounts'])
