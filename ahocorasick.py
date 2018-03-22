from collections import deque

class Dictionary(object):
    '''
    >>> patterns = ['he', 'she', 'his', 'hers']
    >>> d = Dictionary(patterns)
    >>> list(d.matches('ushers'))
    [(0, 3, 1), (0, 3, 0), (0, 5, 3)]
    >>> multiline_text = """
    ... ushe
    ... rs
    ... """
    >>> list(d.matches(multiline_text)) # ignores line breaks
    [(1, 3, 1), (1, 3, 0), (2, 1, 3)]
    '''


    def __init__(self, patterns):
        self._phase1(patterns)
        self._phase2()


    def matches(self, text):
        root = 0

        line = 0
        column = 0
        i = root
        for c in text:
            if c == '\n':
                line += 1
                column = 0
                continue

            while i != root and not self._edge_exists(i, c):
                i = self._failure(i)

            if self._edge_exists(i, c):
                i = self._edge_destination(i, c)
                for o in self._output(i):
                    yield (line, column, o)
            column += 1


    def _phase1(self, patterns):
        self._edges = [None]
        self._out = {}
        i = 0
        for pattern in patterns:
            u = 0
            for c in pattern:
                u = self._insert(u, c)
            self._add_output(u, i)
            i += 1


    def _phase2(self):
        root = 0

        self._fail = [0] * len(self._edges)
        self._fail[root] = -1

        q = deque()

        for _, v in self._edges_from(root):
            self._set_failure(v, root)
            q.append(v)

        while len(q) > 0:
            u = q.popleft()
            for c, v in self._edges_from(u):
                fu = self._failure(u)

                while fu != root and not self._edge_exists(fu, c):
                    fu = self._failure(fu)

                if self._edge_exists(fu, c):
                    fv = self._edge_destination(fu, c)
                    self._set_failure(v, fv)
                    self._merge_output(fv, v)

                q.append(v)

    def _insert(self, u, c):
        edges = self._edges[u]

        if edges is None:
            edges = {}
            self._edges[u] = edges

        if c in edges:
            return edges[c]
        else:
            self._edges.append(None)
            newnode = len(self._edges) - 1
            self._edges[u][c] = newnode
            return newnode


    def _add_output(self, u, i):
        if not u in self._out:
            self._out[u] = []
        self._out[u].append(i)


    def _edges_from(self, u):
        edges = self._edges[u]
        if edges is None:
            return iter(())
        else:
            return edges.iteritems()


    def _set_failure(self, u, v):
        self._fail[u] = v


    def _failure(self, u):
        return self._fail[u]


    def _edge_exists(self, u, c):
        edges = self._edges[u]
        return not edges is None and c in edges


    def _edge_destination(self, u, c):
        return self._edges[u][c]


    def _merge_output(self, u, v):
        if not u in self._out:
            return
        if not v in self._out:
            self._out[v] = []
        self._out[v].extend(self._out[u])


    def _output(self, u):
        if not u in self._out:
            return []
        else:
            return self._out[u]

if __name__ == '__main__':
    import sys
    import codecs
    if len(sys.argv) != 3:
        sys.exit(1)
    else:
        dict_path = sys.argv[1]
        text_path = sys.argv[2]
        stats = False
        if len(sys.argv) > 3 and sys.argv[3] == '-s':
            stats = True

        patterns = []
        with codecs.open(dict_path, 'r', 'utf-8') as f:
            for pattern in f:
                pattern = pattern.strip()
                patterns.append(pattern)

        with codecs.open(text_path, 'r', 'utf-8') as f:
            text = f.read()

        d = Dictionary(patterns)
        for line, column, i in d.matches(text):
            p = patterns[i]
            print('{}:{} {}'.format(
                line + 1, column + 1 - len(p) + 1, codecs.encode(p, 'utf-8')))
