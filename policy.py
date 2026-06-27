"""
Sentinel Core Policy Repository

This file contains enterprise policies that determine
how Sentinel classifies and routes decisions.
"""

POLICY = {

    "LOW": {
        "score_min": 0,
        "score_max": 30,
        "decision": "APPROVE",
        "audit_required": False
    },

    "MEDIUM": {
        "score_min": 31,
        "score_max": 60,
        "decision": "REVIEW",
        "audit_required": False
    },

    "HIGH": {
        "score_min": 61,
        "score_max": 85,
        "decision": "ESCALATE",
        "audit_required": True
    },

    "CRITICAL": {
        "score_min": 86,
        "score_max": 100,
        "decision": "REJECT",
        "audit_required": True
    }

}


def get_policy(risk_score: int):
    """
    Returns the applicable enterprise policy
    based on the calculated risk score.
    """

    for level, config in POLICY.items():

        if config["score_min"] <= risk_score <= config["score_max"]:

            return {
                "risk_level": level,
                "decision": config["decision"],
                "audit_required": config["audit_required"]
            }

    return {
        "risk_level": "UNKNOWN",
        "decision": "REVIEW",
        "audit_required": True
    }
