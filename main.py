action = "READ_SENSITIVE_DATA"
approved = False

if action == "READ_SENSITIVE_DATA" and not approved:
    decision = "DENY"
    reason = "Approval missing"
else:
    decision = "ALLOW"
    reason = "Approved"

print("Action:", action)
print("Decision:", decision)
print("Reason:", reason)
