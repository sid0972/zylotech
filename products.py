import random
from pymongo import MongoClient

def get_db():
    client = MongoClient('localhost:27017')
    db = client.zylo
    return db

def add_products(db):
    alph = ['a','b','c','d','e']
    userID = 0
    Y = 0
    for i in range(1,10**7):
        db.product.insert({'userID':random.randint(1,10**7),
        'Y':random.choice(alph)})


if __name__ == "__main__":

    db = get_db()
    add_products(db)
