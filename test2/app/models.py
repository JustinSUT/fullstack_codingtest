# In-memory data store for product information
products = []

def get_next_id():
    return len(products) + 1
