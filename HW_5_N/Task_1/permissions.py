from HW_5_N.Task_1.exceptions import NoAccess


def user_permission(func):
    def wrapper(user_, data_):
        result = func(user_, data_)
        return result
    return wrapper


def moderator_permission(func):
    def wrapper(user_, data_):
        if user_.__dict__.get('badge') is not None:
            result = func(user_, data_)
            return result
        else:
            raise NoAccess(f"{user_}")
    return wrapper


def admin_permission(func):
    def wrapper(user_, data_):
        if user_.__dict__.get('badge') == 'Admin':
            result = func(user_, data_)
            return result
        else:
            raise NoAccess(f"{user_}")
    return wrapper


def full_permission(func):
    def wrapper(user_, data_):
        if user_.__dict__.get('badge') == 'Admin' and user_.__dict__.get('level') >= 3:
            result = func(user_, data_)
            return result
        else:
            raise NoAccess(f"{user_}")
    return wrapper
