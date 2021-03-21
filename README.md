# pypackagetemplate

**A cookiecutter template for a python databricks package.**

This repo can be used to create the simple file and directory structure for a python package.

## Usage

### Requirements
In order to use this template, you will need to install the `cookiecutter` python package:
```
pip install cookiecutter>=1.7.2
```
or
```
pip install -r requirements.txt
```
### Generating your repo
Then, from within the directory where you would like to create a new repo, run the following:
```
cookiecutter /path/to/pypackagetemplate
```

This will then prompt you for how to populate various values which will be used to generate your repo.

The repo will then be created in the directory you are in, with the name you specified in the prompts.

For example, if I run `cookiecutter /path/to/package-template` from within my `/home/user/Documents/git` directory and specify `template_demo123` as my `repo_name`, then a new directory will be created `/home/user/Documents/git/template_demo123`.

### Initialising the repo with git
In order to initialise this as a git repository, you will need to run one of the following (where template_demo123 may replace your repo name):

Using ssh for authentication (likely with Linux):
```
git init
git remote add origin git@ssh.dev.azure.com:v3/redslim/Redslim/template_demo123
git push -u origin --all
```

Using https for authentication (likely with Windows):
```
git init
git remote add origin https://redslim@dev.azure.com/redslim/Redslim/_git/template_demo123
git push -u origin --all
```
You will then need to add and commit all of the files to git as you want.
