# git-appraise-test

This repository is used for testing the JupyterLab Notebook Comments in Git Extension, which uses [git-appraise](https://github.com/google/git-appraise).

## Useful git-appraise commands:


Add a detached comment
```console
git appraise comment -d -m "{MESSAGE}" -f {FILE_PATH_FROM_REPO_ROOT}
```

Add a detached reply comment
```console
git appraise comment -d -p {HASH_OF_COMMENT_TO_REPLY_TO} -m "{MESSAGE}" -f {FILE_PATH_FROM_REPO_ROOT}
```

Fetch detached comments for a particular file, JSON format
```console
git appraise show -d -json -f {FILE_PATH_FROM_REPO_ROOT}
```

Pull new comments from the remote repo
```console
git appraise pull {REMOTE_REPO}
```

Push new comments to the remote repo
```console
git appraise push ${REMOTE_REPO}
```
