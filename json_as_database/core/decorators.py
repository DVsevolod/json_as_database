import json


def file_processing(self):
    def decorator(func):
        def wrapper(*args):
            with open(self.file_path, 'r') as file:
                self.storage = json.load(file)

            result = func(*args)

            with open(self.file_path, 'w') as file:
                json.dump(result, file, indent=4)

        return wrapper
    return decorator


def item_removing(self):
    def decorator(func):
        def wrapper(*args):
            with open(self.file_path, 'r') as file:
                self.storage = json.load(file)

            result = func(*args)

            with open(self.file_path, 'w') as file:
                file.write(json.dumps(self.storage, indent=4))
            return result
        return wrapper
    return decorator


def file_reading(self):
    def decorator(func):
        def wrapper(*args):
            with open(self.file_path, 'r') as file:
                self.storage = json.load(file)

            result = func(*args)

            return result
        return wrapper
    return decorator
