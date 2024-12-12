# Placeholder for future utility functions
def validate_product_data(data):
    if not data.get("name") or not data.get("price"):
        return False, "Product name and price are required"
    return True, None
