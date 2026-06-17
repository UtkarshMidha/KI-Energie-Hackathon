from fastapi import APIRouter
from src.agents.legal_agent import LegalAgent
from src.loaders.knowledge_loader import KnowledgeLoader
from src.services.rule_engine import RuleEngine
from src.loaders.knowledge_loader import KnowledgeLoader
from src.services.roof_service import RoofService
from src.services.subsidy_service import SubsidyService
from src.services.cost_service import CostService
from src.services.recommendation_service import RecommendationService
from src.services.llm_service import LLMService



router = APIRouter()

@router.get("/test-llm")
def test_llm():

    response = LLMService().explain(
        {
            "test": "hello"
        }
    )

    return {
        "response": response
    }


@router.get('/health')
def health():
    return {'status': 'ok'}

@router.post('/analyze')
def analyze(payload: dict):
    return LegalAgent().analyze(payload)

@router.post("/advisor")
def advisor(payload: dict):

    
    kb = KnowledgeLoader().load_all()

    roof = RoofService().assess(

        roof_area_m2=payload.get(
            "roof_area_m2",
            100
        ),

        roof_type=payload.get(
            "roof_type",
            "gable"
        ),

        orientation=payload.get(
            "orientation",
            "south"
        ),

        shading=payload.get(
            "shading",
            "none"
        ),

        state="lower_saxony"
    )

    all_rules = []

    for file_name, file_data in kb["rules"].items():

        if "rules" in file_data:

            all_rules.extend(
                file_data["rules"]
            )

    print("RULE FILES FOUND:")

    for file_name in kb["rules"]:
        print("-", file_name)

    print("TOTAL RULES:", len(all_rules))


    evaluation_data = {}

    evaluation_data.update(payload)

    evaluation_data.update(roof)

    evaluation_data["pv_capacity_kw"] = roof["estimated_kwp"]

    legal_results = RuleEngine().evaluate(
        evaluation_data,
        all_rules
    )

    
    subsidies = SubsidyService().get_eligible_programs(
        payload,
        kb
    )

    financials = CostService().estimate(
        roof["estimated_kwp"]
    )

    recommendation = (
        RecommendationService()
        .generate(
            roof,
            legal_results,
            financials
        )
    )

    explanation = LLMService().explain(
        {
            "city": payload.get("city"),
            "roof_assessment": roof,
            "legal_results": legal_results,
            "eligible_programs": subsidies,
            "financials": financials,
            "recommendation": recommendation
        }
    )

    return {
        "city": payload.get("city"),
        "roof_assessment": roof,
        "legal_results": legal_results,
        "eligible_programs": subsidies,
        "financials": financials,
        "recommendation": recommendation,
        "report": explanation
    }

@router.get("/kb")
def get_kb():

    kb = KnowledgeLoader().load_all()

    return {
        "laws": list(kb["laws"].keys()),
        "rules": list(kb["rules"].keys()),
        "technical": list(kb["technical"].keys()),
        "incentives": list(kb["incentives"].keys())
    }

@router.post("/rules")
def run_rules(payload: dict):

    kb = KnowledgeLoader().load_all()

    rules = kb["rules"]["decision_rules"]["rules"]

    result = RuleEngine().evaluate(
        payload,
        rules
    )

    return result

@router.post("/roof")
def roof(payload: dict):

    result = RoofService().assess(
        roof_area_m2=payload["roof_area_m2"]
    )

    return result


@router.get("/debug")
def debug():

    kb = KnowledgeLoader().load_all()

    return {
        "laws": list(kb["laws"].keys()),
        "rules": list(kb["rules"].keys()),
        "technical": list(kb["technical"].keys())
    }
