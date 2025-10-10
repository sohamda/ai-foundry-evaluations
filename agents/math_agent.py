import os
from pathlib import Path
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import CodeInterpreterTool

# Create an AIProjectClient from an endpoint, copied from your Azure AI Foundry project.
# You need to login to Azure subscription via Azure CLI and set the environment variables
project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]  # Ensure the FOUNDRY_PROJECT_ENDPOINT environment variable is set

# Create an AIProjectClient instance
project_client = AIProjectClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential(),  # Use Azure Default Credential for authentication
)

code_interpreter = CodeInterpreterTool()
with project_client:
    # Create an agent with the Code Interpreter tool
    agent = project_client.agents.create_agent(
        model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],  # Model deployment name
        name="math-agent",  # Name of the agent
        instructions="You politely help with math questions. Use the Code Interpreter tool when asked to visualize numbers.",  # Instructions for the agent
        tools=code_interpreter.definitions,  # Attach the tool
    )
    print(f"Created agent, ID: {agent.id}")

    # # Create a thread for communication
    # thread = project_client.agents.threads.create()
    # print(f"Created thread, ID: {thread.id}")

    # # Add a message to the thread
    # message = project_client.agents.messages.create(
    #     thread_id=thread.id,
    #     role="user",  # Role of the message sender
    #     content="Hi, Agent! Draw a graph for a line with a slope of 4 and y-intercept of 9.",  # Message content
    # )
    # print(f"Created message, ID: {message['id']}")

    # # Create and process an agent run
    # run = project_client.agents.runs.create_and_process(
    #     thread_id=thread.id,
    #     agent_id=agent.id,
    #     additional_instructions="Please address the user as Jane Doe. The user has a premium account",
    # )
    # print(f"Run finished with status: {run.status}")

    # # Check if the run failed
    # if run.status == "failed":
    #     print(f"Run failed: {run.last_error}")

    # # Fetch and log all messages
    # messages = project_client.agents.messages.list(thread_id=thread.id)
    # for message in messages:
    #     print(f"Role: {message.role}, Content: {message.content}")

    #     # Save every image file in the message
    #     for img in message.image_contents:
    #         file_id = img.image_file.file_id
    #         file_name = f"{file_id}_image_file.png"
    #         project_client.agents.files.save(file_id=file_id, file_name=file_name)
    #         print(f"Saved image file to: {Path.cwd() / file_name}")

    # Uncomment these lines to delete the agent when done
    # project_client.agents.delete_agent(agent.id)
    # print("Deleted agent")