def verify_budget(proposed_route: dict, total_budget: float) -> bool:
    total_cost = 0
    for day, details in proposed_route.items():
        for activity in details.get("activities", []):
            total_cost += activity.get("cost", 0)
    
    return total_cost <= total_budget