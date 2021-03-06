#!groovy

@Library('emt-pipeline-lib@master') _

repo_creds = 'emt-jenkins-github-ssh'
repo_url = 'git@github.com:hlaf/apcupsd.git'
yum_repo_url = 'http://nexus.emtegrity.com:8082/repository/emt-yum-3rdparty'
version = '3.14.14-2'

node('docker-slave') {
  
  stage('Checkout') {
	checkoutFromGit(repo_creds, repo_url)
  }
  
  def build_tools_image = 'centos-devtools32'
  stage('Build Image') {
    def customImage = docker.build(build_tools_image, './EBuild')
  }

  stage('Verify SPEC file') {
    sh "docker run -t --volumes-from $DOCKER_CONTAINER_ID $build_tools_image \
      /bin/sh -c 'cd ${env.WORKSPACE}/EBuild && \
                  rpmlint apcupsd.spec'\
    "
  }

  stage('Build RPM') {
    sh "docker run -t --volumes-from $DOCKER_CONTAINER_ID $build_tools_image \
      /bin/sh -c 'cd ${env.WORKSPACE}/EBuild && \
        rpmdev-setuptree && \
        ln -s ${env.WORKSPACE}/RECEIVED/apcupsd-3.14.14.tar.gz /root/rpmbuild/SOURCES && \
        rpmbuild -bb --define \"debug_package %{nil}\" --define \"_ebuild_root ${env.WORKSPACE}/EBuild\" apcupsd.spec --target i386 && \
        mv /root/rpmbuild/RPMS/i386/*.rpm .'\
    "
    sh 'ls ./EBuild'
  }

  stage('Verify RPM') {
    sh "docker run -t --volumes-from $DOCKER_CONTAINER_ID $build_tools_image \
      /bin/sh -c 'cd ${env.WORKSPACE}/EBuild && \
                  rpmlint -f .rpmlint.waivers *.rpm'\
    "
  }

  stage('Deploy to Yum repo') {
    if (isBuildReplayed() || isBuildStartedByTimer()) {
      echo "Skipping release"
    } else {
      withCredentials([usernamePassword(credentialsId: 'nexus-credentials',
                                        usernameVariable: 'USERNAME',
                                        passwordVariable: 'PASSWORD')]) {
         sh "curl --fail -v --user '${USERNAME}:${PASSWORD}' --upload-file ./EBuild/apcupsd-${version}.el6.i386.rpm ${yum_repo_url}/i386/apcupsd-${version}.el6.i386.rpm"
      }
    }
  }

}
