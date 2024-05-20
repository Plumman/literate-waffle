from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    return_list = []
    list_of_args = args.keys()
    for row in USERS:
        if 'id' in list_of_args:
            if search_user_match_id(row['id'], args['id']):
                return_list.append(row)
                continue
        if 'name' in list_of_args:
            if search_user_match_name(row['name'], args['name']):
                return_list.append(row)
                continue
        if 'age' in list_of_args:
            if search_user_match_age(row['age'], args['age']):
                return_list.append(row)
                continue
        if 'occupation' in list_of_args:
            if search_user_match_occupation(row['occupation'], args['occupation']):
                return_list.append(row)
                continue

    return return_list

def search_user_match_id(row_id, id):
    if id == None:
        return False 
    elif row_id == id:
        return True 
    else:
        return False
    
def search_user_match_name(row_name, name):
    if name == None:
        return False 
    elif name in row_name:
        return True 
    else:
        return False
    
def search_user_match_age(row_age: int, age: int):
    row_age = int(row_age)
    age = int(age)
    if age == None:
        return False 
    elif (age == (row_age+1)) or  (age == (row_age-1)) or age == row_age:
        return True 
    else:
        return False
    
def search_user_match_occupation(row_occupation, occupation):
    if occupation == None:
        return False 
    elif occupation in row_occupation:
        return True 
    else:
        return False