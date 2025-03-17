provider "azurerm" {
  features {}
subscription_id = "f67a4e8e-9799-416e-af54-5c0a8bf8e6e4"
}

resource "azurerm_resource_group" "rg" {
  name     = "TerraformResourceGroup"
  location = "East US"
}
