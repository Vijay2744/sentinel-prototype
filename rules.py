import json
from openai import OpenAI
import streamlit as st

from models import DecisionContext, Decision
from policy import evaluate_policy


SYSTEM_PROMPT = """
You are Sentinel Decision Intelligence Engine.

Your ONLY responsibility is to analyse business risk.

Return ONLY JSON in this format:

{
    "risk_score": 0,
    "risk_types": ["Operational"],
    "impact": "",
    "opportunities": [],
    "recommendations": []
}

Do NOT return risk level or decision.
"""


def evaluate_decision(context: DecisionContext) -> Decision:

    client = OpenAI(
        api_key=st.secrets["OPENAI_API_KEY"]
    )

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        response_format={
            "type": "json_object"
        },

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": context.user_input
            }
        ]
    )

    ai = json.loads(
        response.choices[0].message.content
    )

    risk_score = int(ai["risk_score"])

    policy = evaluate_policy(risk_score)

    return Decision(

        risk_score=risk_score,

        risk_level=policy["risk_level"],

        decision=policy["decision"],

        workflow=policy["workflow"],

        risk_types=ai.get("risk_types", []),

        impact=ai.get("impact", ""),

        opportunities=ai.get("opportunities", []),

        recommendations=ai.get("recommendations", []),

        policy_triggered=policy["policy_triggered"],

        audit_required=policy["audit_required"]

    )
