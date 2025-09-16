# Bounty Suggestion Agent

A sophisticated AI agent that analyzes brand performance data and generates targeted bounty suggestions for loyalty program members. This agent integrates with the brand-research-agent to fetch comprehensive brand metrics and uses AI reasoning to create actionable bounties that address specific brand weaknesses.

## 🤖 What This Agent Does

This agent connects to your brand research system and provides intelligent bounty suggestions by:

- **Brand Analysis**: Fetches comprehensive brand data from the brand-research-agent
- **Weakness Identification**: Analyzes brand performance across multiple platforms (reviews, Reddit, social media)
- **Bounty Generation**: Creates 6 targeted bounties that address specific brand weaknesses
- **Structured Output**: Provides detailed bounty information including difficulty, rewards, and success metrics

## 🔗 Integration Architecture

The agent integrates with your existing brand research infrastructure:

- **Brand Research Agent**: `http://localhost:8006/brand/summary` - Fetches comprehensive brand data
- **Knowledge Graph**: Uses structured data from MeTTa knowledge graph
- **ASI:One AI**: Powers intelligent analysis and bounty generation

## 🏗️ Project Architecture

### Core Components

1. **`agent.py`**: Main uAgent implementation with REST API and Chat Protocol
2. **Brand Data Integration**: Fetches data from brand-research-agent
3. **AI Analysis Engine**: Uses ASI:One to analyze weaknesses and generate bounties
4. **Structured Output**: Returns detailed bounty suggestions with metrics

### Data Flow

Brand Name → Brand Research Agent → Brand Data → Weakness Analysis → Bounty Generation → Structured Response

## 🚀 Setup Instructions

### Prerequisites

- Python 3.11+
- ASI:One API key
- AGENTVERSE_API_KEY
- Brand-research-agent running on localhost:8006

### Installation

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   cp env.example .env
   # Edit .env with your ASI:One API key and AGENTVERSE_API_KEY
   ```

4. **Ensure brand-research-agent is running**:
   ```bash
   # In another terminal, start the brand research agent
   cd ../brand-research-agent
   python agent.py
   ```

5. **Run the bounty agent**:
   ```bash
   python agent.py
   ```

## 🧪 Testing the Agent

### REST API Testing (Postman/curl)

1. **Start the agent**:
   ```bash
   python agent.py
   ```

2. **Test bounty generation**:
   ```bash
   curl -X POST http://localhost:8007/bounty/generate \
     -H "Content-Type: application/json" \
     -d '{"brand_name": "Tesla"}'
   ```

   **Expected Response**:
   ```json
   {
     "success": true,
     "brand_name": "Tesla",
     "bounties": [
       {
         "title": "Share Your Tesla Experience",
         "description": "Post about your Tesla driving experience on social media",
         "category": "Social Media",
         "difficulty": "Easy",
         "estimated_reward": "50 points",
         "target_audience": "Tesla owners",
         "success_metrics": ["Social media post created", "Hashtag used", "Positive sentiment"]
       },
       // ... 5 more bounties
     ],
     "analysis_summary": "Identified 3 key weaknesses: Customer service, Charging infrastructure, Pricing",
     "timestamp": "2024-01-15T10:30:00Z",
     "agent_address": "agent1q..."
   }
   ```

### Chat Interface Testing

1. **Access the inspector**:
   Visit the URL shown in the console and connect via Mailbox

2. **Test queries**:
   - "generate bounties for Tesla"
   - "bounties for Apple"
   - "create bounties for Nike"

## 🔧 Key Features

### 1. **Intelligent Brand Analysis**
The agent analyzes comprehensive brand data:
```python
# Fetches data from brand-research-agent
brand_data = get_brand_data_from_research_agent(brand_name)

# Analyzes weaknesses using AI
analysis = analyze_brand_weaknesses(brand_data, brand_name, llm)
```

### 2. **Targeted Bounty Generation**
Creates bounties that address specific weaknesses:
- **Social Media**: Address negative sentiment
- **Reviews**: Improve online reputation
- **Content Creation**: Boost brand awareness
- **Community Building**: Strengthen customer loyalty
- **Product Testing**: Gather feedback
- **Referrals**: Expand customer base

### 3. **Structured Bounty Format**
Each bounty includes:
- **Title**: Engaging, actionable title
- **Description**: Detailed task description
- **Category**: Type of bounty (Social Media, Review, etc.)
- **Difficulty**: Easy, Medium, or Hard
- **Estimated Reward**: Points or monetary value
- **Target Audience**: Who should complete this bounty
- **Success Metrics**: How to measure completion

### 4. **Fallback Mechanisms**
- **Graceful Degradation**: Works even if brand data is limited
- **Fallback Bounties**: Generates generic bounties if AI fails
- **Error Handling**: Provides meaningful error messages

## 📋 Example Bounty Categories

### Social Media Bounties
- "Share Your [Brand] Experience"
- "Create [Brand] Content"
- "Join [Brand] Community"

### Review Bounties
- "Write a [Brand] Review"
- "Rate [Brand] Products"
- "Share Product Photos"

### Community Bounties
- "Refer a Friend"
- "Join Discussion Forums"
- "Participate in Surveys"

### Content Creation Bounties
- "Create Tutorial Videos"
- "Write Blog Posts"
- "Design Social Media Content"

### Product Testing Bounties
- "Beta Test New Features"
- "Provide Product Feedback"
- "Test Mobile App"

## 🔄 Integration Points

### Brand Research Agent Integration
```python
# Fetches comprehensive brand data
url = "http://localhost:8006/brand/summary"
payload = {"brand_name": brand_name}
response = requests.post(url, json=payload)
```

### Knowledge Graph Integration
- Uses MeTTa knowledge graph for structured reasoning
- Integrates with existing brand research data
- Maintains consistency with brand analysis framework

## 📊 Bounty Generation Process

1. **Data Collection**: Fetches brand data from research agent
2. **Weakness Analysis**: Identifies key areas for improvement
3. **Bounty Creation**: Generates 6 targeted bounties
4. **Structured Output**: Returns detailed bounty information
5. **Fallback Handling**: Provides alternatives if generation fails

## 🔗 Useful Links

- [uAgents Documentation](https://innovationlab.fetch.ai/resources/docs/examples/chat-protocol/asi-compatible-uagents)
- [ASI:One](https://asi1.ai/)
- [MeTTa Knowledge Graph](https://metta-lang.dev/)
- [Agentverse](https://agentverse.ai/)

## 🚨 Troubleshooting

### Common Issues

1. **Brand Research Agent Not Running**:
   - Ensure brand-research-agent is running on localhost:8006
   - Check that the agent is accessible and responding

2. **No Brand Data Found**:
   - Verify the brand exists in the knowledge graph
   - Check that the brand-research-agent has data for the requested brand

3. **API Key Issues**:
   - Ensure ASI_ONE_API_KEY is set correctly
   - Verify AGENTVERSE_API_KEY is configured

4. **Port Conflicts**:
   - Change the port in agent.py if 8007 is already in use
   - Update the endpoint configuration accordingly

### Debug Mode

Enable debug logging by checking the console output for detailed information about:
- Brand data fetching
- Weakness analysis
- Bounty generation process
- Error handling

## 📈 Future Enhancements

- **Dynamic Reward Calculation**: Calculate rewards based on brand budget
- **A/B Testing**: Test different bounty types for effectiveness
- **Performance Tracking**: Monitor bounty completion rates
- **Personalization**: Tailor bounties to individual user preferences
- **Integration with Loyalty Platforms**: Direct integration with existing loyalty systems
