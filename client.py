class GuidedShoppingDecisionEngineClient:
    def guide_decision(self, customer_preferences: dict, browsing_session: list) -> dict:
        size = customer_preferences.get("size", "M")
        fit = customer_preferences.get("fit_preference", "regular")
        style = customer_preferences.get("style", "casual")

        matches = [
            {
                "product_id": "PROD-8801",
                "title": "Tailored Everyday Linen Shirt",
                "match_score": 0.96,
                "fit_confidence": "HIGH (Fits True to Size)",
                "price_usd": 78.00
            },
            {
                "product_id": "PROD-8805",
                "title": "Relaxed Fit Chino Trousers",
                "match_score": 0.91,
                "fit_confidence": "HIGH",
                "price_usd": 92.00
            }
        ]

        return {
            "recommended_matches": matches,
            "return_risk_score": 0.05,
            "checkout_readiness": "HIGHLY_RECOMMENDED"
        }
