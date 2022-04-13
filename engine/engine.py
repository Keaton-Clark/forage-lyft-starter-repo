from abc import ABC
class Engine(ABC, Serviceable):
    def __init__(self):
        pass
    @abstractmethod
    def needs_service(self):
        pass
