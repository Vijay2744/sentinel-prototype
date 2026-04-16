from rules import check_rule

action = "READ_SENSITIVE_DATA"
approved = False

decision, reason = check_rule(action, approved)

print("Action:", action)
print("Decision:", decision)
print("Reason:", reason)
