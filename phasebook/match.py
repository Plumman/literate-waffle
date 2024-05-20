import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    # print('match_id', fave_numbers_1)
    fave_numbers_1 = list(set(fave_numbers_1))
    fave_numbers_2 = list(set(fave_numbers_2))

    fave_numbers_1.sort()
    fave_numbers_2.sort()

    # print('match_id after', fave_numbers_1)

    pointer_in_fave_numbers_1 = 0
    pointer_in_fave_numbers_2 = 0
    """
    1                2
    ([1, 2, 3, 4], [2, 3]),
                    ^
            ^
    ([11, 81, 120, 31], [55, 12]),
    """
    while pointer_in_fave_numbers_1<len(fave_numbers_1) and pointer_in_fave_numbers_2<len(fave_numbers_2):
        if fave_numbers_2[pointer_in_fave_numbers_2] > fave_numbers_1[pointer_in_fave_numbers_1]:
            pointer_in_fave_numbers_1+=1
        elif fave_numbers_2[pointer_in_fave_numbers_2] == fave_numbers_1[pointer_in_fave_numbers_1]:
            pointer_in_fave_numbers_1+=1
            pointer_in_fave_numbers_2+=1
        else:
            return False
    
    if len(fave_numbers_2) != pointer_in_fave_numbers_2:
        return False

    # for number in fave_numbers_2:
    #     if number not in fave_numbers_1:
    #         return False

    return True
