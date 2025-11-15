destinations = [
    {
        "name": "Paris",
        "budget": "high",
        "weather": "hot",
        "activities": ["cultural", "sightseeing", "museums"]
    },
    {
        "name": "Bali",
        "budget": "medium",
        "weather": "moderate",
        "activities": ["relaxation", "beach", "surfing"]
    },
    {
        "name": "Switzerland",
        "budget": "high",
        "weather": "cold",
        "activities": ["adventure", "skiing", "hiking"]
    },
    {
        "name": "Thailand",
        "budget": "low",
        "weather": "moderate",
        "activities": ["relaxation", "adventure", "beach"]
    },
    {
        "name": "New York",
        "budget": "high",
        "weather": "hot",
        "activities": ["cultural", "sightseeing", "shopping"]
    },
    {
        "name": "Dubai",
        "budget": "high",
        "weather": "hot",
        "activities": ["adventure", "hiking", "northern_lights"]
    }
]
def similarity_score(user_pref, destination):
    score = 0
    if user_pref["budget"].lower() == destination["budget"].lower():
        score += 1
    if user_pref["weather"].lower() == destination["weather"].lower():
        score += 1
    activity_matches = set(user_pref["activities"]).intersection(set(destination["activities"]))
    score += len(activity_matches)
    return score

def recommend_destinations(user_pref, top_n=2):
    scores = []
    for dest in destinations:
        score = similarity_score(user_pref, dest)
        scores.append((dest["name"], score))
    
    
    scores.sort(key=lambda x: x[1], reverse=True)
    
    
    recommended = [name for name, score in scores[:top_n]]
    return recommended


print("Welcome to the Travel Recommendation System!")
budget = input("Enter your budget (low, medium, high): ").strip().lower()
weather = input("Preferred weather (moderate, hot, cold): ").strip().lower()
activities = input("Enter preferred activities (comma-separated, e.g., adventure, beach, cultural): ")


activities_list = [act.strip().lower() for act in activities.split(",")]

user_pref = {
    "budget": budget,
    "weather": weather,
    "activities": activities_list
}

recommendations = recommend_destinations(user_pref, top_n=3)

print("\nRecommended travel destinations for you:")
for dest in recommendations:
    print("-", dest)
