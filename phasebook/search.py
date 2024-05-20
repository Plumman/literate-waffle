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
    if args == {}:
        return USERS
    return_list = []
    for i in args:
        return_list = check_condition(USERS, i, args[i], return_list)
    return return_list


def check_condition(
        users: list, 
        attribute: str, 
        attribute_value: str, 
        return_list: list
        ):
    """
    Search through a list of users. 
    Add all the users who meets the criteria based on the attribute and attribute value to the pre existing list. 
    Then returns the list

    Parameters:
        users: list of user dictionary
            user:
                id: string
                name: string
                age: string
                occupation: string
        attribute: atrribute of a user to be checked which can be id, name, age, occupation
        attribute_value: value of the attribute that should match with a user to be added to a list
        return_list: list of users that have matched criterias so far

    Returns:
        a list of users that match the search attributes
    """
    for row in users:
        if attribute in row:
            match attribute:
                case 'id':
                    if search_user_match_id(row['id'], attribute_value) and row not in return_list:
                        return_list.append(row)
                case 'name':
                    if search_user_match_name(row['name'], attribute_value) and row not in return_list:
                        return_list.append(row)
                case 'age':
                    if search_user_match_age(row['age'], attribute_value) and row not in return_list:
                        return_list.append(row)
                case 'occupation':
                    if search_user_match_occupation(row['occupation'], attribute_value) and row not in return_list:
                        return_list.append(row)
    return return_list

def search_user_match_id(row_id, id):
    if id == None:
        return False 
    return row_id == id
    
def search_user_match_name(row_name, name):
    if name == None:
        return False 
    return name.lower() in row_name.lower()
    
def search_user_match_age(row_age: int, age: int):
    row_age = int(row_age)
    age = int(age)
    if age == None:
        return False 
    return (age == (row_age+1)) or  (age == (row_age-1)) or age == row_age

def search_user_match_occupation(row_occupation, occupation):
    if occupation == None:
        return False 
    return occupation.lower() in row_occupation.lower()
        