"""
100 Days of Code, Day 17, Lesson 117
Create your own classes in Python
"""


class User:
    """
    User class
    """

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        """
        follow another user
        """
        user.followers += 1
        self.following += 1


def main():
    """
    Code for Day ddd Lesson 117
    Create your own classes in Python
    """
    user_1 = User("001", "smops")
    user_2 = User("002", "jack")
    print(f"{user_1.id=}, {user_1.username=}, {user_1.followers=}, {user_1.following=}")
    print(f"{user_2.id=}, {user_2.username=}, {user_2.followers=}, {user_2.following=}")
    user_1.follow(user_2)
    print(f"{user_1.id=}, {user_1.username=}, {user_1.followers=}, {user_1.following=}")
    print(f"{user_2.id=}, {user_2.username=}, {user_2.followers=}, {user_2.following=}")


if __name__ == "__main__":
    main()
