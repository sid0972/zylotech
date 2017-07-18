import random
from pymongo import MongoClient

def get_db():
    client = MongoClient('localhost:27017')
    db = client.zylo
    return db

def add_products(db):
    for i in range(1,10**7):
        db.transaction.insert({
        'userID':random.randint(1,10**7),
        'X':random.randint(1,10**5),
        'Z':random.randint(1,10**6)
        })

if __name__ == "__main__":

    db = get_db()
    add_products(db)
