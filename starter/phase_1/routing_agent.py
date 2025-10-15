from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent, RoutingAgent
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

persona = "You are a college professor"

# Create specialized agents
knowledge_texas = "You know everything about Texas"
texas_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge_texas)

knowledge_europe = "You know everything about Europe"
europe_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge_europe)

persona_math = "You are a college math professor"
knowledge_math = "You know everything about math, you take prompts with numbers, extract math formulas, and show the answer without explanation"
math_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_math, knowledge_math)

# Create router with agent definitions
routing_agent = RoutingAgent(openai_api_key, {})
agents = [
    {
        "name": "texas agent",
        "description": "Answer a question about Texas",
        "func": lambda x: texas_agent.respond(x)
    },
    {
        "name": "europe agent",
        "description": "Answer a question about Europe",
        "func": lambda x: europe_agent.respond(x)
    },
    {
        "name": "math agent",
        "description": "When a prompt contains numbers, respond with a math formula",
        "func": lambda x: math_agent.respond(x)
    }
]
routing_agent.agents = agents

# Test routing
print("=== Test 1: Rome, Texas ===")
print(routing_agent.route("Tell me about the history of Rome, Texas"))

print("\n=== Test 2: Rome, Italy ===")
print(routing_agent.route("Tell me about the history of Rome, Italy"))

print("\n=== Test 3: Math Problem ===")
print(routing_agent.route("One story takes 2 days, and there are 20 stories"))
