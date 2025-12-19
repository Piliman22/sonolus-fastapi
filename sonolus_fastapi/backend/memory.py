from typing import Generic, TypeVar, Dict, List, Optional

T = TypeVar("T")

class MemoryItemStore(Generic[T]):
    def __init__(self, item_cls):
        self.item_cls = item_cls
        self._data: Dict[str, T] = {}
        
    def get(self, name: str) -> Optional[T]:
        return self._data.get(name)
    
    def list(self) -> List[T]:
        return list(self._data.values())
    
    def add(self, item: T):
        self._data[item.name] = item
    
    def delete(self, name: str):
        self._data.pop(name, None)