#!/usr/bin/env python3
"""
Test script for the Bounty Suggestion Agent

This script demonstrates how to interact with the bounty agent
and test its functionality.
"""

import requests
import json
import time
import sys
from typing import Dict, Any

class BountyAgentTester:
    def __init__(self, agent_url: str = "http://localhost:8007"):
        self.agent_url = agent_url
        self.bounty_endpoint = f"{agent_url}/bounty/generate"
    
    def test_bounty_generation(self, brand_name: str) -> Dict[str, Any]:
        """Test bounty generation for a specific brand."""
        print(f"🧪 Testing bounty generation for brand: {brand_name}")
        print(f"🌐 Endpoint: {self.bounty_endpoint}")
        
        payload = {"brand_name": brand_name}
        
        try:
            print("📤 Sending request...")
            response = requests.post(
                self.bounty_endpoint,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=60
            )
            
            print(f"📡 Response status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print("✅ Successfully received bounty suggestions!")
                return data
            else:
                print(f"❌ Error response: {response.text}")
                return {"success": False, "error": response.text}
                
        except requests.exceptions.ConnectionError:
            print("❌ Connection error: Make sure the bounty agent is running on localhost:8007")
            return {"success": False, "error": "Connection failed"}
        except requests.exceptions.Timeout:
            print("❌ Request timeout: The agent took too long to respond")
            return {"success": False, "error": "Request timeout"}
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return {"success": False, "error": str(e)}
    
    def display_bounty_results(self, result: Dict[str, Any]):
        """Display bounty generation results in a formatted way."""
        if not result.get("success"):
            print(f"❌ Bounty generation failed: {result.get('error', 'Unknown error')}")
            return
        
        brand_name = result.get("brand_name", "Unknown Brand")
        bounties = result.get("bounties", [])
        analysis_summary = result.get("analysis_summary", "No analysis available")
        
        print(f"\n🎯 BOUNTY SUGGESTIONS FOR {brand_name.upper()}")
        print("=" * 60)
        print(f"📊 Analysis Summary: {analysis_summary}")
        print(f"🎁 Generated {len(bounties)} bounties")
        print("=" * 60)
        
        for i, bounty in enumerate(bounties, 1):
            print(f"\n🏆 BOUNTY #{i}: {bounty.get('title', 'Untitled')}")
            print(f"   📝 Description: {bounty.get('description', 'No description')}")
            print(f"   🏷️  Category: {bounty.get('category', 'Unknown')}")
            print(f"   ⚡ Difficulty: {bounty.get('difficulty', 'Unknown')}")
            print(f"   💰 Reward: {bounty.get('estimated_reward', 'Not specified')}")
            print(f"   👥 Target: {bounty.get('target_audience', 'All users')}")
            print(f"   📈 Success Metrics: {', '.join(bounty.get('success_metrics', []))}")
            print("-" * 40)
    
    def test_multiple_brands(self, brands: list):
        """Test bounty generation for multiple brands."""
        print(f"🧪 Testing bounty generation for {len(brands)} brands")
        print("=" * 60)
        
        results = {}
        for brand in brands:
            print(f"\n🔄 Testing brand: {brand}")
            result = self.test_bounty_generation(brand)
            results[brand] = result
            
            if result.get("success"):
                print(f"✅ Successfully generated bounties for {brand}")
            else:
                print(f"❌ Failed to generate bounties for {brand}")
            
            # Add delay between requests
            time.sleep(2)
        
        return results
    
    def check_agent_status(self) -> bool:
        """Check if the bounty agent is running and accessible."""
        try:
            # Try to make a simple request to check if the agent is running
            response = requests.get(f"{self.agent_url}/", timeout=5)
            return True
        except:
            return False

def main():
    """Main test function."""
    print("🚀 Bounty Agent Tester")
    print("=" * 40)
    
    tester = BountyAgentTester()
    
    # Check if agent is running
    print("🔍 Checking if bounty agent is running...")
    if not tester.check_agent_status():
        print("❌ Bounty agent is not running or not accessible")
        print("💡 Make sure to start the bounty agent first:")
        print("   python agent.py")
        sys.exit(1)
    
    print("✅ Bounty agent is running and accessible")
    
    # Test with different brands
    test_brands = [
        "Tesla",
        "Apple", 
        "Nike",
        "Starbucks",
        "Netflix"
    ]
    
    print(f"\n🧪 Testing with brands: {', '.join(test_brands)}")
    
    # Test single brand first
    print("\n" + "="*60)
    print("🎯 SINGLE BRAND TEST")
    print("="*60)
    
    result = tester.test_bounty_generation("Tesla")
    tester.display_bounty_results(result)
    
    # Ask user if they want to test more brands
    print("\n" + "="*60)
    response = input("🤔 Would you like to test more brands? (y/n): ").lower().strip()
    
    if response in ['y', 'yes']:
        print("\n🎯 MULTIPLE BRANDS TEST")
        print("="*60)
        
        # Test multiple brands
        results = tester.test_multiple_brands(test_brands)
        
        # Summary
        print("\n📊 TEST SUMMARY")
        print("="*60)
        successful = sum(1 for r in results.values() if r.get("success"))
        total = len(results)
        
        print(f"✅ Successful: {successful}/{total}")
        print(f"❌ Failed: {total - successful}/{total}")
        
        for brand, result in results.items():
            status = "✅" if result.get("success") else "❌"
            bounty_count = len(result.get("bounties", []))
            print(f"   {status} {brand}: {bounty_count} bounties generated")
    
    print("\n🎉 Testing completed!")
    print("💡 You can also test the agent via:")
    print("   - REST API: POST http://localhost:8007/bounty/generate")
    print("   - Chat interface: Connect via Agentverse")

if __name__ == "__main__":
    main()
