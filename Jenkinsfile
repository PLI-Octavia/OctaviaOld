pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'bin/install.sh && bin/build.sh'
      }
    }
    stage('test') {
      steps {
        sh 'bin/test.sh'
      }
    }
    stage('deploy') {
      steps {
        sh 'bin/deploy.sh Preproduction'
      }
    }
  }
}
