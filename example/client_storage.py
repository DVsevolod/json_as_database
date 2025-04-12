from pydantic import BaseModel
from typing import List

from json_as_database import JSONasDataBase


class AccountModel(BaseModel):
    account_id: int
    account_type: str
    balance: float


class ClientModel(BaseModel):
    client_id: int
    name: str
    is_active: bool
    linked_accounts: List[AccountModel]


class ClientStorage:
    def __init__(self, filename):
        self.database = JSONasDataBase(filename)

    def add(self, data):
        client_model = ClientModel.model_validate(data)
        self.database.call(
            operation='create',
            key=client_model.client_id,
            value=client_model.model_dump()
        )

    def get(self, client_id):
        client_obj = self.database.call(
            operation='get',
            key=client_id
        )
        if client_obj is not None:
            return ClientModel.model_validate(client_obj)
        else:
            return "user does not exist"

    def update(self, client_id, data):
        client_obj = self.database.call(
            operation='get',
            key=client_id
        )
        if client_obj is not None:
            for key, val in data.items():
                if key in client_obj:
                    client_obj[key] = val

            self.database.call(
                operation='update',
                key=client_id,
                value=client_obj
            )
        else:
            return "user does not exist"

    def delete(self, client_id):
        self.database.call(
            operation='delete',
            key=client_id
        )


if __name__ == '__main__':
    def add_clients(client_storage):
        for i in range(5):
            data = {
                'client_id': 100100 + i,
                'name': f'user{i}',
                'is_active': True,
                'linked_accounts': [
                    {
                        'account_id': 200 + i,
                        'account_type': 'business',
                        'balance': 1023.476 * i
                    }
                ]
            }
            client_storage.add(data)

    client_storage = ClientStorage('clients.json')

    # add some clients
    # add_clients(client_storage)

    # get client
    # print(client_storage.get('100100'))

    # update client
    # updated_items = {'is_active': False}
    # client_storage.update(client_id="100100", data=updated_items)

    # delete client
    # client_storage.delete("100104")
