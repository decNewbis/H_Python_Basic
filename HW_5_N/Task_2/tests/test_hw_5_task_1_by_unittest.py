import unittest
import uuid

from datetime import datetime as dt

from HW_5_N.Task_1.script_1 import Member, Moderator, Admin
from HW_5_N.Task_1.hw_data import *


class TestMember(unittest.TestCase):
    params = {
        'name': 'Vasya',
        'surname': 'Pupkin',
        'age': 18,
    }

    def setUp(self) -> None:
        self.member = Member(**self.params)

    def tearDown(self) -> None:
        self.member = None

    def test_member_create(self):
        self.assertEqual(self.member.name, self.params['name'])
        self.assertEqual(self.member.surname, self.params['surname'])
        self.assertEqual(self.member.age, self.params['age'])

    def test_member_create_name_exception(self):
        params = self.params.copy()
        params.update({'name': 123})
        with self.assertRaises(TypeError):
            self.member = Member(**params)

    def test_member_create_surname_exception(self):
        params = self.params.copy()
        params.update({'surname': 123})
        with self.assertRaises(TypeError):
            self.member = Member(**params)

    def test_member_create_age_exception(self):
        params = self.params.copy()
        params.update({'age': '18'})
        with self.assertRaises(TypeError):
            self.member = Member(**params)

    def test_member_user_id(self):
        self.assertIsInstance(self.member.user_id, uuid.UUID)

    def test_member_join_date(self):
        self.assertEqual(self.member.join_date, dt.now().strftime("%d.%m.%Y"))

    def test_member_full_name(self):
        self.assertEqual(self.member.full_name, f'{self.member.name} {self.member.surname}')

    def test_member_set_user_id(self):
        with self.assertRaises(AttributeError):
            self.member.user_id = 1

    def test_member_set_join_date(self):
        with self.assertRaises(AttributeError):
            self.member.join_date = 1

    def test_member_change_name(self):
        self.member.change_name('Vasya_0')
        self.assertEqual(self.member.name, 'Vasya_0')

    def test_member_change_name_exception(self):
        with self.assertRaises(TypeError):
            self.member.change_name(123)

    def test_member_change_surname(self):
        self.member.change_surname('Pupkin_0')
        self.assertEqual(self.member.surname, 'Pupkin_0')

    def test_member_change_surname_exception(self):
        with self.assertRaises(TypeError):
            self.member.change_surname(123)

    def test_member_change_age(self):
        self.member.change_age(10)
        self.assertEqual(self.member.age, 10)

    def test_member_change_age_exception(self):
        with self.assertRaises(TypeError):
            self.member.change_age('123')

    def test_member_str(self):
        self.assertEqual(str(self.member), f'Користувач id: {self.member.user_id}')


class TestModerator(unittest.TestCase):
    params = {
        'name': 'Vasya_1',
        'surname': 'Pupkin_1',
        'age': 20,
    }

    def setUp(self) -> None:
        self.moderator = Moderator(**self.params)

    def tearDown(self) -> None:
        self.moderator = None

    def test_moderator_create(self):
        self.assertEqual(self.moderator.name, self.params['name'])
        self.assertEqual(self.moderator.surname, self.params['surname'])
        self.assertEqual(self.moderator.age, self.params['age'])

    def test_moderator_create_name_exception(self):
        params = self.params.copy()
        params.update({'name': 123})
        with self.assertRaises(TypeError):
            self.moderator = Moderator(**params)

    def test_moderator_create_surname_exception(self):
        params = self.params.copy()
        params.update({'surname': 123})
        with self.assertRaises(TypeError):
            self.moderator = Moderator(**params)

    def test_moderator_create_age_exception(self):
        params = self.params.copy()
        params.update({'age': '20'})
        with self.assertRaises(TypeError):
            self.moderator = Moderator(**params)

    def test_moderator_user_id(self):
        self.assertIsInstance(self.moderator.user_id, uuid.UUID)

    def test_moderator_join_date(self):
        self.assertEqual(self.moderator.join_date, dt.now().strftime("%d.%m.%Y"))

    def test_moderator_full_name(self):
        self.assertEqual(self.moderator.full_name, f'{self.moderator.name} {self.moderator.surname}')

    def test_moderator_badge(self):
        self.assertEqual(self.moderator.badge, 'Moderator')

    def test_moderator_set_user_id(self):
        with self.assertRaises(AttributeError):
            self.moderator.user_id = 1

    def test_moderator_set_join_date(self):
        with self.assertRaises(AttributeError):
            self.moderator.join_date = 1

    def test_moderator_change_name(self):
        self.moderator.change_name('Vasya_0')
        self.assertEqual(self.moderator.name, 'Vasya_0')

    def test_moderator_change_name_exception(self):
        with self.assertRaises(TypeError):
            self.moderator.change_name(123)

    def test_moderator_change_surname(self):
        self.moderator.change_surname('Pupkin_0')
        self.assertEqual(self.moderator.surname, 'Pupkin_0')

    def test_moderator_change_surname_exception(self):
        with self.assertRaises(TypeError):
            self.moderator.change_name(123)

    def test_moderator_change_age(self):
        self.moderator.change_age(10)
        self.assertEqual(self.moderator.age, 10)

    def test_moderator_change_age_exception(self):
        with self.assertRaises(TypeError):
            self.moderator.change_age('123')

    def test_moderator_change_badge_exception(self):
        with self.assertRaises(TypeError):
            self.moderator.change_badge(123)

    def test_moderator_change_badge_access_exception(self):
        self.moderator.badge = None
        with self.assertRaises(NoAccess):
            self.moderator.change_badge(123)

    def test_moderator_str(self):
        self.assertEqual(str(self.moderator), f'Користувач id: {self.moderator.user_id}')


class TestAdmin(unittest.TestCase):
    params = {
        'name': 'Vasya_1',
        'surname': 'Pupkin_1',
        'age': 20,
    }

    def setUp(self) -> None:
        self.admin = Admin(**self.params)

    def tearDown(self) -> None:
        self.admin = None

    def test_admin(self):
        self.assertEqual(self.admin.name, self.params['name'])
        self.assertEqual(self.admin.surname, self.params['surname'])
        self.assertEqual(self.admin.age, self.params['age'])
        self.assertEqual(self.admin.level, 1)

    def test_admin_create_name_exception(self):
        params = self.params.copy()
        params.update({'name': 123})
        with self.assertRaises(TypeError):
            self.admin = Admin(**params)

    def test_admin_create_surname_exception(self):
        params = self.params.copy()
        params.update({'surname': 123})
        with self.assertRaises(TypeError):
            self.admin = Admin(**params)

    def test_admin_create_age_exception(self):
        params = self.params.copy()
        params.update({'age': '20'})
        with self.assertRaises(TypeError):
            self.admin = Admin(**params)

    def test_admin_create_level_exception(self):
        params = self.params.copy()
        params.update({'level': '4'})
        with self.assertRaises(TypeError):
            self.admin = Admin(**params)

    def test_admin_default_level(self):
        self.assertEqual(self.admin.level, 1)

    def test_admin_user_id(self):
        self.assertIsInstance(self.admin.user_id, uuid.UUID)

    def test_admin_join_date(self):
        self.assertEqual(self.admin.join_date, dt.now().strftime("%d.%m.%Y"))

    def test_admin_full_name(self):
        self.assertEqual(self.admin.full_name, f'{self.admin.name} {self.admin.surname}')

    def test_admin_badge(self):
        self.assertEqual(self.admin.badge, 'Admin')

    def test_admin_set_user_id(self):
        with self.assertRaises(AttributeError):
            self.admin.user_id = 1

    def test_admin_set_join_date(self):
        with self.assertRaises(AttributeError):
            self.admin.join_date = 1

    def test_admin_change_name(self):
        self.admin.change_name('Vasya_0')
        self.assertEqual(self.admin.name, 'Vasya_0')

    def test_admin_change_name_exception(self):
        with self.assertRaises(TypeError):
            self.admin.change_name(123)

    def test_admin_change_surname(self):
        self.admin.change_surname('Pupkin_0')
        self.assertEqual(self.admin.surname, 'Pupkin_0')

    def test_admin_change_surname_exception(self):
        with self.assertRaises(TypeError):
            self.admin.change_name(123)

    def test_admin_change_age(self):
        self.admin.change_age(10)
        self.assertEqual(self.admin.age, 10)

    def test_admin_change_age_exception(self):
        with self.assertRaises(TypeError):
            self.admin.change_age('123')

    def test_admin_change_badge_exception(self):
        with self.assertRaises(TypeError):
            self.admin.change_badge(123)

    def test_admin_change_badge_access_exception(self):
        self.admin.badge = None
        with self.assertRaises(NoAccess):
            self.admin.change_badge(123)

    def test_admin_change_level(self):
        self.admin.change_level(2)
        self.assertEqual(self.admin.level, 2)

    def test_admin_change_level_exception(self):
        with self.assertRaises(TypeError):
            self.admin.change_level('123')

    def test_admin_change_level_access_exception(self):
        self.admin.badge = None
        with self.assertRaises(NoAccess):
            self.admin.change_level(2)

    def test_admin_str(self):
        self.assertEqual(str(self.admin), f'Користувач id: {self.admin.user_id}')


class TestMemberPermission(unittest.TestCase):
    params = {
        'name': 'Vasya',
        'surname': 'Pupkin',
        'age': 18,
    }

    def setUp(self) -> None:
        self.member = Member(**self.params)

    def test_member_permission_set_like_to_article(self):
        self.assertTrue(set_like_to_article(self.member, None), 'Test result is not True')

    def test_member_permission_set_like_to_article_without_exception(self):
        try:
            set_like_to_article(self.member, None)
        except NoAccess:
            self.fail(f'Test raised NoAccess unexpectedly')

    def test_member_permission_share_article(self):
        self.assertTrue(share_article(self.member, None), 'Test result is not True')

    def test_member_permission_share_article_without_exception(self):
        try:
            share_article(self.member, None)
        except NoAccess:
            self.fail(f'Test raised NoAccess unexpectedly')

    def test_member_permission_update_article_exception(self):
        with self.assertRaises(NoAccess):
            update_article(self.member, None)

    def test_member_permission_create_article_exception(self):
        with self.assertRaises(NoAccess):
            create_article(self.member, None)

    def test_member_permission_delete_article_exception(self):
        with self.assertRaises(NoAccess):
            delete_article(self.member, None)

    def test_member_permission_delete_group_exception(self):
        with self.assertRaises(NoAccess):
            delete_group(self.member, None)


class TestModeratorPermission(unittest.TestCase):
    params = {
        'name': 'Vasya_1',
        'surname': 'Pupkin_1',
        'age': 20,
    }

    def setUp(self) -> None:
        self.moderator = Moderator(**self.params)

    def test_moderator_permission_set_like_to_article(self):
        self.assertTrue(set_like_to_article(self.moderator, None), 'Test result is not True')

    def test_moderator_permission_set_like_to_article_without_exception(self):
        try:
            set_like_to_article(self.moderator, None)
        except NoAccess:
            self.fail(f'Test raised NoAccess unexpectedly')

    def test_moderator_permission_share_article(self):
        self.assertTrue(share_article(self.moderator, None), 'Test result is not True')

    def test_moderator_permission_share_article_without_exception(self):
        try:
            share_article(self.moderator, None)
        except NoAccess:
            self.fail(f'Test raised NoAccess unexpectedly')

    def test_moderator_permission_update_article(self):
        self.assertTrue(update_article(self.moderator, None), 'Test result is not True')

    def test_moderator_permission_update_article_without_exception(self):
        try:
            update_article(self.moderator, None)
        except NoAccess:
            self.fail(f'Test raised NoAccess unexpectedly')

    def test_moderator_permission_create_article(self):
        self.assertTrue(create_article(self.moderator, None), 'Test result is not True')

    def test_moderator_permission_create_article_without_exception(self):
        try:
            create_article(self.moderator, None)
        except NoAccess:
            self.fail(f'Test raised NoAccess unexpectedly')

    def test_moderator_permission_delete_article_exception(self):
        with self.assertRaises(NoAccess):
            delete_article(self.moderator, None)

    def test_moderator_permission_delete_group_exception(self):
        with self.assertRaises(NoAccess):
            delete_group(self.moderator, None)


class TestAdminPermission(unittest.TestCase):
    params = {
        'name': 'Vasya_1',
        'surname': 'Pupkin_1',
        'age': 20,
        'level': 1
    }

    def setUp(self) -> None:
        self.admin = Admin(**self.params)

    def tearDown(self) -> None:
        self.admin = None

    def test_admin_permission_set_like_to_article(self):
        self.assertTrue(set_like_to_article(self.admin, None), 'Test result is not True')

    def test_admin_permission_set_like_to_article_without_exception(self):
        try:
            set_like_to_article(self.admin, None)
        except NoAccess:
            self.fail(f'Test raised NoAccess unexpectedly')

    def test_admin_permission_share_article(self):
        self.assertTrue(share_article(self.admin, None), 'Test result is not True')

    def test_admin_permission_share_article_without_exception(self):
        try:
            share_article(self.admin, None)
        except NoAccess:
            self.fail(f'Test raised NoAccess unexpectedly')

    def test_admin_permission_update_article(self):
        self.assertTrue(update_article(self.admin, None), 'Test result is not True')

    def test_admin_permission_update_article_without_exception(self):
        try:
            update_article(self.admin, None)
        except NoAccess:
            self.fail(f'Test raised NoAccess unexpectedly')

    def test_admin_permission_create_article(self):
        self.assertTrue(create_article(self.admin, None), 'Test result is not True')

    def test_admin_permission_create_article_without_exception(self):
        try:
            create_article(self.admin, None)
        except NoAccess:
            self.fail(f'Test raised NoAccess unexpectedly')

    def test_admin_permission_delete_article(self):
        self.assertTrue(delete_article(self.admin, None), 'Test result is not True')

    def test_admin_permission_delete_article_without_exception(self):
        try:
            delete_article(self.admin, None)
        except NoAccess:
            self.fail(f'Test raised NoAccess unexpectedly')

    def test_admin_permission_delete_group_exception(self):
        with self.assertRaises(NoAccess):
            delete_group(self.admin, None)

    def test_admin_full_permission_delete_group(self):
        self.admin.change_level(3)
        self.assertTrue(delete_group(self.admin, None), 'Test result is not True')

    def test_admin_full_permission_delete_group_without_exception(self):
        self.admin.change_level(3)
        try:
            delete_group(self.admin, None)
        except NoAccess:
            self.fail(f'Test raised NoAccess unexpectedly')


if __name__ == '__main__':
    unittest.main()
