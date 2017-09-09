class User(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def __str__(self):
        return "{} id:{}, name:{} {}".format('{', self.id, self.name, '}')

class DB(object):
    def __init__(self):
        self.contents = []
        self.next_id = 1
    
    def create(self, name):
        newUser = User(name, self.next_id)
        self.next_id += 1
        self.contents.append(newUser)
        
    def all(self):
        return self.contents

    def get(self, id):
        for User in self.contents:
            if User.id == id:
                return User
    
    def filter(self, name):
        filter_list = []
        for User in self.contents:
            if User.name == name:
                filter_list.append(name)
        return filter_list
    
    def exclude(self, name):
        exclude_list = []
        for User in self.contents:
            if User.name != name:
                exclude_list.append(name)
        return exclude_list

UserDB = DB()
UserDB.create('justin')
UserDB.create('ainoi')
UserDB.create('nick')
UserDB.create('ian')
UserDB.create('ian')
x = UserDB.get(1)
y = UserDB.get(3)
print x, 'first list'
print y, 'second list'
users_name_ian = UserDB.filter('ian')
print users_name_ian, "unfortunately we found him."