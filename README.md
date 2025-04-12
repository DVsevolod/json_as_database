# JSON as DataBase

This simple class allows you to store data in a json-file.
CRUD functionality is implemented and supports all standard operations:
- `create` to add object to the file,
- `get`    to get object from the file, 
- `update` to update object in the file,
- `delete` to delete object in the file,
- `pop`    to cut to get object from the file
____

## Usage 
____

During the initialization process, the file name must be passed. 
If the file does not exist, it will be created automatically. 
The class itself is responsible for storing files and accessing them.

Example:
```Python
from json_as_database import JSONasDataBase


database = JSONasDataBase('my_file.json')
```

The class has only one method `call(operation, key, value)` for interacting with the file. 
This method takes 3 arguments: `operation`, `key`, `value`.

- `operation` - string, one of the CRUD operations: `create`, `get`, `update`, `delete`, `pop`;
- `key` - key for/in json-file used as database;
- `value` - value for json-file used as database.

Example:
```Python
from json_as_database import JSONasDataBase


data = {'user_id': 1, 'username': 'test', 'params': None}


database = JSONasDataBase('my_file.json')
database.call(
    operation='create',
    key=data.get('user_id'),
    value=data
)
user = database.call(
    operation='get',
    key=data.get('user_id')
)
```