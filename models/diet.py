class Diet:
    def __init__(self, id, name, description, date, isHealthy) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.date = date
        self.isHealthy = isHealthy

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date": self.date,
            "isHealthy": self.isHealthy
        }
