"""
Sentinel Enterprise Policy Repository
"""

POLICY_MATRIX = {

    "LOW": {
        "min_score": 0,
        "max_score": 30,
        "decision": "APPROVE",
        "workflow": "STP",
        "audit_required": False
    },

    "MEDIUM": {
        "min_score": 31,
        "max_score": 60,
        "decision": "REVIEW",
        "workflow": "BUSINESS_REVIEW",
        "audit_required": False
    },

    "HIGH": {
        "min_score": 61,
        "max_score": 85,
        "decision": "ESCALATE",
        "workflow": "HUMAN_REVIEW",
        "audit_required": True
    },

    "CRITICAL": {
        "min_score": 86,
        "max_score": 100,
        "decision": "REJECT",
        "workflow": "BLOCKED",
        "audit_required": True
    }

}


def evaluate_policy(risk_score: int):

    for risk_level, config in POLICY_MATRIX.items():

        if config["min_score"] <= risk_score <= config["max_score"]:

            return {

                "risk_level": risk_level,

                "decision": config["decision"],

                "workflow": config["workflow"],

                "audit_required": config["audit_required"],

                "policy_triggered": f"{risk_level}_RISK_POLICY"

            }

    return {

        "risk_level": "UNKNOWN",

        "decision": "REVIEW",

        "workflow": "HUMAN_REVIEW",

        "audit_required": True,

        "policy_triggered": "DEFAULT_POLICY"

    }
