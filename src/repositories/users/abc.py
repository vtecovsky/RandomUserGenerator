from abc import ABC, abstractmethod


class AbstractUserRepository(ABC):
    @abstractmethod
    async def some_func(self):
        raise NotImplementedError()
