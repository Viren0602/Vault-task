#!/bin/bash



# Set up Vault environment variables
export VAULT_ADDR='http://192.168.3.174:8200'
export VAULT_TOKEN='test'

# Retrieve secrets from Vault
screener_username=$(vault kv get -field=username secret/data/myapp)
screener_password=$(vault kv get -field=password secret/data/myapp)

# Print retrieved secrets
echo "Retrieved Screener Username: $screener_username"
echo "Retrieved Screener Password: $screener_password"


























#!/bin/bash

# # Define Vault address and user credentials
# VAULT_ADDR='http://0.0.0.0:8200'
# VAULT_USER="viren"
# VAULT_PASS="viren@9999"

# # Log in to Vault and retrieve a token
# VAULT_TOKEN=$(curl -s --request POST \
#   --data "{\"password\": \"$VAULT_PASS\"}" \
#   $VAULT_ADDR/v1/auth/userpass/login/$VAULT_USER | jq -r '.auth.client_token')

# # Use the token to fetch the secret values
# username=$(curl -s --header "X-Vault-Token: $VAULT_TOKEN" \
#   $VAULT_ADDR/v1/secret/data/screener | jq -r '.data.data.username')

# password=$(curl -s --header "X-Vault-Token: $VAULT_TOKEN" \
#   $VAULT_ADDR/v1/secret/data/screener | jq -r '.data.data.password')

# # Export the variables for use in other scripts
# export SCREENER_USERNAME=$username
# export SCREENER_PASSWORD=$password


















# # Define Vault address and user credentials
# VAULT_ADDR='http://0.0.0.0:8200'
# VAULT_USER="viren"
# VAULT_PASS="viren@9999"

# # Log in to Vault and retrieve a token
# VAULT_TOKEN=$(curl -s --request POST \
#   --data "{\"password\": \"$VAULT_PASS\"}" \
#   $VAULT_ADDR/v1/auth/userpass/login/$VAULT_USER | jq -r '.auth.client_token')

# # Use the token to fetch the secret values
# username=$(curl -s --header "X-Vault-Token: $VAULT_TOKEN" \
#   $VAULT_ADDR/v1/secret/data/screener | jq -r '.data.data.username')

# password=$(curl -s --header "X-Vault-Token: $VAULT_TOKEN" \
#   $VAULT_ADDR/v1/secret/data/screener | jq -r '.data.data.password')

# # Export the variables for use in other scripts
# export SCREENER_USERNAME=$username
# export SCREENER_PASSWORD=$password







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







