from empresa.config.database import SupabaseConnection

class BaseDAO:
    def __init__(self, table_name: str):
        self.connection = SupabaseConnection().client
        self.table = table_name

    def create(self, data: dict):
        response = self.connection.table(self.table).insert(data).execute()
        return response.data

    def read(self, filters: dict = None):
        query = self.connection.table(self.table).select("*")
        if filters:
            for key, value in filters.items():
                query = query.eq(key, value)
        response = query.execute()
        return response.data

    def update(self, id_value: int, data: dict):
        response = (
            self.connection.table(self.table)
            .update(data)
            .eq("id", id_value)
            .execute()
        )
        return response.data

    def delete(self, id_value: int):
        response = (
            self.connection.table(self.table)
            .delete()
            .eq("id", id_value)
            .execute()
        )
        return response.data