import time
from InstagramAPI import InstagramAPI
import random



def getTotalFollowers(api, user_id):
    """
    Returns the list of followers of the user.
    """

    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers


def getTotalFollowings(api, user_id):
    """
    Returns the list of followers of the user.
    """

    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowings(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers


def nonFollowers(followers, followings):
    nonFollowers = {}
    dictFollowers = {}
    for follower in followers:
        dictFollowers[follower['username']] = follower['pk']

    for followedUser in followings:
        if followedUser['username'] not in dictFollowers:
            nonFollowers[followedUser['username']] = followedUser['pk']

    return nonFollowers


def unFollow(USERNAME, PASS):
    api = InstagramAPI(USERNAME, PASS)
    api.login()
    listNonFollow = []
    user_id = api.username_id
    followers = getTotalFollowers(api, user_id)
    following = getTotalFollowings(api, user_id)
    nonFollow = nonFollowers(followers, following)
    print('Number of followers:', len(followers))
    print('Number of followings:', len(following))
    print('Number of nonFollowers:', len(nonFollow))
    for i in nonFollow:
        listNonFollow.append(i)
    listNonFollow.sort()
    return listNonFollow

