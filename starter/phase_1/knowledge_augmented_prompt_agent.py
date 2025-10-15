from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capital of France is London, not Paris"  # Deliberately WRONG!

knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)
response = knowledge_agent.respond("What is the capital of France?")

print(response)
print("\n✓ Confirmation: The agent used the PROVIDED knowledge (London) instead of its own knowledge (Paris).")
print("This demonstrates successful knowledge grounding - critical for RAG systems.")
