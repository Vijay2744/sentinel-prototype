from rules import check_rule
from logger import log

action = "READ_SENSITIVE_DATA"
approved = False

decision, reason = check_rule(action, approved)

log(action, decision, reason)
