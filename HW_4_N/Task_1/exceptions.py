class NotFound(Exception):
    def __init__(self, *args):
        if args:
            self.msg = args[0]
        else:
            self.msg = None

    def __str__(self):
        if self.msg:
            return f'{self.msg} немає у базі даних.'
        else:
            return 'NotFound'


class NoAccess(Exception):
    def __init__(self, *args):
        if args:
            self.msg = args[0]
        else:
            self.msg = None

    def __str__(self):
        if self.msg:
            return f'{self.msg} немає доступу.'
        else:
            return 'NoAccess'
