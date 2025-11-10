pipeline {
  agent any
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Unit Tests') { steps { sh 'pytest -q' } }
    stage('Build Image') { steps { sh 'docker build -t aceest:latest .' } }
  }
}
