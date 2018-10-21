#!groovy

@Library('emt-pipeline-lib@master') _

repo_creds = 'emt-jenkins-git-ssh'
repo_url = 'git@github.com:hlaf/apcupsd.git'

node('docker-slave') {
  
  stage('Checkout') {
	checkoutFromGit(repo_creds, repo_url)
  }
  
  def build_tools_image = 'centos-devtools32'
  stage('Build Image') {
    def customImage = docker.build(build_tools_image, './EBuild')
  }

  stage('Build RPM') {
    sh "docker run -t --volumes-from $DOCKER_CONTAINER_ID $build_tools_image \
      /bin/sh -c 'cd ${env.WORKSPACE}/EBuild && \
        rpmdev-setuptree && \
        ln -s ${env.WORKSPACE}/RECEIVED/apcupsd-3.14.14.tar.gz /root/rpmbuild/SOURCES && \
        ls -al /root/rpmbuild/SOURCES && \
        rpmbuild -ba --define \"_ebuild_root ${env.WORKSPACE}/EBuild\" apcupsd.spec --target i386'"
    sh 'ls ./EBuild'
  }

}

