# Install kubernetes cli plugin
- https://plugins.jenkins.io/kubernetes-cli/

# Download credentials
- scp ubuntu@54.211.240.46:.kube/config k8-config
- Create a secret file credentials in jenkins

# Show minikube IP
- kubectl config view -o jsonpath="{.clusters[?(@.name==\"minikube\")].cluster.server}"

# Set KUBECONFIG
- export KUBECONFIG=~/.kube/config

# Change permissions to cert files
- sudo apt install -y acl
- setfacl -R -m u:jenkins:rwx /home/ubuntu/.minikube/profiles/minikube/

