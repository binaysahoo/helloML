pipeline {
  agent any
  stages {
    stage('unittest') {
      parallel {
        stage('unittest') {
          steps {
            sh '''#!/bin/bash

time=`date`
host=`host`

echo "running on host:$host at: $time "'''
          }
        }

        stage('coverage') {
          steps {
            echo 'generate coverage report'
          }
        }

      }
    }

  }
  environment {
    NAME = 'pipelinetesting'
  }
}