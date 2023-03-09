from github import Github, UnknownObjectException
from Configs.config import MANDATORY_GITHUB_ADMINS
from Configs.grading_config import REPO_NAMES
from Configs.secrets_config import GITHUB_PAT
from GitHubSetup.gitHubUtils import getOrgName, readGitHubUserNames



def createRepository(assignment_number):
    g = Github(GITHUB_PAT)

    # Replace YOUR_ORGANIZATION_NAME with your organization na
    orgName = getOrgName()
    print("Creating Repositories under {} Organization".format(orgName))

    try:
        org = g.get_organization(orgName)
    except UnknownObjectException as e:
        print(f"Error {e.status}: {orgName} {e.data['message']}")
        print("Please create GitHub organization with the name as: {}".format(orgName))

    usernames = readGitHubUserNames()

    
    for username in usernames:  

        try: 
            repo = org.create_repo(
                REPO_NAMES.format(
                username, assignment_number
                )
                ,private=True
            )
        except Exception as e:
            print(f"Error {e.status}: {e.data['message']}")
        try:
            # Give the user access to the repository
            repo.add_to_collaborators(username, permission="push")

            # ADD PROFESSOR, AMEY AS ADMIN TO REPOS
            for adminUser in MANDATORY_GITHUB_ADMINS:
                repo.add_to_collaborators(adminUser, permission="admin")

            print("Created branch for {} with the name {}".format(
                username,
                REPO_NAMES.format(
                username, assignment_number
                )            
            ))
        except Exception as e:
            print(f"Failed creating repository for {username}")
    print("All repositories created Successfully")



if __name__ == "__main__":
    pass