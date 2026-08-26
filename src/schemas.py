LOGIN_SCHEMA = {
    "type": "object",
    "required": ["id", "username", "email", "accessToken", "refreshToken"],
    "properties": {
        "id": {"type": "integer", "minimum": 1},
        "username": {"type": "string", "minLength": 1},
        "email": {"type": "string", "pattern": "^[^@]+@[^@]+\\.[^@]+$"},
        "accessToken": {"type": "string", "minLength": 20},
        "refreshToken": {"type": "string", "minLength": 20},
    },
}

PRODUCT_LIST_SCHEMA = {
    "type": "object",
    "required": ["products", "total", "skip", "limit"],
    "properties": {
        "products": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "title", "price", "category"],
                "properties": {
                    "id": {"type": "integer"},
                    "title": {"type": "string"},
                    "price": {"type": "number", "minimum": 0},
                    "category": {"type": "string"},
                },
            },
        },
        "total": {"type": "integer", "minimum": 0},
        "skip": {"type": "integer", "minimum": 0},
        "limit": {"type": "integer", "minimum": 0},
    },
}
