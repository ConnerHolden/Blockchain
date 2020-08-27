import hashlib
import json


def hash_string_256(string):
    return hashlib.sha256(string).hexdigest()


# Hash generator
def hash_block(block):
    """ Generate hash.
    """
    # Create a string from <block> (dict) and encode it in UTF-8. Then generate a byte
    # hash using the sha256 algorithm from hashlib. Convert the byte hash into a string
    # with hexdigest().
    return hash_string_256(json.dumps(block, sort_keys=True).encode())
