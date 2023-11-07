import requests

# Replace these with your Artifactory details
artifactory_url = 'https://your-artifactory-instance/artifactory/your-repo'
username = 'your-username'
password = 'your-password'

# Replace this with the path where you want to deploy the JAR in the repository
deploy_path = 'your/path/in/repository'

# Replace this with the local path to your JAR file
local_jar_path = '/path/to/your/file.jar'

# Create the URL for deployment
deploy_url = f'{artifactory_url}/{deploy_path}/file.jar'

# Prepare headers for authentication
headers = {'Authorization': 'Basic ' + f'{username}:{password}'.encode('utf-8').b64encode().decode('utf-8')}

# Open the JAR file and send it to Artifactory
with open(local_jar_path, 'rb') as jar_file:
        response = requests.put(deploy_url, data=jar_file, headers=headers)

        # Check the response status
        if response.status_code == 201:
                print(" JAR file successfully deployed to {deploy_url} ")
            else:
                    print("Failed to deploy JAR file. Status code: {response.status_code}, Response: {response.text}")

