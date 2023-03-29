# What types of commits and pushes can I do?

The <type> can be one of the following:

    feat: A new feature
    fix: A bug fix
    docs: Documentation changes
    style: Changes to the formatting or style
    refactor: Code changes that neither fixes a bug nor adds a feature
    test: Adding missing or correcting existing tests
    chore: Changes to the build process or other project-related tasks

The <short summary> should be a concise, descriptive summary of the changes made in the commit.

The <longer description> provides more context and explanation of the changes made in the commit.

The [optional body] provides additional details or justification for the changes made.

The [optional footer] can be used for any closing remarks or to reference issues or pull requests related to the commit.

It's important to note that a well-crafted commit message can help make your project more understandable and maintainable for yourself and other contributors.

# How do I make a commit in Visual Studio code?

To make a Git commit in Visual Studio Code, you can follow these steps:

    Open the file you want to commit in Visual Studio Code.
    Open the Source Control panel by clicking on the Source Control icon in the left sidebar (it looks like a branch with a circle around it).
    In the Source Control panel, you should see your file listed under "Changes". Click the "+" icon next to the file to stage it for the commit.
    Enter a commit message in the text box at the top of the panel. This should be a short, descriptive message that explains what changes you made.
    Click the checkmark icon at the top of the panel to commit your changes.

## Alternatively, you can also use the Git command line to make a commit. 

You can do this by opening the  terminal in Visual Studio Code and running the following commands:

    git init
    git add <filename> to stage your changes
    git commit -m "commit message" to make the commit with your message

Replace <filename> with the name of your file, and replace "commit message" with a short, descriptive message that explains what changes you made

# If you are updating a file

To commit changes to a file in Git, you can follow these general steps:

    Make changes to the file using your code editor or other text editor.
    Save the changes to the file.
    Use the command git add <filename> to stage the changes for the commit. If you want to stage all changes in the repository, you can use git add . instead.
    Use the command git commit -m "commit message" to commit the changes with a message that describes the changes you made.
    Use the command **git push** to push the changes to the remote repository (e.g. GitHub, Bitbucket, etc.).

    It's two steps, commit to the change, then push the change.

## you should always finish your coding session with a COMMIT and PUSH to keep your project up to date.

# **Git Pull**

## It's a good idea, when you are working with an online repository to get the lastest updates before starting work

The **git pull** command is used to update your local repository with changes from the remote repository. This command combines the git fetch command, which retrieves the latest changes from the remote repository, and the git merge command, which merges those changes into your local repository.

When you run **git pull**, Git will download the latest changes from the remote repository and merge them into your current branch. If there are conflicts between the changes on the remote repository and your local changes, you may need to resolve those conflicts manually before you can commit and push your changes.

It's a good practice to run **git pull** before starting to work on any new changes to make sure that you are working with the most up-to-date version of the code.
