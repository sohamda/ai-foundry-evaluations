# Azure AI Foundry Evaluations

This project demos the Github actions for Evaluations of Azure AI Foundry models and Agents.

# Infra
Azure infra is a copy of [Standard Agent Setup](https://github.com/azure-ai-foundry/foundry-samples/blob/main/samples/microsoft/infrastructure-setup/41-standard-agent-setup/README.md)


## 🚀 Quick Start

### Prerequisites

- Azure subscription with appropriate permissions
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed
- [Bicep CLI](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/install) installed
- [Azure Developer CLI (azd)](https://docs.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd) installed (optional)

### Option 1: Deploy with Azure Developer CLI (Recommended)

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ai-foundry-evaluations
   ```

2. **Initialize azd**:
   ```bash
   azd init
   ```

3. **Deploy the infrastructure**:
   ```bash
   azd up
   ```

4. **Start building AI agents**:
   Visit [Azure AI Foundry Studio](https://ai.azure.com) and locate your deployed project.

### Option 2: Deploy with Azure CLI

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ai-foundry-evaluations
   ```

2. **Login to Azure**:
   ```bash
   az login
   ```

3. **Create a resource group**:
   ```bash
   az group create --name rg-ai-foundry-eval --location eastus
   ```

4. **Deploy the Bicep template**:
   ```bash
   az deployment group create \
     --resource-group rg-ai-foundry-eval \
     --template-file infra/main.bicep \
     --parameters infra/main.parameters.json
   ```

### Option 3: Deploy with GitHub Actions

1. **Fork this repository** to your GitHub account

2. **Set up GitHub secrets** for Azure authentication:
   - `AZURE_CLIENT_ID` - Service Principal Client ID
   - `AZURE_TENANT_ID` - Azure Tenant ID
   - `AZURE_SUBSCRIPTION_ID` - Azure Subscription ID
   - `AZURE_OPENAI_API_KEY` - Key to connect to AOAI model
   - `AZURE_OPENAI_API_VERSION` - AOAI API version
   - `AZURE_OPENAI_CHAT_DEPLOYMENT` - AOAI deployment name
   - `AZURE_OPENAI_ENDPOINT` - AOAI endpoint
   - `FOUNDRY_PROJECT_ENDPOINT` - Azure foundry Project endpoint

3. **Push changes** to the `main` branch or manually trigger the workflow

4. **Monitor deployment** in the Actions tab of your GitHub repository


## 📁 Project Structure

```
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions workflow
├── infra/
│   ├── modules/
│   │   └── xxxxx
│   ├── main.bicep              # Main infrastructure template
├── azure.yaml                  # Azure Developer CLI configuration
└── README.md                   # This file
```

### CI/CD Pipeline

The GitHub Actions workflow:

1. **Validates** Bicep templates on pull requests
2. **Deploys** on main branch pushes
3. **Evaluation** Model and Agent evaluations

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

- [Azure AI Foundry Documentation](https://docs.microsoft.com/en-us/azure/ai-studio/)
- [Azure Bicep Documentation](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/)
- [Azure Developer CLI Documentation](https://docs.microsoft.com/en-us/azure/developer/azure-developer-cli/)
- [GitHub Actions for Azure](https://docs.microsoft.com/en-us/azure/developer/github/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Submit pull requests to the main branch.

