from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class DecisionContext:
    """
    Raw request received from the UI.
    """

    user_input: str
    user_role: str = "USER"
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass
class Decision:
    """
    Standard decision object used across Sentinel.
    """

    risk_score: int
    risk_level: str
    decision: str
    risk_types: str
    impact: str
    opportunities: List[str]
    recommendations: List[str]
    policy_triggered: str
    audit_required: bool
    timestamp: datetime = field(default_factory=datetime.now)

    def to_dict(self):

        return {
            "risk_score": self.risk_score,
            "risk_level": self.risk_level,
            "decision": self.decision,
            "risk_types": self.risk_types,
            "impact": self.impact,
            "opportunities": self.opportunities,
            "recommendations": self.recommendations,
            "policy_triggered": self.policy_triggered,
            "audit_required": self.audit_required
        }
