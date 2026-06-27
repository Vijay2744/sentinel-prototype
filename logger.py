from datetime import datetime
from models import Decision


def log_decision(decision: Decision):

    print("\n================ SENTINEL AUDIT LOG ================")

    print(f"Timestamp         : {datetime.now()}")

    print(f"Risk Score        : {decision.risk_score}")

    print(f"Risk Level        : {decision.risk_level}")

    print(f"Decision          : {decision.decision}")

    print(f"Policy Triggered  : {decision.policy_triggered}")

    print(f"Audit Required    : {decision.audit_required}")

    print(f"Risk Types        : {decision.risk_types}")

    print(f"Impact            : {decision.impact}")

    print("====================================================\n")
