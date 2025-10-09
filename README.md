# Azure AI Foundry Evaluations

This project provides a simplified Infrastructure as Code (IaC) solution to deploy an Azure AI Foundry project optimized for AI agent development. The setup includes GPT-4o model deployment using Bicep templates with a focus on simplicity and agent-ready configuration.

## 🏗️ Architecture

The deployment creates the following Azure resources optimized for AI agents:

- **Azure AI Project** - Standalone project workspace for AI agent development
- **Cognitive Services** - AI Services account with GPT-4o deployment
- **AI Services Connection** - Pre-configured connection for agent access

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

3. **Push changes** to the `main` branch or manually trigger the workflow

4. **Monitor deployment** in the Actions tab of your GitHub repository

## ⚙️ Configuration

### Parameters

You can customize the deployment by modifying the parameters in `infra/main.parameters.json`:

| Parameter | Description | Default Value |
|-----------|-------------|---------------|
| `projectName` | Name of the AI Foundry project | `ai-foundry-eval` |
| `location` | Azure region for deployment | `eastus` |
| `enableGpt4oDeployment` | Whether to deploy GPT-4o model | `true` |
| `gpt4oDeploymentName` | Name for the GPT-4o deployment | `gpt-4o-global` |
| `gpt4oCapacity` | GPT-4o capacity in TPM | `100` |

### Customization

For different capacity requirements, you can override parameters:

```bash
azd up --set gpt4oCapacity=300
```

## 📁 Project Structure

```
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions workflow
├── infra/
│   ├── modules/
│   │   └── gpt4o-deployment.bicep  # GPT-4o model deployment
│   ├── main.bicep              # Main infrastructure template
│   └── main.parameters.json    # Default parameters
├── azure.yaml                  # Azure Developer CLI configuration
└── README.md                   # This file
```

## 🤖 AI Agent Setup

The deployed infrastructure is optimized for Azure AI Foundry agents with:

- **Pre-configured AI Services Connection** - Ready for agent access
- **GPT-4o Global Standard Model** - Latest model for agent capabilities
- **Simplified Architecture** - No complex hub dependencies
- **Agent-Ready Configuration** - Follows Azure AI Foundry best practices

## � Security Considerations

- **Managed Identity**: AI Project uses system-assigned managed identity
- **Network Security**: Resources configured with appropriate access controls
- **AI Services**: Secure connection using Azure AD authentication

## 🛠️ Development Workflow

### Local Development

1. Make changes to Bicep templates
2. Validate templates:
   ```bash
   az bicep build --file infra/main.bicep
   az bicep lint --file infra/main.bicep
   ```
3. Test deployment
4. Submit pull request for review

### CI/CD Pipeline

The GitHub Actions workflow automatically:

1. **Validates** Bicep templates on pull requests
2. **Deploys** on main branch pushes
3. **Provides** deployment summaries and links

## 🔧 Troubleshooting

### Common Issues

**Issue**: Deployment fails with quota limits
**Solution**: Check [Azure quotas](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits) and request increases if needed

**Issue**: GPT-4o model deployment fails
**Solution**: Ensure the selected region supports GPT-4o and you have sufficient quota

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

Contributions are welcome! Please read our contributing guidelines and submit pull requests to the main branch.

---

**Happy building with Azure AI Foundry! 🚀**
Github workflow example of running Azure AI Foundry evaluations
