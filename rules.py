def check_rule(action, approved):
    if action == "READ_SENSITIVE_DATA" and not approved:
        return "DENY", "Approval missing"
    return "ALLOW", "Approved"
