INSERT INTO checkpoints
values
    (1, 'Create a repository', 'Congraluations on creating your github account, Create a repository
    <small class="text-muted">This is the place where all the files are stored</small>', 'check_repo', 5);

INSERT INTO checkpoints
values
    (2, 'Add a README.md file', 'After creating the repository, create a new file in it and name it README.md
    <small class="text-muted">README.md file helps other users to read and understand what the repository does or contains</small>', 'check_commit_web', 10);

INSERT INTO checkpoints
values
    (3, 'Quiz: Clone the repo', '
    <div class="form-text">Now if you want to add some files or modify the present files in your local machine or use this repository locally then you must clone this repository using the git clone command</div>
    <div class="form-group">
    <label for="question">Which command did you run to clone your repository created in the first checkpoint?</label>
    <input type="text" class="form-control" name="clone_url">
    <small class="form-text text-muted">run $git clone :url</small>
</div>', 'check_quiz_1', 10);

INSERT INTO checkpoints
values
    (4, 'Quiz: Analyse the remote urls', '
    <div class="form-text">git uses remote urls to track the repository which is in github, by default there is <i>origin</i> which points to the remote repository which you just cloned from github</div>
    <label for="question">What is the fetch url of the local repository?</label>
    <input type="text" class="form-control" name="fetchurl">
    <small class="form-text text-muted">this is the url from where git fetches the updates </small>
    <label for="question">What is the push url of the local repository?</label>
    <input type="text" class="form-control" name="pushurl">
    <small class="form-text text-muted">This is the url to which the git pushes updates</small>
    <small class="form-text text-muted">you can list the remotes available by running <i> git remote -v</i></small>
</div>', 'check_quiz_2', 10);







