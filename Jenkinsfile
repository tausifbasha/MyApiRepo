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
                build : 'pacttest'
            }
        }
        stage('End') {
            steps {
                echo 'Bye'
            }
        }
    }
}
