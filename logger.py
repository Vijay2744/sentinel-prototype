from datetime import datetime
from uuid import uuid4

from models import Decision


def log_decision(decision: Decision):

    audit_id = str(uuid4())[:8]

    print("\n==============================================")
    print("         SENTINEL AUDIT LOG")
    print("==============================================")

    print(f"Audit ID          : {audit_id}")
    print(f"Timestamp         : {datetime.now()}")

    print("----------------------------------------------")

    print(f"Risk Score        : {decision.risk_score}")
    print(f"Risk Level        : {decision.risk_level}")
    print(f"Decision          : {decision.decision}")
    print(f"Workflow          : {decision.workflow}")

    print("----------------------------------------------")

    print(f"Policy Triggered  : {decision.policy_triggered}")
    print(f"Audit Required    : {decision.audit_required}")

    print("----------------------------------------------")

    print(f"Risk Types        : {', '.join(decision.risk_types)}")
    print(f"Impact            : {decision.impact}")

    print("==============================================\n")

    return audit_id
