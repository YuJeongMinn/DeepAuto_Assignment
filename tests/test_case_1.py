code = """
def process_user_input(user_data):
    query = f"SELECT * FROM users WHERE id = {user_data['id']}"
    buffer = [0] * 10
    for i in range(len(user_data['items'])):
        buffer[i] = user_data['items'][i]
    return query, buffer
"""