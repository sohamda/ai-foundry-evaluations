# Azure AI Foundry: Agentic DevOps

This project demonstrates `Github workflow for AgenticDevOps` 
1. Deploy Azure Infra
2. Create Agent(s)
3. Evaluate model(s)
4. Evaluation Agent(s)

Uses [Github actions for Evaluations](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/evaluation-github-action?tabs=foundry-project) of Azure AI Foundry models and Agents.

This project uses evaluation input samples from:
1. [genai-evals](https://github.com/microsoft/genai-evals/blob/main/.github/.test_files/eval-input.jsonl)
2. [ai-agents-eval](https://github.com/microsoft/ai-agent-evals/tree/main/samples/data)

# Infra
Azure infra is a copy of [Standard Agent Setup](https://github.com/azure-ai-foundry/foundry-samples/blob/main/samples/microsoft/infrastructure-setup/41-standard-agent-setup/README.md)

## NOTE
Make sure 
1. Public Network access is enabled for Storage and CosmosDB resources. 
2. The Storage, Cosmos, AI Search are connected resources for your Foundry project.
3. You have "Storage Blob Data Contributor" role assigned. 
4. For gpt-4o deployment you need enough TPM to run the evaluations, otherqwise you'll see throttling errors. For example, I have 1K TPM.

# Service Principle for Github Actions
Last checked: 15-10-2025 

Using Managed Identity to run Agent Eval action doesn't work. You need a Service Principle (atleast) to execute the "Create Agent" and "Agent Evaluation" workflows.

[How to create Service Principle](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-secret)

## 🚀 How to Start

### Prerequisites

- Azure subscription with appropriate permissions (Contributor or Owner)
- **Fork this repository** to your GitHub account

### 1. Deploy with GitHub Actions - [deploy.yml](.github/workflows/deploy.yml)

1. Setup Service Principle for Github action. (see above)
2. Add the following Repository Secrets:
   - `AZURE_CREDENTIALS` - JSON object with Service Principal Client ID, Client Secret, Subscription ID, Tenant ID
   - `AZURE_SUBSCRIPTION_ID` - Azure Subscription ID
   - `AZURE_RESOURCE_GROUP_NAME` - Azure Resource Group Name
3. Wait for a successfull run.
4. Alternatively you can click the below. But DO NOT forget do Step 1 & 2

[![Deploy To Azure](https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazure.svg?sanitize=true)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fazure-ai-foundry%2Ffoundry-samples%2Frefs%2Fheads%2Fmain%2Fsamples%2Fmicrosoft%2Finfrastructure-setup%2F41-standard-agent-setup%2Fazuredeploy.json) 

### 2. Create Agent GitHub Actions - [create_agent.yml](.github/workflows/create_agent.yml)

1. Assuming #1 deploy action is successfully done.
2. Add the following Repository Secrets:
   - `FOUNDRY_PROJECT_ENDPOINT` - Azure foundry Project endpoint
   - `AZURE_OPENAI_CHAT_DEPLOYMENT` - AOAI deployment name
3. Wait for a successfull run.

### 3. Evaluate Model GitHub Actions - [model_eval.yml](.github/workflows/model_eval.yml)

1. Assuming #1 deploy action is successfully done.
2. Add the following Repository Secrets:
   - `AZURE_OPENAI_API_KEY` - Key to connect to AOAI model
   - `AZURE_OPENAI_API_VERSION` - AOAI API version
   - `AZURE_OPENAI_ENDPOINT` - AOAI endpoint
   - `AZURE_AI_PROJECT_NAME` - Azure foundry Project Name
3. Wait for a successfull run.

### 4. Evaluate Agent GitHub Actions - [agent_eval.yml](.github/workflows/agent_eval.yml)

1. Assuming #1(deploy) & #2(create agent) actions are successfully finished.
2. Add the following Repository Secrets: (it also needs some secrets mentioned in the previous step)
   - `AGENT_ID` - Azure foundry Agent ID
3. Wait for a successfull run.

#### Validate you have all the below secrets to run all the Github workflows

   - `AZURE_CREDENTIALS` - JSON object with Service Principal Client ID, Client Secret, Subscription ID, Tenant ID
   - `AZURE_SUBSCRIPTION_ID` - Azure Subscription ID
   - `AZURE_RESOURCE_GROUP_NAME` - Azure Resource Group Name
   - `AZURE_OPENAI_API_KEY` - Key to connect to AOAI model
   - `AZURE_OPENAI_API_VERSION` - AOAI API version
   - `AZURE_OPENAI_CHAT_DEPLOYMENT` - AOAI deployment name
   - `AZURE_OPENAI_ENDPOINT` - AOAI endpoint
   - `FOUNDRY_PROJECT_ENDPOINT` - Azure foundry Project endpoint
   - `AZURE_AI_PROJECT_NAME` - Azure foundry Project Name
   - `AGENT_ID` - Azure foundry Agent ID

## 🔧 Troubleshooting

### Common Issues

**Issue**: Deployment fails with quota limits
**Solution**: Check [Azure quotas](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits) and request increases if needed

**Issue**: Model deployment fails
**Solution**: Ensure the selected region supports the model and you have sufficient quota

**Issue**: Resource naming conflicts
**Solution**: Change the `resourceToken` or `projectName` parameter

### Getting Help

1. Check the [Azure AI Foundry documentation](https://docs.microsoft.com/en-us/azure/ai-studio/)
2. Review deployment logs in Azure Portal
3. Check GitHub Actions workflow logs
4. Create an issue in this repository

## 📚 Additional Resources

- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry)
- [Evaluation via Github actions](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/evaluation-github-action?tabs=foundry-project)
- [GitHub Actions for Azure](https://docs.microsoft.com/en-us/azure/developer/github/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Submit pull requests to the main branch.

