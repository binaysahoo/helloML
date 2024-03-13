pipeline {
  agent any
  stages {
    stage('unittest') {
      steps {
        sh '''#!/bin/bash

time=`date`
host=`host`

echo "running on host:$host at: $time "'''
      }
    }

  }
  environment {
    NAME = 'pipelinetesting'
  }
}