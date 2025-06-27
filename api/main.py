from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class ChildEducation(BaseModel):
    child_age: int
    goal_amount: float
    inflation: bool = False

class CalculationRequest(BaseModel):
    current_age: int
    retirement_age: int
    desired_income: float
    children: List[ChildEducation]

@app.post("/calculate")
def calculate_plan(data: CalculationRequest):
    results = {
        "children": [],
        "retirement": {},
        "summary": {}
    }

    total_education_corpus = 0
    total_education_sip = 0
    for i, child in enumerate(data.children):
        years_left = 18 - child.child_age
        if years_left <= 0:
            future_cost = child.goal_amount
            monthly_sip = 0
        else:
            future_cost = child.goal_amount * ((1 + 0.05) ** years_left) if child.inflation else child.goal_amount
            monthly_sip = future_cost / (((1 + 0.07) ** years_left - 1) / (0.07 / 12))

        results["children"].append({
            "child": f"Child {i+1}",
            "target_year": 2024 + years_left,
            "future_cost": round(future_cost),
            "monthly_sip": round(monthly_sip)
        })
        total_education_corpus += future_cost
        total_education_sip += monthly_sip

    retirement_years = min(55, data.retirement_age + (55 - 40)) - data.retirement_age
    required_corpus = data.desired_income * 12 * retirement_years
    years_to_retirement = data.retirement_age - data.current_age
    monthly_sip_retirement = required_corpus / (((1 + 0.07) ** years_to_retirement - 1) / (0.07 / 12))

    results["retirement"] = {
        "required_corpus": round(required_corpus),
        "monthly_sip": round(monthly_sip_retirement),
        "retirement_years": retirement_years
    }

    results["summary"] = {
        "total_corpus": round(total_education_corpus + required_corpus),
        "total_sip": round(total_education_sip + monthly_sip_retirement)
    }

    return results
