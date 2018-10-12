#!groovy

@Library('emt-pipeline-lib@master') _

repo_creds = 'emt-jenkins-git-ssh'
repo_url = 'git@github.com:hlaf/apcupsd.git'

node('docker-slave') {
  
  stage('Checkout') {
	checkoutFromGit(repo_creds, repo_url)
  }
  
  stage('BuildImage') {
    def build_tools_image = 'centos-devtools32'
    def customImage = docker.build(build_tools_image, './EBuild')
    sh "docker run -t --volumes-from $DOCKER_CONTAINER_ID $build_tools_image /bin/sh -c 'cd ${env.WORKSPACE}/EBuild; make Release_Linux32'"
    sh 'ls ./EBuild'
  }

}
