from connector.connection import stat

def get_value(name):
    r = stat.find_one({"FirstName": name})
    return r