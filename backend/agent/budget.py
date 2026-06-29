def verify_budget(proposed_route: dict, total_budget: float) -> bool:
    total_cost = 0
    for day, details in proposed_route.items():
        if isinstance(details, dict):
            for activity in details.get("activities", []):
                try:
                    total_cost += float(activity.get("cost", 0))
                except (ValueError, TypeError):
                    pass
    
    return total_cost <= total_budget