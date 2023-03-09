from github import Github
from Configs.secrets_config import GITHUB_PAT
from Configs.config import ORG_NAME
from Utils.utils import getCurrentSeason


def createOrg():
    global ORG_NAME
    # SET THIS VARIABLE IN YOUR ENVIRONMENT VARIABLES
    g = Github(GITHUB_PAT)

    ORG_NAME = getOrgName()


# ================= THIS CODE DOESN'T WORK SOMEHOW ==================================
    # Replace YOUR_ORGANIZATION_NAME with the name of the organization you want to create
    # org = g.create_organization(ORG_NAME,
    #                             login=ORG_NAME, 
    #                             description="This is {} created on {}".format(),
    #                             has_organization_projects=True, 
    #                             has_repository_projects=True, 
    #                             default_repository_permission="admin", 
    #                             members_can_create_repositories=False,
    #                             visibility="private")

    # Replace YOUR_ORGANIZATION_NAME with the name of the organization you want to create
    print(g.get_organization("CSE511-SPRING-2023"))

    print("Organization: {} was successfully created!".format({ORG_NAME}))


if __name__ == "__main__":
    createOrg()