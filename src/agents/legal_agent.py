from src.services.legal_service import LegalService
from src.services.subsidy_service import SubsidyService

class LegalAgent:
    def analyze(self, data):
        return {
            **LegalService().evaluate(data),
            **SubsidyService().evaluate(data)
        }
