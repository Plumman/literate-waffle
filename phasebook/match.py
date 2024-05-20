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

def is_match(fave_numbers_1: list, fave_numbers_2: list):
    """check if all the numbers in 2nd list is in the first list

    Parameters:
        fave_numbers_1: contains the search space of numbers
        fave_numbers_2: contains the numbers that should be in the first list

    Returns:
        True if all the numbers in the fave_numbers_2 is in fave_numbers_1, False otherwise
    """
    fave_numbers_1 = set(fave_numbers_1)
    fave_numbers_2 = set(fave_numbers_2)
    return fave_numbers_2.issubset(fave_numbers_1)

