def validate_not_empty(value):
    if not value.strip():
        raise ValueError("Value cannot be empty")
