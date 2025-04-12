import json
import os

from json_as_database.core.decorators import file_processing, file_reading, item_removing


current_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(current_dir, '..'))


class JSONasDataBase:

    def __init__(self, file_name):
        self.file_path = os.path.join(base_dir, 'files', file_name)
        self.storage = {}

        if not os.path.exists(self.file_path):
            self._create_file()

    def _create_file(self):
        with open(self.file_path, 'w') as file:
            file.write(json.dumps(self.storage, indent=4))

    def call(self, operation, key, value=None):
        operations_list = ['create', 'update', 'get', 'delete', 'pop']

        if operation not in operations_list:
            raise ValueError(f'Wrong operation type. Must be: {operations_list}')
        elif operation in ['create', 'update'] and value is None:
            raise ValueError('Value was not provided.')

        @file_processing(self)
        def create(key, value):
            self.storage.update({key: value})
            return self.storage

        @file_processing(self)
        def update(key, value):
            if key in self.storage:
                self.storage.pop(key)
                self.storage[key] = value
                return self.storage
            return self.storage

        @file_reading(self)
        def get(key):
            return self.storage.get(key)

        @item_removing(self)
        def pop(key):
            if key in self.storage:
                return self.storage.pop(key)

        if operation == 'create':
            create(key, value)
        elif operation == 'update':
            update(key, value)
        elif operation == 'get':
            return get(key)
        elif operation == 'delete':
            pop(key)
        elif operation == 'pop':
            return pop(key)
