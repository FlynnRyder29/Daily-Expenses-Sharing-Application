def split_equal(total_amount, users):
    split_amount = total_amount / len(users)
    return {user: split_amount for user in users}

def split_exact(amounts):
    return amounts  # {user_id: amount}

def split_percentage(total_amount, percentages):
    assert sum(percentages.values()) == 100, "Percentages must add to 100%"
    return {user_id: (percent / 100) * total_amount for user_id, percent in percentages.items()}
