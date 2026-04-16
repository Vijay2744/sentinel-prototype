def check_rule(action, approved):

    # Define risk levels
    risk_levels = {
        "READ_PUBLIC_DATA": "LOW",
        "READ_SENSITIVE_DATA": "HIGH",
        "DELETE_DATA": "CRITICAL"
    }

    risk = risk_levels.get(action, "UNKNOWN")

    # Decision logic based on risk
    if risk == "LOW":
        return "ALLOW", "Low risk action", risk

    elif risk == "HIGH":
        if not approved:
            return "DENY", "High risk requires approval", risk
        return "ALLOW", "Approved high risk action", risk

    elif risk == "CRITICAL":
        return "DENY", "Critical actions are blocked", risk

    else:
        return "DENY", "Unknown action", risk
