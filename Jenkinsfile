pipeline {
agent any





stages {
stage('Build') {
steps {
// Get some code from a GitHub repository
git url: 'https://github.com/tripathi01/newflaskproject.git'

// Run Maven on a Unix agent.
script{
if(isUnix()){
sh "pip3 install -r requirements.txt"
}
else{
bat "pip install -r requirements.txt"
}
}
}
}



stage('Integration Test') {
steps {

// Run Maven on a Unix agent.
script{
if(isUnix()){
sh "pytest"
}
else{
bat "pytest"
}
}
}

}
stage('Docker Build') {
            steps {
                script{
                if(isUnix()){
                sh "docker build -t  atultripathi01/newflaskapp ."
                }
                else{
                 bat "docker build -t atultripathi01/newflaskapp ."
                 }
                 }

            }
        }
stage('Docker Push') {
            steps {
               withCredentials([usernamePassword(credentialsId:'dockerHub',passwordVariable: 'dockerHubPassword',usernameVariable:'dockerHubUser')]){
                sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                sh "docker push atultripathi01/newflaskapp:latest"
                }
            }
    }
}
}