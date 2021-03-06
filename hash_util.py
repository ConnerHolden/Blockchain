import hashlib
import json


def hash_string_256(string):
    return hashlib.sha256(string).hexdigest()


# Hash generator
def hash_block(block):
    """Generate hash."""
    # Custom class objects are incompatible with json.
    hashable_block = block.__dict__.copy()
    hashable_block["transactions"] = [
        transaction.to_ordered_dict() for transaction in hashable_block["transactions"]
    ]
    # Create a string from <block> (dict) and encode it in UTF-8. Then generate
    # a byte hash using the sha256 algorithm from hashlib. Convert the byte
    # hash into a string with hexdigest().
    return hash_string_256(json.dumps(hashable_block, sort_keys=True).encode())
