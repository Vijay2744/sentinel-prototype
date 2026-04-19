from policy import POLICY

def check_rule(action, approved, role):

    rule = POLICY.get(action)

    if not rule:
        return "DENY", "Unknown action", "UNKNOWN"

    risk = rule["risk"]
    requires_approval = rule["requires_approval"]

    # Role-based restriction
    if role == "ANALYST" and risk in ["HIGH", "CRITICAL"]:
        return "DENY", "Role not allowed for high risk", risk

    # Low risk always allowed
    if risk == "LOW":
        return "ALLOW", "Low risk action", risk

    # Approval check
    if requires_approval and not approved:
        return "DENY", "Approval required", risk

    # Critical always blocked
    if risk == "CRITICAL":
        return "DENY", "Critical actions blocked", risk

    return "ALLOW", "Allowed by policy", risk
