from behave import given, when, then
from social_network import SocialNetwork, User

@given('зарегистрирован пользователь с электронной почтой "{email}"')
def step_impl(context, email):
    if not hasattr(context, 'network'):
        context.network = SocialNetwork()
    username = email.split('@')[0]
    user = User(username, email, "password")
    context.network.register_user(user)

@when('пользователь "{user_email}" добавляет в друзья "{friend_email}"')
def step_impl(context, user_email, friend_email):
    context.network.add_friend(user_email, friend_email)

@then('пользователь "{friend_email}" появляется в списке друзей пользователя "{user_email}"')
def step_impl(context, user_email, friend_email):
    user = context.network.users[user_email]
    assert friend_email in user.friends

@then('пользователь "{user_email}" также появляется в списке друзей пользователя "{friend_email}"')
def step_impl(context, user_email, friend_email):
    friend = context.network.users[friend_email]
    assert user_email in friend.friends
