from users.models import User, UserRoles


def create_admin_user():
    user = User.objects.create(
        email='test_admin@mail.com',
        role=UserRoles.MODERATOR,
        is_active=True,
        is_superuser=True,
        is_staff=True,
    )
    user.set_password('qwerty')
    user.save()
    return user


def create_member_user():
    user = User.objects.create(
        email='test_member@mail.com',
        role=UserRoles.MEMBER,
        is_active=True,
        is_superuser=False,
        is_staff=False,
    )
    user.set_password('querty')
    user.save()
    return user
