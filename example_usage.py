from client import GuidedShoppingDecisionEngineClient

def main():
    client = GuidedShoppingDecisionEngineClient()
    res = client.guide_decision(
        customer_preferences={"size": "L", "fit_preference": "slim", "style": "smart casual"},
        browsing_session=["viewed_shirts", "compared_sizing_chart", "filtered_color_navy"]
    )
    print(f"Checkout Readiness: {res['checkout_readiness']}")
    print(f"Return Risk Score: {res['return_risk_score']*100}% (Extremely Low)")
    print("Guided Matches:")
    for match in res["recommended_matches"]:
        print(f"  [{match['product_id']}] {match['title']} - ${match['price_usd']} | Fit: {match['fit_confidence']}")

if __name__ == "__main__":
    main()
