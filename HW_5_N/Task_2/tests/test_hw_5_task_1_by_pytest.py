import pytest
import uuid

from datetime import datetime as dt

from HW_5_N.Task_1.script_1 import Member, Moderator, Admin
from HW_5_N.Task_1.hw_data import *


PARAM = {
    'name': 'Vasya',
    'surname': 'Pupkin',
    'age': 18,
}


@pytest.fixture()
def create_user():
    class Constructor:
        def __init__(self):
            self.users = []

        def create_member(self, params_):
            user = Member(**params_)
            self.users.append(user)
            return user

        def create_moderator(self, params_):
            user = Moderator(**params_)
            self.users.append(user)
            return user

        def create_admin(self, params_):
            user = Admin(**params_)
            self.users.append(user)
            return user

        def clean_up(self):
            self.users = []

    result = Constructor()
    yield result
    result.clean_up()


@pytest.mark.parametrize('params', [PARAM])
def test_user(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    assert member.name == params['name']
    assert member.surname == params['surname']
    assert member.age == params['age']

    assert moderator.name == params['name']
    assert moderator.surname == params['surname']
    assert moderator.age == params['age']

    assert admin.name == params['name']
    assert admin.surname == params['surname']
    assert admin.age == params['age']


@pytest.mark.parametrize('params', [
    {
        'name': 123,
        'surname': 'Pupkin',
        'age': 18,
    },
])
def test_user_create_name_exception(create_user, params):
    with pytest.raises(TypeError):
        member = create_user.create_member(params)
    with pytest.raises(TypeError):
        moderator = create_user.create_moderator(params)
    with pytest.raises(TypeError):
        admin = create_user.create_admin(params)


@pytest.mark.parametrize('params', [
    {
        'name': 'Vasya',
        'surname': 123,
        'age': 18,
    },
])
def test_user_create_surname_exception(create_user, params):
    with pytest.raises(TypeError):
        member = create_user.create_member(params)
    with pytest.raises(TypeError):
        moderator = create_user.create_moderator(params)
    with pytest.raises(TypeError):
        admin = create_user.create_admin(params)


@pytest.mark.parametrize('params', [
    {
        'name': 'Vasya',
        'surname': 'Pupkin',
        'age': '18',
    },
])
def test_user_create_age_exception(create_user, params):
    with pytest.raises(TypeError):
        member = create_user.create_member(params)
    with pytest.raises(TypeError):
        moderator = create_user.create_moderator(params)
    with pytest.raises(TypeError):
        admin = create_user.create_admin(params)


@pytest.mark.parametrize('params', [PARAM])
def test_user_user_id(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    assert isinstance(member.user_id, uuid.UUID)
    assert isinstance(moderator.user_id, uuid.UUID)
    assert isinstance(admin.user_id, uuid.UUID)


@pytest.mark.parametrize('params', [PARAM])
def test_user_join_date(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)
    dt_now = dt.now().strftime("%d.%m.%Y")

    assert member.join_date == dt_now
    assert moderator.join_date == dt_now
    assert admin.join_date == dt_now


@pytest.mark.parametrize('params', [PARAM])
def test_user_full_name(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    assert member.full_name == f'{member.name} {member.surname}'
    assert moderator.full_name == f'{moderator.name} {moderator.surname}'
    assert admin.full_name == f'{admin.name} {admin.surname}'


@pytest.mark.parametrize('params', [PARAM])
def test_user_set_user_id(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    with pytest.raises(AttributeError):
        member.user_id = 1
    with pytest.raises(AttributeError):
        moderator.user_id = 1
    with pytest.raises(AttributeError):
        admin.user_id = 1


@pytest.mark.parametrize('params', [PARAM])
def test_user_set_join_date(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    with pytest.raises(AttributeError):
        member.join_date = 1
    with pytest.raises(AttributeError):
        moderator.join_date = 1
    with pytest.raises(AttributeError):
        admin.join_date = 1


@pytest.mark.parametrize('params', [PARAM])
def test_user_change_name(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    member.change_name('Vasya_0')
    assert member.name == 'Vasya_0'
    moderator.change_name('Vasya_0')
    assert moderator.name == 'Vasya_0'
    admin.change_name('Vasya_0')
    assert admin.name == 'Vasya_0'


@pytest.mark.parametrize('params', [PARAM])
def test_user_change_name_exception(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    with pytest.raises(TypeError):
        member.change_name(123)
    with pytest.raises(TypeError):
        moderator.change_name(123)
    with pytest.raises(TypeError):
        admin.change_name(123)


@pytest.mark.parametrize('params', [PARAM])
def test_user_change_surname(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    member.change_surname('Pupkin_0')
    assert member.surname == 'Pupkin_0'
    moderator.change_surname('Pupkin_0')
    assert moderator.surname == 'Pupkin_0'
    admin.change_surname('Pupkin_0')
    assert admin.surname == 'Pupkin_0'


@pytest.mark.parametrize('params', [PARAM])
def test_user_change_surname_exception(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    with pytest.raises(TypeError):
        member.change_surname(123)
    with pytest.raises(TypeError):
        moderator.change_surname(123)
    with pytest.raises(TypeError):
        admin.change_surname(123)


@pytest.mark.parametrize('params', [PARAM])
def test_user_change_age(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    member.change_age(10)
    assert member.age == 10
    moderator.change_age(10)
    assert moderator.age == 10
    admin.change_age(10)
    assert admin.age == 10


@pytest.mark.parametrize('params', [PARAM])
def test_user_change_age_exception(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    with pytest.raises(TypeError):
        member.change_age('123')
    with pytest.raises(TypeError):
        moderator.change_age('123')
    with pytest.raises(TypeError):
        admin.change_age('123')


@pytest.mark.parametrize('params', [PARAM])
def test_user_change_badge(create_user, params):
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    moderator.change_badge('123')
    assert moderator.badge == '123'
    admin.change_badge('123')
    assert admin.badge == '123'


@pytest.mark.parametrize('params', [PARAM])
def test_user_change_badge_exception(create_user, params):
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    with pytest.raises(TypeError):
        moderator.change_badge(123)
    with pytest.raises(TypeError):
        admin.change_badge(123)


@pytest.mark.parametrize('params', [PARAM])
def test_user_change_badge_access_exception(create_user, params):
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    moderator.badge = None
    with pytest.raises(NoAccess):
        moderator.change_badge('Mdr')
    admin.badge = None
    with pytest.raises(NoAccess):
        admin.change_badge('Adm')


@pytest.mark.parametrize('params', [PARAM])
def test_user_change_level(create_user, params):
    admin = create_user.create_admin(params)

    admin.change_level(2)
    assert admin.level == 2


@pytest.mark.parametrize('params', [PARAM])
def test_user_change_leve_exception(create_user, params):
    admin = create_user.create_admin(params)

    with pytest.raises(TypeError):
        admin.change_level('123')


@pytest.mark.parametrize('params', [PARAM])
def test_user_change_level_access_exception(create_user, params):
    admin = create_user.create_admin(params)

    admin.badge = None
    with pytest.raises(NoAccess):
        admin.change_level(2)


@pytest.mark.parametrize('params', [PARAM])
def test_user_str(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    assert str(member) == f'Користувач id: {member.user_id}'
    assert str(moderator) == f'Користувач id: {moderator.user_id}'
    assert str(admin) == f'Користувач id: {admin.user_id}'


@pytest.mark.parametrize('params', [PARAM])
def test_user_permission_set_like_to_article(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    assert set_like_to_article(member, None) is True
    assert set_like_to_article(moderator, None) is True
    assert set_like_to_article(admin, None) is True


@pytest.mark.parametrize('params', [PARAM])
def test_user_permission_set_like_to_article_without_exception(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    try:
        set_like_to_article(member, None)
    except NoAccess:
        pytest.fail(f'Test raised NoAccess unexpectedly')
    try:
        set_like_to_article(moderator, None)
    except NoAccess:
        pytest.fail(f'Test raised NoAccess unexpectedly')
    try:
        set_like_to_article(admin, None)
    except NoAccess:
        pytest.fail(f'Test raised NoAccess unexpectedly')


@pytest.mark.parametrize('params', [PARAM])
def test_user_permission_share_article(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    assert share_article(member, None) is True
    assert share_article(moderator, None) is True
    assert share_article(admin, None) is True


@pytest.mark.parametrize('params', [PARAM])
def test_user_permission_share_article_without_exception(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    try:
        share_article(member, None)
    except NoAccess:
        pytest.fail(f'Test raised NoAccess unexpectedly')
    try:
        share_article(moderator, None)
    except NoAccess:
        pytest.fail(f'Test raised NoAccess unexpectedly')
    try:
        share_article(admin, None)
    except NoAccess:
        pytest.fail(f'Test raised NoAccess unexpectedly')


@pytest.mark.parametrize('params', [PARAM])
def test_user_permission_update_article(create_user, params):
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    assert update_article(moderator, None) is True
    assert update_article(admin, None) is True


@pytest.mark.parametrize('params', [PARAM])
def test_user_permission_update_article_exception(create_user, params):
    member = create_user.create_member(params)

    with pytest.raises(NoAccess):
        update_article(member, None)


@pytest.mark.parametrize('params', [PARAM])
def test_user_permission_update_article_without_exception(create_user, params):
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    try:
        update_article(moderator, None)
    except NoAccess:
        pytest.fail(f'Test raised NoAccess unexpectedly')
    try:
        update_article(admin, None)
    except NoAccess:
        pytest.fail(f'Test raised NoAccess unexpectedly')


@pytest.mark.parametrize('params', [PARAM])
def test_user_permission_create_article(create_user, params):
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    assert create_article(moderator, None) is True
    assert create_article(admin, None) is True


@pytest.mark.parametrize('params', [PARAM])
def test_user_permission_create_article_exception(create_user, params):
    member = create_user.create_member(params)

    with pytest.raises(NoAccess):
        create_article(member, None)


@pytest.mark.parametrize('params', [PARAM])
def test_user_permission_create_article_without_exception(create_user, params):
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    try:
        create_article(moderator, None)
    except NoAccess:
        pytest.fail(f'Test raised NoAccess unexpectedly')
    try:
        create_article(admin, None)
    except NoAccess:
        pytest.fail(f'Test raised NoAccess unexpectedly')


@pytest.mark.parametrize('params', [PARAM])
def test_user_permission_delete_article(create_user, params):
    admin = create_user.create_admin(params)

    assert delete_article(admin, None) is True


@pytest.mark.parametrize('params', [PARAM])
def test_user_permission_delete_article_exception(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)

    with pytest.raises(NoAccess):
        delete_article(member, None)
    with pytest.raises(NoAccess):
        delete_article(moderator, None)


@pytest.mark.parametrize('params', [PARAM])
def test_user_permission_delete_article_without_exception(create_user, params):
    admin = create_user.create_admin(params)

    try:
        delete_article(admin, None)
    except NoAccess:
        pytest.fail(f'Test raised NoAccess unexpectedly')


@pytest.mark.parametrize('params', [PARAM])
def test_user_permission_delete_group_exception(create_user, params):
    member = create_user.create_member(params)
    moderator = create_user.create_moderator(params)
    admin = create_user.create_admin(params)

    with pytest.raises(NoAccess):
        delete_group(member, None)
    with pytest.raises(NoAccess):
        delete_group(moderator, None)
    with pytest.raises(NoAccess):
        delete_group(admin, None)


@pytest.mark.parametrize('params', [PARAM])
def test_admin_full_permission_delete_group(create_user, params):
    admin = create_user.create_admin(params)
    admin.change_level(3)

    assert delete_group(admin, None) is True


@pytest.mark.parametrize('params', [PARAM])
def test_admin_full_permission_delete_group_without_exception(create_user, params):
    admin = create_user.create_admin(params)
    admin.change_level(3)

    try:
        delete_group(admin, None)
    except NoAccess:
        pytest.fail(f'Test raised NoAccess unexpectedly')


if __name__ == '__main__':
    pytest.main()
