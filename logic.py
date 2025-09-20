import json

with open("product_docs.json", "r") as f:
    PRODUCT_DOCS = json.load(f)

def map_to_ticket_fields(data: dict) -> dict:
    return {
        "user_name": data.get("name", "Unknown"),
        "email": data.get("contact", {}).get("email", "unknown@example.com"),
        "issue_type": data.get("issue", {}).get("type", "general"),
        "description": data.get("issue", {}).get("description", ""),
    }

def get_product_info(data: dict) -> str:
    product = data.get("product", "").lower()
    query = data.get("question", "").lower()

    doc = PRODUCT_DOCS.get(product)
    if not doc:
        return f"No documentation found for product: {product}"

    for key, value in doc.items():
        if query in key.lower() or query in value.lower():
            return f"{key}: {value}"

    return "No matching info found in documentation."
