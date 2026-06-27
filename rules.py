from openai import OpenAI
import streamlit as st

from models import Decision
from policy import get_policy


SYSTEM_PROMPT = """
You are Sentinel Decision Intelligence Engine.

Your responsibility is ONLY to analyze the risk.

Return ONLY valid JSON.

{
    "risk_score": 0,
    "risk_types": "",
    "impact": "",
    "opportunities": [],
    "recommendations": []
}
"""


def evaluate_decision(user_input: str) -> Decision:

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
                "content": user_input
            }
        ]
    )

    import json

    ai = json.loads(
        response.choices[0].message.content
    )

    risk_score = int(ai["risk_score"])

    policy = get_policy(risk_score)

    return Decision(

        risk_score=risk_score,

        risk_level=policy["risk_level"],

        decision=policy["decision"],

        risk_types=ai["risk_types"],

        impact=ai["impact"],

        opportunities=ai["opportunities"],

        recommendations=ai["recommendations"],

        policy_triggered=policy["risk_level"],

        audit_required=policy["audit_required"]

    )
