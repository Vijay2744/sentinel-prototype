from rules import check_rule
from logger import log

print("Running Sentinel...\n")

actions = [
    {"action": "READ_SENSITIVE_DATA", "approved": False, "role": "ANALYST"},
    {"action": "READ_SENSITIVE_DATA", "approved": True, "role": "MANAGER"},
    {"action": "READ_PUBLIC_DATA", "approved": False, "role": "ANALYST"},
    {"action": "DELETE_DATA", "approved": True, "role": "ADMIN"}
]

for item in actions:

    result = check_rule(
        item["action"],
        item["approved"],
        item["role"]
    )

    log(result)
