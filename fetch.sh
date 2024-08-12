#!/bin/bash

# Define Vault address and user credentials
VAULT_ADDR='http://0.0.0.0:8200'
VAULT_USER="viren"
VAULT_PASS="viren"

# Log in to Vault and retrieve a token
VAULT_TOKEN=$(curl -s --request POST \
  --data "{\"password\": \"$VAULT_PASS\"}" \
  $VAULT_ADDR/v1/auth/userpass/login/$VAULT_USER | jq -r '.auth.client_token')

# Use the token to fetch the secret values
username=$(curl -s --header "X-Vault-Token: $VAULT_TOKEN" \
  $VAULT_ADDR/v1/secret/data/screener | jq -r '.data.data.username')

password=$(curl -s --header "X-Vault-Token: $VAULT_TOKEN" \
  $VAULT_ADDR/v1/secret/data/screener | jq -r '.data.data.password')

# Export the variables for use in other scripts
export SCREENER_USERNAME=$username
export SCREENER_PASSWORD=$password







# #!/bin/bash

# # Define Vault address and user credentials
# VAULT_ADDR='http://0.0.0.0:8200'
# VAULT_USER="viren"
# VAULT_PASS="viren"

# # Log in to Vault and retrieve a token
# VAULT_TOKEN=$(curl -s --request POST \
#   --data "{\"password\": \"$VAULT_PASS\"}" \
#   $VAULT_ADDR/v1/auth/userpass/login/$VAULT_USER | jq -r '.auth.client_token')

# # Use the token to fetch the secret values
# username=$(curl -s --header "X-Vault-Token: $VAULT_TOKEN" \
#   $VAULT_ADDR/v1/secret/data/screener | jubq -r '.data.data.username')

# password=$(curl -s --header "X-Vault-Token: $VAULT_TOKEN" \
#   $VAULT_ADDR/v1/secret/data/screener | jq -r '.data.data.password')

# # Export the variables for use in other scripts
# export SCREENER_USERNAME=$username
# export SCREENER_PASSWORD=$password







