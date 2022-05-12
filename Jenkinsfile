pipeline {
    agent {
      kubernetes  {
      yaml """
apiVersion: v1
kind: Pod
metadata:
  name: kaniko
spec:
  containers:
    - name: tools
      image: adiachan/ci-cd-builder
      command:
        - /bin/cat
      tty: true
    - name: kaniko
      image: gcr.io/kaniko-project/executor:debug
      command:
        - /busybox/cat
      tty: true
      volumeMounts:
        - name: kaniko-secret
          mountPath: /kaniko/.docker
  volumes:
    - name: kaniko-secret
      secret:
        secretName: regcred
        items:
          - key: .dockerconfigjson
            path: config.json
"""
        }
    }
  environment {
      IMAGE_REPO = "adiachan/microblog"
      def IMAGE_TAG = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
  }
  stages {

    stage('Kaniko Build & Push Image') {
      steps {
        container('kaniko') {
          script {
            sh '''
            /kaniko/executor --dockerfile `pwd`/Dockerfile \
                             --context `pwd` \
                             --destination=${IMAGE_REPO}:${IMAGE_TAG}
            '''
          }
        }
      }
    }
    stage('Deploy') {
      environment {
        GIT_CREDS = credentials('github')
        GIT_REPO_URL = '$GIT_CREDS_USR:$GIT_CREDS_PSW@github.com/namesjc/homelab.git'
        GIT_REPO_EMAIL = 'adiachan@outlook.com'
        GIT_REPO_BRANCH = '23-API'
        // GIT_REPO_BRANCH = "master"

      }
      steps {
        container('tools') {
            sh "git clone https://${GIT_REPO_URL}"
            sh "git config --global user.email ${GIT_REPO_EMAIL}"
            // sh "git checkout -b master"
          dir("homelab") {
            // sh "git checkout ${GIT_REPO_BRANCH}"
            //install done
            sh '''#!/bin/bash
              echo $GIT_REPO_EMAIL
              echo $GIT_COMMIT
              ls -lth
              cd ./apps/microblog
              yq eval '.microblog.main.image.repository = ${IMAGE_REPO}' -i values.yaml
              yq eval '.microblog.main.image.tag = ${IMAGE_TAG}' -i values.yaml
              cat values.yaml
              pwd
              git commit -am 'Publish new version' && git push || echo 'no changes'
            '''
          }
        }
      }
    }
  }
}
