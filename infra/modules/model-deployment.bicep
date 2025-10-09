@description('The name of the Cognitive Services account')
param accountName string

@description('The capacity for the deployment (TPM - Tokens Per Minute)')
param capacity int = 100

@description('Model name to be deployed')
param modelName string = 'gpt-4o'

@description('The model format of the model you want to deploy. Example: OpenAI')
param modelFormat string = 'OpenAI'

@description('The version of the model you want to deploy. Example: 2024-11-20')
param modelVersion string = '2024-11-20'

// Reference to existing Cognitive Services account
resource account 'Microsoft.CognitiveServices/accounts@2025-04-01-preview' existing = {
  name: accountName
}

// GPT-4o Global Standard Model Deployment
resource modelDeployment 'Microsoft.CognitiveServices/accounts/deployments@2024-10-01'= {
  parent: account
  name: modelName
  sku : {
    capacity: capacity
    name: 'GlobalStandard'
  }
  properties: {
    model:{
      name: modelName
      format: modelFormat
      version: modelVersion
    }
  }
}

// Outputs
@description('The resource ID of the GPT-4o deployment')
output deploymentId string = modelDeployment.id

@description('The name of the GPT-4o deployment')
output deploymentName string = modelDeployment.name

@description('The model name')
output modelName string = modelDeployment.properties.model.name

@description('The model version')
output modelVersion string = modelDeployment.properties.model.version

@description('The SKU name')
output skuName string = modelDeployment.sku.name

@description('The deployment capacity')
output capacity int = modelDeployment.sku.capacity
