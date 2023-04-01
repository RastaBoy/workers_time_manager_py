from abc import ABC, abstractmethod


# Не факт, что пригодится
class IConverter(ABC):
    
    @abstractmethod
    def convert_user(self, obj):
        ...
        
    @abstractmethod
    def convert_task(self, obj):
        ...

    @abstractmethod
    def convert_project(self, obj):
        ...
        
    @abstractmethod
    def convert_history(self, obj):
        ...