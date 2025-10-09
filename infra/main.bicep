targetScope = 'resourceGroup'

// Parameters
@description('The name of the Azure AI Foundry project')
param projectName string

@description('Resource token for naming consistency')
param resourceToken string = uniqueString(subscription().id, resourceGroup().id)

// Variables
var aiProjectName = '${projectName}-${resourceToken}'
var cognitiveServicesName = '${projectName}-cs-${resourceToken}'

// Cognitive Services - Required for AI agents
resource account 'Microsoft.CognitiveServices/accounts@2025-04-01-preview' = {
  name: cognitiveServicesName
  location: resourceGroup().location
  sku: {
    name: 'S0'
  }
  kind: 'AIServices'
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    allowProjectManagement: true
    customSubDomainName: toLower(cognitiveServicesName)
    networkAcls: {
      defaultAction: 'Allow'
      virtualNetworkRules: []
      ipRules: []
    }
    publicNetworkAccess: 'Enabled'
    disableLocalAuth: true
  }
}


// AI Project - Standalone project for AI agent development
resource aiProject 'Microsoft.CognitiveServices/accounts/projects@2025-04-01-preview' = {
  parent: account
  name: aiProjectName
  location: resourceGroup().location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    displayName: aiProjectName
  }
}

// GPT-4o Model Deployment (conditionally deployed)
module modelDeployment 'modules/model-deployment.bicep' = {
  name: 'model-deployment'
  params: {
    accountName: account.name
  }
}

// Outputs
@description('The resource ID of the AI Project')
output aiProjectId string = aiProject.id

@description('The name of the AI Project')
output aiProjectName string = aiProject.name

@description('The resource ID of the Cognitive Services account')
output cognitiveServicesId string = account.id

@description('The endpoint of the Cognitive Services account')
output cognitiveServicesEndpoint string = account.properties.endpoint

@description('The resource group location')
output location string = resourceGroup().location

// AZD-compatible outputs
@description('The name of the AI Project for azd')
output AZURE_AI_PROJECT_NAME string = aiProject.name

@description('The Cognitive Services endpoint for azd')
output AZURE_COGNITIVE_SERVICES_ENDPOINT string = account.properties.endpoint

@description('The resource group name for azd')
output AZURE_RESOURCE_GROUP string = resourceGroup().name

@description('The location for azd')
output AZURE_LOCATION string = resourceGroup().location
