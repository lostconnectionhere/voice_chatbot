import json

# Load the configuration from the JSON file
with open('config.json') as config_file:
    config_data = json.load(config_file)

# Extract the subscription key
subscription_key = config_data.get('subscription_key')

if subscription_key:
    # Use the subscription key in your script
    print(f"Subscription Key: {subscription_key}")
    # Now you can use subscription_key for your Azure service

else:
    print("Subscription key not found in the configuration file.")

