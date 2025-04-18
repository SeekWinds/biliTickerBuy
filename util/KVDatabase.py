from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage


class KVDatabase:
    def __init__(self, db_path):
        if db_path is None:
            self.db = TinyDB(storage=MemoryStorage)
        else:
            self.db = TinyDB(db_path)
        self.KeyValue = Query()

    def insert(self, key, value):
        # 如果键已经存在，更新其值；否则插入新键值对
        if self.db.contains(self.KeyValue.key == key):
            self.db.update({'value': value}, self.KeyValue.key == key)
        else:
            self.db.insert({'key': key, 'value': value})

    def get(self, key):
        result = self.db.get(self.KeyValue.key == key)
        return result['value'] if result else None

    def update(self, key, value):
        if self.db.contains(self.KeyValue.key == key):
            self.db.update({'value': value}, self.KeyValue.key == key)
        else:
            raise KeyError(f"Key '{key}' not found in database.")

    def delete(self, key):
        self.db.remove(self.KeyValue.key == key)

    def contains(self, key):
        return self.db.contains(self.KeyValue.key == key)
