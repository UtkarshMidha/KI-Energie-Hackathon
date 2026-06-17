class RecommendationService:

    def generate(
        self,
        roof,
        legal,
        financial
    ):

        battery = (
            roof["estimated_kwp"]
            >= 8
        )

        return {

            "legal_status":
                "allowed",

            "roof_suitability":
                "excellent",

            "recommended_pv_size":
                f"{roof['estimated_kwp']} kWp",

            "battery_recommended":
                battery,

            "estimated_payback":
                f"{financial['payback_years']} years",

            "next_steps": [

                "Request grid connection",

                "Select PV installer",

                "Register in Marktstammdatenregister",

                "Apply for incentives",

                "Install smart meter if required"
            ]
        }