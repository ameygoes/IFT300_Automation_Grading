from github import Github, UnknownObjectException
from Configs.grading_config import REPO_NAMES
from Configs.secrets_config import GITHUB_PAT
from GitHubSetup.gitHubUtils import getOrgName, readGitHubUserNames


def deleteRepository(assignment_number):

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
        repo_name = REPO_NAMES.format(
                username, assignment_number
                ) 
        # Try to retrieve the repository object
        try:
            repo = org.get_repo(repo_name)
        
        except UnknownObjectException:
            print(f"Repository '{repo_name}' not found.")
        
        else:
            # Delete the repository
            repo.delete()
            print(f"Repository '{repo_name}' deleted successfully.")

    print("All repositories deleted Successfully")
