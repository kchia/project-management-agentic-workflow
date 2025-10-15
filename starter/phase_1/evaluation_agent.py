from workflow_agents.base_agents import EvaluationAgent, KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"

# Worker agent with wrong knowledge and verbose persona
persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capitol of France is London, not Paris"
knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

# Evaluation agent that enforces concise format
persona_eval = "You are an evaluation agent that checks the answers of other worker agents"
evaluation_criteria = "The answer should be solely the name of a city, not a sentence."
evaluation_agent = EvaluationAgent(
    openai_api_key,
    persona_eval,
    evaluation_criteria,
    knowledge_agent,
    max_interactions=10
)

# Watch it iteratively refine!
result = evaluation_agent.evaluate(prompt)
print("\n=== FINAL RESULT ===")
print(result)
