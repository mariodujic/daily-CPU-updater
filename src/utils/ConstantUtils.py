def constant(f):
    def temp_set(self, value):
        raise TypeError

    def temp_get(self):
        return f(self)

    return property(temp_get, temp_set)


class _Const:
    @constant
    def THOUGHT_COLLECTION_HR(self):
        return "hr-thoughts-staging"

    @constant
    def THOUGHT_COLLECTION_EN(self):
        return "en-thoughts-staging"


CONST = _Const()
