from workflow_agents.base_agents import AugmentedPromptAgent
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
persona = "a college professor; your answers always start with: 'Dear students,'"

augmented_agent = AugmentedPromptAgent(openai_api_key, persona)
augmented_agent_response = augmented_agent.respond(prompt)

print(augmented_agent_response)

# The agent likely used the LLM's general knowledge about France,
# but the persona shaped the RESPONSE FORMAT to start with "Dear students,"
# This shows how system prompts control the style/tone without changing the factual content.
