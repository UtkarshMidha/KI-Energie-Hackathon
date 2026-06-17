class SubsidyService:

    def get_eligible_programs(self, payload, kb):

        programs = []

        try:
            federal = kb["incentives"]["federal"]

            for program in federal.get("programs", []):
                programs.append(
                    {
                        "program_id": program.get("program_id"),
                        "name": program.get("name")
                    }
                )

        except Exception:
            pass

        battery = payload.get(
            "battery_storage",
            False
        )

        if battery:

            programs.append(
                {
                    "program_id": "BATTERY_ELIGIBLE",
                    "name": "Battery Storage Eligible"
                }
            )

        return programs