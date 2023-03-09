from github import Github, UnknownObjectException
from Configs.secrets_config import GITHUB_PAT
from GitHubSetup.gitHubUtils import getOrgName, readGitHubUserNames

def addStudents():
    g = Github(GITHUB_PAT)
    # Replace YOUR_ORGANIZATION_NAME with your organization na
    orgName = getOrgName()
    print("Adding members to {}".format(orgName))

    try:
        org = g.get_organization(orgName)

    except UnknownObjectException as e:

        print(f"Error {e.status}: {orgName} {e.data['message']}")
        print("Please create GitHub organization with the name as: {}".format(orgName))

    # Replace <org_name> with the name of your organization
    usernames = readGitHubUserNames()

    # Add each user to the organization
    for username in usernames:
        try:
            user = g.get_user(username)
            org.add_to_members(user, role="member")
            print(f"User '{username}' added to organization '{orgName}' successfully.")
        except UnknownObjectException:
            print(f"User '{username}' not found.")

if __name__ == "__main__":
    addStudents()