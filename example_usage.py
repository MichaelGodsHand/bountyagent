#!/usr/bin/env python3
"""
Example usage of the Bounty Suggestion Agent

This script shows how to integrate the bounty agent into your application
and demonstrates various usage patterns.
"""

import requests
import json
from typing import Dict, List, Any

class BountyAgentClient:
    """Client for interacting with the Bounty Suggestion Agent."""
    
    def __init__(self, agent_url: str = "http://localhost:8007"):
        self.agent_url = agent_url
        self.bounty_endpoint = f"{agent_url}/bounty/generate"
    
    def generate_bounties(self, brand_name: str) -> Dict[str, Any]:
        """
        Generate bounty suggestions for a brand.
        
        Args:
            brand_name: Name of the brand to generate bounties for
            
        Returns:
            Dictionary containing bounty suggestions and analysis
        """
        payload = {"brand_name": brand_name}
        
        try:
            response = requests.post(
                self.bounty_endpoint,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=60
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
                
        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "error": "Cannot connect to bounty agent. Make sure it's running."
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_bounty_summary(self, brand_name: str) -> str:
        """
        Get a summary of bounty suggestions for a brand.
        
        Args:
            brand_name: Name of the brand
            
        Returns:
            Formatted string summary of bounties
        """
        result = self.generate_bounties(brand_name)
        
        if not result.get("success"):
            return f"❌ Failed to generate bounties for {brand_name}: {result.get('error', 'Unknown error')}"
        
        bounties = result.get("bounties", [])
        analysis_summary = result.get("analysis_summary", "No analysis available")
        
        summary = f"🎯 Bounty Suggestions for {brand_name}\n"
        summary += f"📊 Analysis: {analysis_summary}\n"
        summary += f"🎁 Generated {len(bounties)} bounties:\n\n"
        
        for i, bounty in enumerate(bounties, 1):
            summary += f"{i}. {bounty.get('title', 'Untitled')}\n"
            summary += f"   Category: {bounty.get('category', 'Unknown')}\n"
            summary += f"   Difficulty: {bounty.get('difficulty', 'Unknown')}\n"
            summary += f"   Reward: {bounty.get('estimated_reward', 'Not specified')}\n\n"
        
        return summary
    
    def filter_bounties_by_category(self, brand_name: str, category: str) -> List[Dict[str, Any]]:
        """
        Get bounties filtered by category.
        
        Args:
            brand_name: Name of the brand
            category: Category to filter by (e.g., "Social Media", "Review")
            
        Returns:
            List of bounties matching the category
        """
        result = self.generate_bounties(brand_name)
        
        if not result.get("success"):
            return []
        
        bounties = result.get("bounties", [])
        return [bounty for bounty in bounties if bounty.get("category", "").lower() == category.lower()]
    
    def get_bounties_by_difficulty(self, brand_name: str, difficulty: str) -> List[Dict[str, Any]]:
        """
        Get bounties filtered by difficulty level.
        
        Args:
            brand_name: Name of the brand
            difficulty: Difficulty level ("Easy", "Medium", "Hard")
            
        Returns:
            List of bounties matching the difficulty
        """
        result = self.generate_bounties(brand_name)
        
        if not result.get("success"):
            return []
        
        bounties = result.get("bounties", [])
        return [bounty for bounty in bounties if bounty.get("difficulty", "").lower() == difficulty.lower()]

def example_basic_usage():
    """Example of basic bounty generation."""
    print("🎯 Basic Bounty Generation Example")
    print("=" * 50)
    
    client = BountyAgentClient()
    
    # Generate bounties for Tesla
    result = client.generate_bounties("Tesla")
    
    if result.get("success"):
        print("✅ Successfully generated bounties!")
        print(f"📊 Analysis: {result.get('analysis_summary', 'No analysis')}")
        print(f"🎁 Generated {len(result.get('bounties', []))} bounties")
        
        # Display first bounty as example
        bounties = result.get("bounties", [])
        if bounties:
            first_bounty = bounties[0]
            print(f"\n🏆 Example Bounty:")
            print(f"   Title: {first_bounty.get('title', 'N/A')}")
            print(f"   Description: {first_bounty.get('description', 'N/A')}")
            print(f"   Category: {first_bounty.get('category', 'N/A')}")
            print(f"   Difficulty: {first_bounty.get('difficulty', 'N/A')}")
            print(f"   Reward: {first_bounty.get('estimated_reward', 'N/A')}")
    else:
        print(f"❌ Failed: {result.get('error', 'Unknown error')}")

def example_filtered_usage():
    """Example of filtered bounty retrieval."""
    print("\n🎯 Filtered Bounty Retrieval Example")
    print("=" * 50)
    
    client = BountyAgentClient()
    
    # Get social media bounties for Apple
    social_bounties = client.filter_bounties_by_category("Apple", "Social Media")
    print(f"📱 Social Media bounties for Apple: {len(social_bounties)}")
    
    for bounty in social_bounties:
        print(f"   - {bounty.get('title', 'N/A')}")
    
    # Get easy bounties for Nike
    easy_bounties = client.get_bounties_by_difficulty("Nike", "Easy")
    print(f"\n⚡ Easy bounties for Nike: {len(easy_bounties)}")
    
    for bounty in easy_bounties:
        print(f"   - {bounty.get('title', 'N/A')}")

def example_summary_usage():
    """Example of getting bounty summaries."""
    print("\n🎯 Bounty Summary Example")
    print("=" * 50)
    
    client = BountyAgentClient()
    
    # Get summary for Starbucks
    summary = client.get_bounty_summary("Starbucks")
    print(summary)

def example_integration_pattern():
    """Example of how to integrate bounty generation into a larger system."""
    print("\n🎯 Integration Pattern Example")
    print("=" * 50)
    
    class LoyaltyProgramManager:
        """Example loyalty program manager that uses bounty suggestions."""
        
        def __init__(self):
            self.bounty_client = BountyAgentClient()
        
        def create_campaign(self, brand_name: str, campaign_type: str = "general"):
            """Create a loyalty campaign with bounty suggestions."""
            print(f"🚀 Creating {campaign_type} campaign for {brand_name}")
            
            # Get bounty suggestions
            result = self.bounty_client.generate_bounties(brand_name)
            
            if not result.get("success"):
                print(f"❌ Failed to get bounty suggestions: {result.get('error')}")
                return None
            
            bounties = result.get("bounties", [])
            analysis = result.get("analysis_summary", "")
            
            # Create campaign based on bounties
            campaign = {
                "brand": brand_name,
                "type": campaign_type,
                "analysis": analysis,
                "bounties": bounties,
                "total_bounties": len(bounties),
                "estimated_budget": self._calculate_budget(bounties)
            }
            
            print(f"✅ Campaign created with {len(bounties)} bounties")
            print(f"💰 Estimated budget: {campaign['estimated_budget']}")
            
            return campaign
        
        def _calculate_budget(self, bounties: List[Dict[str, Any]]) -> str:
            """Calculate estimated budget based on bounty rewards."""
            # Simple budget calculation - in real implementation, 
            # you'd parse the reward amounts and calculate totals
            return f"${len(bounties) * 50}-${len(bounties) * 200}"
    
    # Example usage
    manager = LoyaltyProgramManager()
    campaign = manager.create_campaign("Netflix", "engagement")
    
    if campaign:
        print(f"\n📋 Campaign Details:")
        print(f"   Brand: {campaign['brand']}")
        print(f"   Type: {campaign['type']}")
        print(f"   Bounties: {campaign['total_bounties']}")
        print(f"   Budget: {campaign['estimated_budget']}")

def main():
    """Run all examples."""
    print("🚀 Bounty Agent Usage Examples")
    print("=" * 60)
    
    try:
        example_basic_usage()
        example_filtered_usage()
        example_summary_usage()
        example_integration_pattern()
        
        print("\n🎉 All examples completed successfully!")
        print("\n💡 Tips for integration:")
        print("   - Always handle errors gracefully")
        print("   - Cache bounty suggestions to avoid repeated API calls")
        print("   - Filter bounties based on your program's needs")
        print("   - Consider implementing reward calculation logic")
        
    except Exception as e:
        print(f"❌ Error running examples: {e}")
        print("💡 Make sure the bounty agent is running on localhost:8007")

if __name__ == "__main__":
    main()
