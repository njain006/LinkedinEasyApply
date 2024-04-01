# Parse JSON string
data = {
    'app': {'id': -323232, 'name': 'Sevenroons', 'platform': 'web'},
    'accountId': 'lecarillonportofino',
    'subscription': {'id': 5646448887332864, 'name': 'Sevenroons'},
    'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'event': 'accountCreated',
    'properties': {},
    'timestamp': 1711118734,
    'visitorId': 'jancarlo.manuel@sevenrooms.com',
    'uniqueId': '0fd0645bf07728b3c134be376e3f0e7c64715327'
}

# Accessing individual fields and providing explicit variable names
app_id = data['app']['id']
app_name = data['app']['name']
platform = data['app']['platform']
account_id = data['accountId']
subscription_id = data['subscription']['id']
subscription_name = data['subscription']['name']
user_agent = data['userAgent']
event = data['event']
browser_name = data['properties'].get('browserName', '')  # Handle missing key with get() method
browser_version = data['properties'].get('browserVersion', '')  # Handle missing key with get() method
sample_group = data['properties'].get('sampleGroup', '')  # Handle missing key with get() method
timestamp = data['timestamp']
visitor_id = data['visitorId']
unique_id = data['uniqueId']

# Printing the values for applying
print("App ID:", app_id)
print("App Name:", app_name)
print("Platform:", platform)
print("Account ID:", account_id)
print("Subscription ID:", subscription_id)
print("Subscription Name:", subscription_name)
print("User Agent:", user_agent)
print("Event:", event)
print("Browser Name:", browser_name)
print("Browser Version:", browser_version)
print("Sample Group:", sample_group)
print("Timestamp:", timestamp)
print("Visitor ID:", visitor_id)
print("Unique ID:", unique_id)
