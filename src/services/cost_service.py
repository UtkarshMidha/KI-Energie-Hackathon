class CostService:

    def estimate(
        self,
        estimated_kwp
    ):

        cost_per_kwp = 1300

        annual_yield_factor = 950

        electricity_price = 0.30

        installation_cost = (
            estimated_kwp
            * cost_per_kwp
        )

        annual_yield = (
            estimated_kwp
            * annual_yield_factor
        )

        annual_savings = (
            annual_yield
            * electricity_price
        )

        payback = (
            installation_cost
            / annual_savings
        )

        return {

            "estimated_cost_eur":
                round(
                    installation_cost
                ),

            "annual_savings_eur":
                round(
                    annual_savings
                ),

            "payback_years":
                round(
                    payback,
                    1
                )
        }