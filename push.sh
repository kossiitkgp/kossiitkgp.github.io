#!/bin/sh

setup_git() {
  git config --global user.email "contact@kossiitkgp.in"
  git config --global user.name "KOSS"
}

commit_website_files() {
  git checkout -b master
  git add index.html
  git commit --message "update no"
}

upload_files() {
  git remote add origin-here https://${OUATH_KEY}@github.com/kossiitkgp/kossiitkgp.github.io.git
  git push --quiet --set-upstream origin-here master 
}

setup_git
commit_website_files
upload_files