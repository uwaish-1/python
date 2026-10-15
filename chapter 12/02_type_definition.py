from typing import List, Tuple, Dict, Set, Union, Optional

n : int = 5
name : str = "John Doe"

def sum(a: int, b: int) -> int:
    return a + b

result : int = sum(3, 4)

# type definiton for a list of integers
# numbers : List[int] = [1, 2, 3, 4, 5]   

# tuple of strings
# person : Tuple[str, str] = ("John", "Doe")

# dictionary with string keys and integer values
# ages : Dict[str, int] = {"John": 30, "Jane": 25}

# union type for a variable that can be either an int or a str  
# value : Union[int, str] = 42

#  match status : Optional[str] = None

# def http_request(url: str) -> Optional[Dict[str, Union[int, str]]]:
#     # Simulating an HTTP request
#     if url == "https://example.com":
#         return {"status": 200, "message": "OK"}
#     else:
#         return None

# def http_status(status):
#     match status:
#         case 200:
#             return "OK"
#         case 404:
#             return "Not Found"
#         case 500:
#             return "Internal Server Error"
#         case _:
#             return "Unknown Status"