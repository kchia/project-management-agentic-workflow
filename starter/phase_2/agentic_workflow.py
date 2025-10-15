# agentic_workflow.py

# TODO: 1 - Import the following agents: ActionPlanningAgent, KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent from the workflow_agents.base_agents module
from workflow_agents.base_agents import (
    ActionPlanningAgent,
    KnowledgeAugmentedPromptAgent,
    EvaluationAgent,
    RoutingAgent
)

import os
from dotenv import load_dotenv

# TODO: 2 - Load the OpenAI key into a variable called openai_api_key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# load the product spec
# TODO: 3 - Load the product spec document Product-Spec-Email-Router.txt into a variable called product_spec
with open("workflow_agents/Product-Spec-Email-Router.txt", "r") as f:
    product_spec = f.read()

# Instantiate all the agents

# Action Planning Agent
knowledge_action_planning = (
    "Stories are defined from a product spec by identifying a "
    "persona, an action, and a desired outcome for each story. "
    "Each story represents a specific functionality of the product "
    "described in the specification. \n"
    "Features are defined by grouping related user stories. \n"
    "Tasks are defined for each story and represent the engineering "
    "work required to develop the product. \n"
    "A development Plan for a product contains all these components"
)
# TODO: 4 - Instantiate an action_planning_agent using the 'knowledge_action_planning'
action_planning_agent = ActionPlanningAgent(
    openai_api_key,
    knowledge_action_planning  # This is provided in starter code
)

# Product Manager - Knowledge Augmented Prompt Agent
persona_product_manager = "You are a Product Manager, you are responsible for defining the user stories for a product."
knowledge_product_manager = (
    "Stories are defined by writing sentences with a persona, an action, and a desired outcome. "
    "The sentences always start with: As a "
    "Write several stories for the product spec below, where the personas are the different users of the product. "
    # TODO: 5 - Complete this knowledge string by appending the product_spec loaded in TODO 3
    + product_spec
)

# TODO: 6 - Instantiate a product_manager_knowledge_agent using 'persona_product_manager' and the completed 'knowledge_product_manager'
product_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key,
    persona_product_manager,
    knowledge_product_manager
)
# Product Manager - Evaluation Agent
# TODO: 7 - Define the persona and evaluation criteria for a Product Manager evaluation agent and instantiate it as product_manager_evaluation_agent. This agent will evaluate the product_manager_knowledge_agent.
# The evaluation_criteria should specify the expected structure for user stories (e.g., "As a [type of user], I want [an action or feature] so that [benefit/value].").
persona_pm_eval = "You are an evaluation agent that checks the answers of other worker agents"
eval_criteria_pm = "The answer should be stories that follow the following structure: As a [type of user], I want [an action or feature] so that [benefit/value]."
product_manager_evaluation_agent = EvaluationAgent(
    openai_api_key,
    persona_pm_eval,
    eval_criteria_pm,
    product_manager_knowledge_agent,
    max_interactions=10
)

# Program Manager - Knowledge Augmented Prompt Agent
persona_program_manager = "You are a Program Manager, you are responsible for defining the features for a product."
knowledge_program_manager = (
    "Features of a product are defined by organizing similar user stories into cohesive groups. "
    "Here is the product specification to work with:\n\n"
    + product_spec
)
# Instantiate a program_manager_knowledge_agent using 'persona_program_manager' and 'knowledge_program_manager'
# (This is a necessary step before TODO 8. Students should add the instantiation code here.)

# Program Manager - Evaluation Agent
persona_program_manager_eval = "You are an evaluation agent that checks the answers of other worker agents."

program_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key,
    persona_program_manager,      # Provided in starter code
    knowledge_program_manager     # Provided in starter code
)

# TODO: 8 - Instantiate a program_manager_evaluation_agent using 'persona_program_manager_eval' and the evaluation criteria below.
#                      "The answer should be product features that follow the following structure: " \
#                      "Feature Name: A clear, concise title that identifies the capability\n" \
#                      "Description: A brief explanation of what the feature does and its purpose\n" \
#                      "Key Functionality: The specific capabilities or actions the feature provides\n" \
#                      "User Benefit: How this feature creates value for the user"
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.
evaluation_criteria_program = (
    "The answer should be product features that follow the following structure: "
    "Feature Name: A clear, concise title that identifies the capability\n"
    "Description: A brief explanation of what the feature does and its purpose\n"
    "Key Functionality: The specific capabilities or actions the feature provides\n"
    "User Benefit: How this feature creates value for the user"
)

program_manager_evaluation_agent = EvaluationAgent(
    openai_api_key,
    persona_program_manager_eval,  # Provided in starter code
    evaluation_criteria_program,
    program_manager_knowledge_agent,
    max_interactions=10
)

# Development Engineer - Knowledge Augmented Prompt Agent
persona_dev_engineer = "You are a Development Engineer, you are responsible for defining the development tasks for a product."
knowledge_dev_engineer = (
    "Development tasks are defined by identifying what needs to be built to implement each user story. "
    "Here is the product specification to work with:\n\n"
    + product_spec
)
# Instantiate a development_engineer_knowledge_agent using 'persona_dev_engineer' and 'knowledge_dev_engineer'
# (This is a necessary step before TODO 9. Students should add the instantiation code here.)

# Development Engineer - Evaluation Agent
persona_dev_engineer_eval = "You are an evaluation agent that checks the answers of other worker agents."

# Instantiate Development Engineer Knowledge Agent
development_engineer_knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key,
    persona_dev_engineer,      # Provided in starter code
    knowledge_dev_engineer     # Provided in starter code
)
# TODO: 9 - Instantiate a development_engineer_evaluation_agent using 'persona_dev_engineer_eval' and the evaluation criteria below.
#                      "The answer should be tasks following this exact structure: " \
#                      "Task ID: A unique identifier for tracking purposes\n" \
#                      "Task Title: Brief description of the specific development work\n" \
#                      "Related User Story: Reference to the parent user story\n" \
#                      "Description: Detailed explanation of the technical work required\n" \
#                      "Acceptance Criteria: Specific requirements that must be met for completion\n" \
#                      "Estimated Effort: Time or complexity estimation\n" \
#                      "Dependencies: Any tasks that must be completed first"
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.
evaluation_criteria_dev = (
    "The answer should be tasks following this exact structure: "
    "Task ID: A unique identifier for tracking purposes\n"
    "Task Title: Brief description of the specific development work\n"
    "Related User Story: Reference to the parent user story\n"
    "Description: Detailed explanation of the technical work required\n"
    "Acceptance Criteria: Specific requirements that must be met for completion\n"
    "Estimated Effort: Time or complexity estimation\n"
    "Dependencies: Any tasks that must be completed first"
)

development_engineer_evaluation_agent = EvaluationAgent(
    openai_api_key,
    persona_dev_engineer_eval,  # Provided in starter code
    evaluation_criteria_dev,
    development_engineer_knowledge_agent,
    max_interactions=10
)

# Routing Agent
# TODO: 10 - Instantiate a routing_agent. You will need to define a list of agent dictionaries (routes) for Product Manager, Program Manager, and Development Engineer. Each dictionary should contain 'name', 'description', and 'func' (linking to a support function). Assign this list to the routing_agent's 'agents' attribute.

# Job function persona support functions
# TODO: 11 - Define the support functions for the routes of the routing agent (e.g., product_manager_support_function, program_manager_support_function, development_engineer_support_function).
# Each support function should:
#   1. Take the input query (e.g., a step from the action plan).
#   2. Get a response from the respective Knowledge Augmented Prompt Agent.
#   3. Have the response evaluated by the corresponding Evaluation Agent.
#   4. Return the final validated response.
def product_manager_support_function(query):
    """
    Coordinates the Product Manager team:
    1. Knowledge agent generates user stories from product spec
    2. Evaluation agent validates format (As a X, I want Y, so that Z)
    3. Returns validated user stories
    """
    # Step 1: Explicitly call respond() on knowledge agent (rubric requirement)
    response = product_manager_knowledge_agent.respond(query)

    # Step 2: Pass response to evaluation agent (rubric requirement)
    result = product_manager_evaluation_agent.evaluate(query, initial_response=response)

    # Step 3: Return final validated response (rubric requirement)
    return result["final_response"]

def program_manager_support_function(query):
    """
    Coordinates the Program Manager team:
    1. Knowledge agent groups stories into features
    2. Evaluation agent validates feature structure
    3. Returns validated features
    """
    # Step 1: Explicitly call respond() on knowledge agent (rubric requirement)
    response = program_manager_knowledge_agent.respond(query)

    # Step 2: Pass response to evaluation agent (rubric requirement)
    result = program_manager_evaluation_agent.evaluate(query, initial_response=response)

    # Step 3: Return final validated response (rubric requirement)
    return result["final_response"]

def development_engineer_support_function(query):
    """
    Coordinates the Development Engineer team:
    1. Knowledge agent creates engineering tasks
    2. Evaluation agent validates task structure (ID, title, criteria, etc.)
    3. Returns validated tasks
    """
    # Step 1: Explicitly call respond() on knowledge agent (rubric requirement)
    response = development_engineer_knowledge_agent.respond(query)

    # Step 2: Pass response to evaluation agent (rubric requirement)
    result = development_engineer_evaluation_agent.evaluate(query, initial_response=response)

    # Step 3: Return final validated response (rubric requirement)
    return result["final_response"]

routing_agent = RoutingAgent(openai_api_key, {})

routing_agent.agents = [
    {
        "name": "Product Manager",
        # 🎯 RUBRIC TIP: Make descriptions specific and mutually exclusive
        "description": "Responsible for defining product personas and user stories only. Does not define features or tasks. Does not group stories",
        "func": lambda x: product_manager_support_function(x)
    },
    {
        "name": "Program Manager",
        # 🎯 Description emphasizes grouping stories into features
        "description": "Responsible for defining product features by grouping related user stories. Does not create stories or tasks.",
        "func": lambda x: program_manager_support_function(x)
    },
    {
        "name": "Development Engineer",
        # 🎯 Description emphasizes detailed tasks with criteria
        "description": "Responsible for defining detailed engineering tasks with acceptance criteria and estimations. Does not create stories or features.",
        "func": lambda x: development_engineer_support_function(x)
    }
]

# Run the workflow

print("\n*** Workflow execution started ***\n")
# Workflow Prompt
# ****
workflow_prompt = "Create a complete development plan for this product including user stories, features, and development tasks."
# ****
print(f"Task to complete in this workflow, workflow prompt = {workflow_prompt}")

print("\nDefining workflow steps from the workflow prompt")
# TODO: 12 - Implement the workflow.
#   1. Use the 'action_planning_agent' to extract steps from the 'workflow_prompt'.
#   2. Initialize an empty list to store 'completed_steps'.
#   3. Loop through the extracted workflow steps:
#      a. For each step, use the 'routing_agent' to route the step to the appropriate support function.
#      b. Append the result to 'completed_steps'.
#      c. Print information about the step being executed and its result.
#   4. After the loop, print the final output of the workflow (the last completed step).
# The workflow prompt is provided in starter code above
print(f"Task to complete: {workflow_prompt}\n")

# Step 1: Extract workflow steps from the prompt
print("=== STEP 1: Action Planning ===")
workflow_steps = action_planning_agent.extract_steps_from_prompt(workflow_prompt)
print(f"Extracted workflow steps:")
for i, step in enumerate(workflow_steps, 1):
    print(f"  {i}. {step}")

# Step 2: Execute each step with routing
print("\n=== STEP 2: Executing Workflow Steps ===")
completed_steps = []

for step_num, step in enumerate(workflow_steps, 1):
    print(f"\n--- Executing Step {step_num}/{len(workflow_steps)}: {step} ---")

    # Route the step to the appropriate team
    result = routing_agent.route(step)

    # Store the result
    completed_steps.append(result)

    # Show preview of result
    print(f"\nResult Preview:\n{result[:200]}..." if len(result) > 200 else f"\nResult:\n{result}")

# Step 3: Display final output
print("\n" + "="*80)
print("=== WORKFLOW COMPLETE ===")
print("="*80)
print("\nFinal Output (Engineering Tasks):")
print(completed_steps[-1])  # Last step should be the development tasks
