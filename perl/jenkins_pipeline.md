pipeline {
    agent any

    environment {
        P4CLIENT = 'your_perforce_workspace_name'
        P4PORT = 'your_perforce_server:1666'
        P4USER = 'your_perforce_username'
        P4PASSWD = credentials('your_perforce_password_id')
        CHANGE_LIST = sh(script: 'p4 changes -m 1 //path/to/your/code/...@=now', returnStdout: true).trim()
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout([$class: 'PerforceSCM', credential: 'your_perforce_credential_id', populate: autoClean(delete: true, modtime: false, parallel: [enable: false, minbytes: '1024', minfiles: '1', threads: '4'], pin: '', quiet: true, replace: true, tidy: false), workspace: [disableSyncOnly: false, name: "${P4CLIENT}-${CHANGE_LIST}", spec: [allwrite: true, clobber: false, compress: false, line: 'LOCAL', locked: false, modtime: false, rmdir: false, streamName: '', view: '//path/to/your/code/...']]])
                }
            }
        }

        stage('Find Modified Perl Files') {
            steps {
                script {
                    def modifiedPerlFiles = sh(script: 'p4 files //path/to/your/code/...@${CHANGE_LIST}', returnStdout: true).findAll { it.endsWith('.pl') || it.endsWith('.pm') }
                    echo "Modified Perl files: ${modifiedPerlFiles}"
                }
            }
        }

        stage('Run Perl Critic') {
            steps {
                script {
                    // Implement Perl Critic commands here
                    // Example of a failing stage
                    error "Perl Critic failed!"
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    // Implement unit test commands here
                }
            }
        }
    }

    post {
        always {
            script {
                // Capture failure message and stage name
                def failureMessage = currentBuild.result == 'FAILURE' ? currentBuild.rawBuild.getLog(100).join('\n') : null
                def failedStage = currentBuild.result == 'FAILURE' ? currentBuild.rawBuild.getCauseOfFailure().getShortDescription() : null

                // Notify user regardless of success or failure
                echo "Pipeline finished. Sending notification to the user."

                // Include failure details in the notification
                echo "Failure Message: ${failureMessage}"
                echo "Failed Stage: ${failedStage}"

                // Implement notification mechanism (email, Slack, etc.)
            }
        }
    }
}
