from pymongo import MongoClient


def get_db():
    client = MongoClient(host='localhost', port=27017)
    db = client['python']
    return db


def add_one(db, data):
    result = db.python.insert_one(data)
    print("添加成功")
    return result


def add_many(collection_name, data):
    db = get_db()
    result = db[collection_name].insert_many(data)
    print("添加成功")
    return result


def update(collection_name, condition, prepare, db):
    result = db[collection_name].update_one(condition, prepare)
    print("修改成功")
    return result


def delete(col, condition, db):
    result = db[col].delete_one(condition)
    print("删除成功")
    return result


def query(col, condition, db):
    result = db[col].find(condition)
    return list(result)


def main():
    db = get_db()
    add_many('python', [{"name": "喵喵喵", "joy": "坦克"}, {"name": "鹅鹅鹅", "joy": "法师"}, {"name": "ccc", "joy": "战士"}], db)
    update('python', {"name": "西施"}, {"$set": {"joy": "王昭君"}}, db)
    delete('python', {"name": "喵喵喵"}, db)
    result = query('python', {'name': 'ccc'}, db)
    for item in result:
        print(item)
    print(result)


if __name__ == '__main__':
    main()
