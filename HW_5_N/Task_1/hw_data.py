from HW_5_N.Task_1.permissions import *


@full_permission
def delete_group(user, group_id):
    print("Group has been deleted")
    return True


@admin_permission
def delete_article(user, article_id):
    print("Article has been deleted")
    return True


@moderator_permission
def create_article(user, post_data):
    print("Article has been created")
    return True


@moderator_permission
def update_article(user, update_data):
    print("Article has been updated")
    return True


@user_permission
def share_article(user, article_id):
    print("Article has been shared")
    return True


@user_permission
def set_like_to_article(user, post_data):
    print("Like has been set")
    return True
