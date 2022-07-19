# def greeting(name:str) -> str :
#     return 'Hello ' + name

# print(greeting('kwame'))

# Vector = list[float]

# def scale(scalar:float, vector:Vector) -> Vector:
#     return [scalar * num for num in vector]

# new_vector = scale(2.0, [1.0, -4.2, 5.4])

# print(new_vector)

# from collections.abc import Sequence

# ConnetionOptions = dict[str, str]
# Address = tuple[str, int]
# Server = tuple[Address, ConnetionOptions]

# def broadcast_message(message:str, servers:Sequence[Server]) -> None:
#     ...

# def broadcast_message(
#         message:str, 
#         servers:Sequence[tuple[tuple[str, int], dict[str, str]]]) -> None:
#         ...

# from typing import NewType

# UserId = NewType('UserId', int)
# some_id = UserId(52345)
# print(some_id)

# def get_user_name(user_id: UserId) -> str:
#     ...

# user_a = get_user_name(UserId(56783))
# print(user_a)

# UserId = NewType('UserId', int)
# ProUserId = NewType('ProUserId', UserId

# from collections.abc import Callable
# from typing import Awaitable

# def feeder(get_next_item:Callable[[], str]):
#     ...
# def async_query(on_success:Callable[[int], None],
#                 on_error:Callable[[int, Exception], None]) -> None:
#     ...

# async def on_update(value:str) -> None:
#     print('nothing ')

# callback: Callable[[str], Awaitable[None]] = on_update

# print(on_update('kwaku'))

# from typing import Any

# a: Any = None
# a= []
# a=2

# s: str = ''
# print(s=a)

