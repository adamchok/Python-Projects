class User:
    def __init__(self, user_id, username):
        # set attributes using parameters
        self.id = user_id
        self.username = username

        # default values:
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Angela")
user_2 = User("002", "Jack")

user_1.follow(user_2)
user_2.follow(user_1)

print(f"User 1 followers: {user_1.followers}\nUser 1 followings: {user_1.following}\n")
print(f"User 2 followers: {user_2.followers}\nUser 1 followings: {user_2.following}")