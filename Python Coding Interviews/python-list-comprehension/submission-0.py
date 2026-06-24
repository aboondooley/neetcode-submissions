from typing import List


def create_list_of_odds(n: int) -> List[int]:
    return [i+1 for i in range(0,n) if (i+1) % 2 == 1]



# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
