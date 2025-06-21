from pydantic import BaseModel, Field
from typing import List, Optional
from guardrails import Guard

class TravelRecommendation(BaseModel):
    destination: str = Field(..., description="City or place name of the recommended destination")
    country: str = Field(..., description="Country where the destination is located")
    region: Optional[str] = Field(None, description="Geographical region or area")

    reason: str = Field(..., description="Summary of why this destination is recommended")

    activities: List[str] = Field(..., description="List of suggested activities or attractions at the destination")

    estimated_budget_usd: Optional[float] = Field(None, description="Approximate travel budget in USD")

    best_season: Optional[str] = Field(None, description="Best season or time of year to visit")
    traveler_type: Optional[str] = Field(
        None,
        description="Best suited traveler type (e.g., solo, family, adventure, romantic, senior)"
    )

    travel_advice: Optional[str] = Field(
        None,
        description="Any important travel advisories, health tips, or local customs to know"
    )

class StructuredGuardFactory:
    @staticmethod
    def travel_recommendation_guard():
        return Guard.for_pydantic(output_class=TravelRecommendation)
