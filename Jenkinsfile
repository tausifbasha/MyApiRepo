pipeline {
agent
    {
        node {
                label 'master'
                customWorkspace "${env.JobPath}"
              }
    }
    stages 
    {
        stage('Start') {
            steps {
                echo 'Hello'
            }
        }
        stage ('Invoke PACT')  {
            steps {
                build job: "pacttest/master", propagate: true, wait: true
            }
        }
        stage('End') {
            steps {
                echo 'Bye'
            }
        }
    }
}
