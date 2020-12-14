"""
Helper class to interact with PingOne Directory APIs
"""
import requests
from base64 import b64encode
from json import dumps, loads

class XplorersPingOne():
    """
    Class for interacting with PingOne Directory APIs
    """

    def __init__(self, pingone_dir_client_id, pingone_dir_api_key):
        self.pingone_api_base_url = "https://directory-api.pingone.com.au/api/directory"
        self.pingone_invite_user_suffix = "/useractions/invite"
        self.pingone_group_suffix = "/group"

        ## Base64 encoding needed for auth (client_id:api_key)
        self.auth_construct = f"{pingone_dir_client_id}:{pingone_dir_api_key}"
        auth_construct_in_bytes = bytes(self.auth_construct, "utf-8")
        self.auth = b64encode(auth_construct_in_bytes).decode("utf-8")
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Basic {self.auth}"
        }

    def invite_user(self, email_address):
        """
        Invite a new user to PingOne.

        Args:
            email_address ([String]): Email address of the new user to be invited to PingOne
        """
        data = {
            "email" : email_address
        }

        response = requests.post(
            self.pingone_api_base_url + self.pingone_invite_user_suffix,
            headers=self.headers,
            data=dumps(data)
        )

        return loads(response.content)

    def get_groups(self):
        """
        Get all PingOne Directory groups

        Returns:
            [Dictionary]: PingOne Directory groups and their details
        """
        response = requests.get(
            self.pingone_api_base_url + self.pingone_group_suffix,
            headers=self.headers
        )

        return loads(response.content)["resources"]

    def get_group_by_name(self, group_name):
        """
        Get PingOne Directory group information
        -> search by name
        Args:
            group_name ([String]): Name of PingOne Directory Group

        Returns:
            [Dictionary]: Details of the group including users part of the group
        """
        all_groups = self.get_groups()

        for group in all_groups:
            if group["displayName"] == group_name:
                return group

        return f"Group with name {group_name} not found!"

    def get_group_by_id(self, group_id):
        """
        Get PingOne Directory group information
        -> search by id
        Args:
            group_id ([String]): UUID formatted string of PingOne Directory Group

        Returns:
            [Dictionary]: Details of the group including users part of the group
        """
        all_groups = self.get_groups()

        for group in all_groups:
            if group["id"] == group_id:
                return group

        return f"Group with ID {group_id} not found!"

    def get_groups_by_starts_with(self, starts_with_string):
        """
        Get a PingOne Directory group(s) information
        -> search by string that the group name starts with

        Args:
            starts_with_string ([String]): A string to search for in directory group names

        Returns:
            [List]: List of groups that match the given string pattern including users part of the group
        """
        all_groups = self.get_groups()

        matched_groups = []

        for group in all_groups:
            if group["displayName"].startswith(starts_with_string):
                matched_groups.append(group)

        return matched_groups

    def add_user_to_group(self, user_id, group_id):
        """
        Add a user to a group

        Args:
            user_id ([String]): ID of the user
            group_id ([String]): ID of the group
        """
        data = {
            "members": [{"value": user_id, "type" : "User"}]
        }

        response = requests.patch(
            self.pingone_api_base_url + self.pingone_group_suffix + f"/{group_id}",
            headers=self.headers,
            data=dumps(data)
        )

        return loads(response.content)
