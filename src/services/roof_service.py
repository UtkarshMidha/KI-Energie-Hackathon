from src.loaders.knowledge_loader import KnowledgeLoader


class RoofService:

    def assess(
        self,
        roof_area_m2,
        roof_type="gable",
        orientation="south",
        shading="none",
        state="lower_saxony"
    ):

        kb = KnowledgeLoader().load_all()

        roof_kb = kb["technical"]["roof_assessment"]

        # -----------------------------
        # Utilization Factor
        # -----------------------------

        utilization_factor = 0.8

        for rule in roof_kb["usable_area_rules"]:

            if rule["roof_type"] == roof_type:

                utilization_factor = rule[
                    "utilization_factor"
                ]

                break

        usable_area = round(
            roof_area_m2 * utilization_factor,
            2
        )

        # -----------------------------
        # Panel Data
        # -----------------------------

        panel_area = roof_kb[
            "capacity_estimation"
        ]["panel_area_m2"]

        panel_power_wp = roof_kb[
            "capacity_estimation"
        ]["panel_power_wp"]

        panel_count = int(
            usable_area / panel_area
        )

        estimated_kwp = round(
            (panel_count * panel_power_wp)
            / 1000,
            2
        )

        # -----------------------------
        # Regional Yield
        # -----------------------------

        region = roof_kb[
            "regional_mapping"
        ].get(
            state,
            "central_germany"
        )

        yield_factor = roof_kb[
            "yield_factors"
        ][region]

        annual_yield = int(
            estimated_kwp * yield_factor
        )

        # -----------------------------
        # Suitability Score
        # -----------------------------

        orientation_score = roof_kb[
            "orientation_scores"
        ].get(
            orientation,
            50
        )

        shading_score = roof_kb[
            "shading_scores"
        ].get(
            shading,
            50
        )

        total_score = int(
            (orientation_score +
             shading_score) / 2
        )

        classification = "unknown"

        for item in roof_kb[
            "suitability_classification"
        ]:

            if total_score >= item["score_min"]:

                classification = item[
                    "classification"
                ]

                break

        return {

            "roof_suitability_score":
                total_score,

            "classification":
                classification,

            "usable_area_m2":
                usable_area,

            "panel_count":
                panel_count,

            "estimated_kwp":
                estimated_kwp,

            "annual_yield_kwh":
                annual_yield,

            "orientation":
                orientation,

            "shading":
                shading
        }