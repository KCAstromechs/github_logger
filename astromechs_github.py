from github import Github

github_key = ''

# Filename that contains the github key
github_key_filename = 'github_key.txt'

with open(github_key_filename, 'r') as f:
    github_key = f.readline()
    github_key = github_key.replace('\n', '')

#Ensure we did get something
assert (github_key), 'Could not find github key'

github_obj = Github(github_key)

organization = github_obj.get_organization('KCAstromechs')

#Print some info about the organization that we're connecting to
print(f'Connecting to {organization.name}')

for member in organization.get_members():
    print(member.login)

for repo in organization.get_repos():
    #Create or open and overwrite a file with the same name as each repository
    repo_filename = f'{repo.name}.txt'
    with open(repo_filename, 'w') as f:
        commits = []
        for commit in repo.get_commits():
            #For each commit on the repo get the author, timestamp, and commit message
            statuses = commit.get_statuses()
            time_stamp = ''
            for status in statuses:
                time_stamp = f' at {statuses[0].created_at.fromisoformat("YYYY-MM-DD")}'
                break
            commit_str = f'{commit.commit.author}{time_stamp}: {commit.commit.message}'
            commits.append(commit_str)
        #Write all the commits to the file
        f.writelines(commits)
