def to_db_rows(api_users: list[dict]) -> list[tuple[int, str, str, str]]:
    return [(u["id"], u["email"], u["first_name"], u["last_name"]) for u in api_users]
