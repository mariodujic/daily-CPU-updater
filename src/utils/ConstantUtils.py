def constant(f):
    def temp_set(self, value):
        raise TypeError

    def temp_get(self):
        return f(self)

    return property(temp_get, temp_set)


class _Const(object):
    @constant
    def THOUGHT_COLLECTION(self):
        return "hello"


CONST = _Const()
