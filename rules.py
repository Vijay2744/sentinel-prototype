def check_rule(action, approved, role):

    rule = POLICY.get(action)

    if not rule:
        return "DENY", "Unknown action", "UNKNOWN"

    risk = rule["risk"]
    requires_approval = rule["requires_approval"]

    # Role-based restriction
    if role == "ANALYST" and risk in ["HIGH", "CRITICAL"]:
        return "DENY", "Role not allowed for high risk", risk

    if risk == "LOW":
        return "ALLOW", "Low risk action", risk

    if requires_approval and not approved:
        return "DENY", "Approval required", risk

    if risk == "CRITICAL":
        return "DENY", "Critical actions blocked", risk

    return "ALLOW", "Allowed by policy", risk
