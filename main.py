from rules import check_rule
from logger import log

actions = [
    {"action": "READ_SENSITIVE_DATA", "approved": False},
    {"action": "READ_SENSITIVE_DATA", "approved": True},
    {"action": "READ_PUBLIC_DATA", "approved": False}
]

for item in actions:
    action = item["action"]
    approved = item["approved"]

    decision, reason, risk = check_rule(action, approved)

    log(action, decision, reason, risk)
