from rules import check_rule
from logger import log

# Simulated AI actions
actions = [
    {"action": "READ_SENSITIVE_DATA", "approved": False},
    {"action": "READ_SENSITIVE_DATA", "approved": True},
    {"action": "READ_PUBLIC_DATA", "approved": False}
]

for item in actions:
    action = item["action"]
    approved = item["approved"]

    decision, reason = check_rule(action, approved)
    log(action, decision, reason)
