__author__ = 'mjholler'


def require_authentication(f):
    def wrapper(self, *args, **kwargs):
        auth = self.request.get('auth')
        if auth:
            return f(self, *args, **kwargs)
        else:
            self.response.set_status(403)
            self.response.write('403 Not Authorized')

    return wrapper
