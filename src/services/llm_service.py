import os
from pathlib import Path

from openai import OpenAI


class LLMService:

    def __init__(self):

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY not found in environment"
            )

        self.client = OpenAI(
            api_key=api_key
        )

        self.system_prompt = self._load_prompt()

    def _load_prompt(self):

        prompt_file = Path(
            "knowledge_base/prompts/legal_reasoning.md"
        )

        if prompt_file.exists():
            return prompt_file.read_text(
                encoding="utf-8"
            )

        return """
You are an expert German photovoltaic consultant.

You specialize in:

- German PV regulations
- EEG
- EnWG
- MsbG
- Lower Saxony building law (NBauO)
- Feed-in tariffs
- Smart metering
- Grid connection
- Residential rooftop PV systems

Provide practical, legally aware recommendations.

Never invent subsidies or legal requirements.
Always explain assumptions.
"""

    def explain(self, advisor_result):

        user_prompt = f"""
Create a professional PV Feasibility Report.

Use the following structure exactly:

# PV Feasibility Report

## Executive Summary

Provide a short overview.

## Legal Status

Explain whether installation appears legally feasible.

## Roof Assessment

Summarize roof suitability.

## System Recommendation

Recommended PV size and battery recommendation.

## Energy Production

Expected annual production and self-consumption implications.

## Financial Analysis

Include:
- estimated installation cost
- annual savings
- payback period

## Incentives and Subsidies

List eligible programs.

## Recommended Next Steps

Provide a numbered action plan.

## Conclusion

Give a final recommendation.

Analysis Data:

{advisor_result}
"""

        response = self.client.chat.completions.create(
            model="gpt-5.4-mini",
            temperature=0.2,
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        return response.choices[0].message.content

    def summarize(self, advisor_result):

        response = self.client.chat.completions.create(
            model="gpt-5.4-mini",
            temperature=0.1,
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content":
                    f"""
Summarize this PV assessment in less than 150 words.

Data:

{advisor_result}
"""
                }
            ]
        )

        return response.choices[0].message.content