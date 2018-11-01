#!groovy

@Library('emt-pipeline-lib@master') _

repo_creds = 'emt-jenkins-git-ssh'
repo_url = 'git@github.com:hlaf/apcupsd.git'
yum_repo_url = 'http://nexus.emtegrity.com:8082/repository/emt-yum-3rdparty'

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
        rpmbuild -ba --define \"_ebuild_root ${env.WORKSPACE}/EBuild\" apcupsd.spec --target i386 && \
        mv /root/rpmbuild/RPMS/i386/*.rpm .'\
    "
    sh 'ls ./EBuild'
  }

  stage('Deploy to Yum repo') {
    sh "curl -v --user 'USER:PASS' --upload-file ./EBuild/apcupsd-3.14.14-1.el6.i386.rpm ${yum_repo_url}/i386/apcupsd-3.14.14-1.el6.i386.rpm"
  }

}

