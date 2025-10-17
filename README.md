# AI-Powered Agentic Workflow for Project Management

A sophisticated multi-agent system that automates the complete product development lifecycle, transforming high-level product specifications into actionable user stories, features, and engineering tasks through intelligent agent orchestration.

## 🏗️ Architecture Overview

The system implements a hierarchical agent architecture with specialized roles mirroring real-world organizational structures:

```
┌─────────────────────────────────────────────────────────────────┐
│                    Agentic Workflow System                     │
├─────────────────────────────────────────────────────────────────┤
│  Input: Product Specification + High-Level Requirements        │
└─────────────────────┬───────────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────────┐
│                Action Planning Agent                           │
│  • Breaks down high-level goals into logical sub-tasks        │
│  • Defines workflow steps for specialized agents              │
└─────────────────────┬───────────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────────┐
│                  Routing Agent                                 │
│  • Intelligently assigns tasks to specialized agent teams     │
│  • Dynamic task distribution based on query analysis          │
└─────────────────────┬───────────────────────────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
┌───────▼───┐  ┌─────▼─────┐  ┌────▼────────┐
│ Product   │  │ Program   │  │ Development │
│ Manager   │  │ Manager   │  │ Engineer    │
│ Team      │  │ Team      │  │ Team        │
│ (Step 1)  │  │ (Step 2)  │  │ (Step 3)    │
├───────────┤  ├───────────┤  ├─────────────┤
│ • User    │  │ • Feature │  │ • Task      │
│   Stories │  │   Groups  │  │   Creation  │
│ • Persona │  │ • Feature │  │ • Acceptance│
│   Def.    │  │   Specs   │  │   Criteria  │
└─────┬─────┘  └─────┬─────┘  └─────┬───────┘
      │              │              │
      └──────────────┼──────────────┘
                     │
┌────────────────────▼───────────────────────────────────────────┐
│              Evaluation & Quality Control                      │
│  • Each team paired with dedicated evaluation agent           │
│  • Iterative refinement until criteria met                    │
│  • Built-in quality gates prevent suboptimal outputs          │
└───────────────────────────────────────────────────────────────┘
```

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **AI/ML**: OpenAI GPT-3.5-turbo API
- **Environment Management**: python-dotenv
- **Data Processing**: pandas, numpy
- **Architecture Pattern**: Multi-Agent System with Evaluation Loops

## 🚀 Key Features

### Multi-Agent Architecture

- **Specialized Agent Teams**: Product Manager, Program Manager, and Development Engineer teams
- **Intelligent Routing**: Dynamic task assignment based on query analysis
- **Quality Assurance**: Built-in evaluation loops with iterative refinement

### Knowledge Augmentation

- **Context-Aware Processing**: Agents leverage domain-specific product specifications
- **Structured Outputs**: Consistent formatting across all agent outputs
- **Validation Criteria**: Automated quality checks for each output type

### Scalable Design

- **Reusable Agent Library**: Modular components for different workflow types
- **General-Purpose Framework**: Adaptable to various product specifications
- **Extensible Architecture**: Easy to add new agent types and capabilities

## 📁 Project Structure

```
project-management-agentic-workflow/
├── starter/
│   ├── phase_1/                    # Agent Library Implementation
│   │   ├── workflow_agents/
│   │   │   └── base_agents.py     # Core agent implementations
│   │   ├── *_agent.py             # Individual agent test scripts
│   │   └── outputs/               # Test execution results
│   └── phase_2/                    # Workflow Orchestration
│       ├── agentic_workflow.py    # Main workflow implementation
│       ├── workflow_agents/
│       │   └── Product-Spec-Email-Router.txt
│       └── outputs/               # Workflow execution results
├── requirements.txt               # Python dependencies
└── README.md                     # This file
```

## 🎯 Agent Capabilities

### Core Agent Types

1. **DirectPromptAgent**: Basic LLM interaction without augmentation using GPT-3.5-turbo
2. **AugmentedPromptAgent**: Enhanced prompting with persona-based system prompts
3. **KnowledgeAugmentedPromptAgent**: Domain-specific knowledge integration with constrained responses
4. **RAGKnowledgePromptAgent**: Retrieval-Augmented Generation using embeddings and similarity search
5. **EvaluationAgent**: Quality assurance with iterative refinement (max 10 interactions)
6. **RoutingAgent**: Intelligent task distribution using embedding similarity
7. **ActionPlanningAgent**: High-level goal decomposition into sequential steps

### Specialized Workflow Teams

- **Product Manager Team**: User story generation following "As a [user], I want [action] so that [benefit]" format
- **Program Manager Team**: Feature grouping with structured format (Name, Description, Key Functionality, User Benefit)
- **Development Engineer Team**: Task creation with detailed structure (ID, Title, Description, Acceptance Criteria, Effort, Dependencies)

## 🔄 Workflow Process

1. **Input Processing**: Product specification and high-level requirements
2. **Action Planning**: Decomposition into logical sub-tasks
3. **Intelligent Routing**: Dynamic assignment to specialized teams
4. **Sequential Processing**: Teams work on their respective domains in sequence
5. **Quality Evaluation**: Iterative refinement until criteria met
6. **Output Synthesis**: Structured delivery of complete development plan

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd project-management-agentic-workflow
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

### Running the System

1. **Test Individual Agents** (Phase 1):

```bash
cd starter/phase_1
python direct_prompt_agent.py
python augmented_prompt_agent.py
# ... run other agent test scripts
```

2. **Execute Full Workflow** (Phase 2):

```bash
cd starter/phase_2
python agentic_workflow.py
```

## 📊 Example Outputs

The system generates structured outputs including:

- **User Stories**: "As a [user type], I want [action] so that [benefit]" format
- **Product Features**: Structured format with Name, Description, Key Functionality, and User Benefit
- **Engineering Tasks**: Detailed tasks with ID, Title, Description, Acceptance Criteria, Effort, and Dependencies

Sample outputs are available in the `outputs/` directories for both phases.

## 🔍 System Analysis & Reflection

### Strengths

1. **Clear Separation of Concerns**: The workflow effectively divides responsibilities among specialized agents (Product Manager, Program Manager, Development Engineer), mirroring real-world organizational structures and enabling each agent to focus on its domain expertise.

2. **Built-in Quality Control**: The use of Evaluation Agents paired with Knowledge Augmented Prompt Agents creates a feedback loop that ensures outputs meet specific criteria before proceeding to the next step, significantly improving output quality and consistency.

3. **Flexible Routing Mechanism**: The RoutingAgent intelligently directs workflow steps to appropriate specialized agents, enabling dynamic task assignment based on the nature of each query rather than hardcoded execution paths.

4. **Context-Aware Processing**: Knowledge augmentation enables agents to leverage domain-specific information and product specifications, resulting in more accurate and relevant outputs compared to generic prompting.

### Limitations

1. **Sequential Dependency Chain**: The workflow operates in a strictly sequential manner where each step depends on the previous one completing successfully. If an early agent (e.g., Product Manager) produces suboptimal output despite passing evaluation criteria, all downstream agents inherit these issues.

2. **Limited Cross-Agent Communication**: Agents don't share context or learnings with each other. For instance, the Development Engineer doesn't directly access the Program Manager's feature groupings, relying instead on the routing agent to pass information sequentially.

3. **Evaluation Rigidity**: Evaluation agents use fixed criteria that may not adapt to edge cases or varying project requirements. The max_interactions limit (10) could terminate the evaluation loop prematurely for complex queries.

4. **No Feedback from Downstream Agents**: Later-stage agents (Development Engineer) cannot provide feedback to earlier-stage agents (Product Manager) if they discover inconsistencies or gaps in the upstream outputs.

### Suggested Improvements

**Shared Memory Architecture**: Introduce a shared memory/context store accessible to all agents in the workflow.

**Implementation Details**:

- Create a `WorkflowContext` class that maintains a structured record of all agent outputs with metadata (timestamps, agent IDs, validation scores)
- Modify each agent to write outputs to and read relevant context from this shared store
- Enable cross-referencing where Development Engineers can query original product specs and user stories directly, not just receive filtered information
- Add a "context injection" mechanism where each agent receives a summary of relevant prior work from other agents

**Expected Benefits**:

- Reduces information loss through sequential handoffs
- Enables better decision-making by giving each agent full visibility into upstream work
- Facilitates potential parallel processing of independent workflow branches
- Creates an audit trail for debugging and improving agent performance
- Allows for future implementation of feedback loops where downstream agents can flag issues to upstream agents

## 📈 Future Enhancements

- **Parallel Processing**: Enable concurrent execution of independent workflow branches (currently sequential)
- **Dynamic Evaluation Criteria**: Adaptive quality standards based on project complexity
- **Cross-Agent Learning**: Shared context and feedback mechanisms
- **Workflow Optimization**: Performance monitoring and automatic optimization
- **Integration APIs**: RESTful endpoints for external system integration

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
