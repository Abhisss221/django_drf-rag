class DataVersion:
    def __init__(self):
        self._versions = {}

    def get(self, user_id: int) -> int:
        return self._versions.get(user_id, 1)

    def increment(self, user_id: int):
        self._versions[user_id] = self.get(user_id) + 1


data_version = DataVersion()
