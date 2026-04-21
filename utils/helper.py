def auto_priority(deadline):
    if "today" in deadline.lower():
        return "high"
    elif "tomorrow" in deadline.lower():
        return "medium"
    else:
        return "low"
