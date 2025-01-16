#class to represent a user in the system
class User:
    def __init__(self, user_id, name, timezone):
        '''
        Initializes a user object with the following attributes:
        :param user_id: a unique identifier for the user
        :param name: the name of the user
        :param timezone: the user's timezone
        '''
        self.user_id = user_id
        self.name = name
        self.timezone = timezone

    def __repr__(self):
        '''
        Define a string representation of the object.
        :return: user id, user name, timezone
        '''
        return f"User({self.user_id}, {self.name}, {self.timezone})"