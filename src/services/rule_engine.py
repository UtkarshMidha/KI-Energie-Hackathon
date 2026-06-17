class RuleEngine:

    def check_condition(self, value, condition):

        if value is None:
            return False

        if isinstance(condition, dict):

            if "gt" in condition:
                return value > condition["gt"]

            if "gte" in condition:
                return value >= condition["gte"]

            if "lt" in condition:
                return value < condition["lt"]

            if "lte" in condition:
                return value <= condition["lte"]

            if "in" in condition:
                return value in condition["in"]

        return value == condition

    def evaluate(self, user_data, rules):

        results = []

        for rule in rules:

            conditions = rule.get("if", {})

            match = True

            for key, expected in conditions.items():

                actual = user_data.get(key)

                if not self.check_condition(
                    actual,
                    expected
                ):
                    match = False
                    break

            if not match:
                continue

            result_payload = (
                rule.get("then")
                or rule.get("eligible_for")
                or rule.get("recommendation")
                or rule.get("classification")
            )

            if result_payload is None:
                continue

            results.append(
                {
                    "rule_id": rule.get("rule_id"),
                    "result": result_payload
                }
            )

        return results