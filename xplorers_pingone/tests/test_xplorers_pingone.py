"""
Unit tests for Xplorers PingOne library
"""

from unittest import TestCase
from unittest.mock import patch

from xplorers_pingone import XplorersPingOne

class XplorersPingOneTest(TestCase):
    """
    PingOne test suite
    """
    @patch("xplorers_pingone.b64encode")
    def setUp(self, b64encode_mock):
        self.b64encode_mock = b64encode_mock
        self.init_pingone = XplorersPingOne(
            "some-client-id",
            "some-api-key"
        )

    @patch("xplorers_pingone.loads")
    @patch("xplorers_pingone.requests")
    def test_invite_user(self, requests_mock,
                         loads_mock):
        """ module --> invite_user """
        sample_email_address = "coolXplorer@gmail.com"

        loadify_result = {"value": "https://login.pingone.com/idp/directory/a/440bde6f-4242-4004-8fdf-0ee639157859/registration/confirm/1d65ed24-2e28-493a-b460-5e34af5c3782/e5c22c4a-8c02-4aac-8718-77e03f61172d/"}

        loads_mock.return_value = loadify_result

        response = '{"value": "https://login.pingone.com/idp/directory/a/440bde6f-4242-4004-8fdf-0ee639157859/registration/confirm/1d65ed24-2e28-493a-b460-5e34af5c3782/e5c22c4a-8c02-4aac-8718-77e03f61172d/"}'

        requests_mock.post.return_value.content = response

        self.assertEqual(
            self.init_pingone.invite_user(sample_email_address),
            loadify_result
        )

    @patch("xplorers_pingone.loads")
    @patch("xplorers_pingone.requests")
    def test_get_groups(self, requests_mock,
                         loads_mock):
        """ module --> get_groups """
        loads_response = get_groups_response

        loads_mock.return_value = loads_response

        requests_mock.get.return_value.content = '{"resources": [{"id": "4fd74dab-823b-40f0-8768-b77d300ec2b8", "displayName": "arn:aws:iam::722704729150:role/XplorersSes,arn:aws:iam::722704729150:saml-provider/PingOneXplorers", "schemas": ["urn:scim:schemas:core:1.0", "urn:scim:schemas:com_pingone:1.0"], "meta": {"lastModified": "2020-11-12T19:48:15.177-07:00", "created": "2020-11-04T01:14:03.874-07:00", "location": "https://directory-api.pingone.com.au/v1/group/4fd74dab-823b-40f0-8768-b77d300ec2b8"}, "members": [{"value": "e68cc36b-d761-4159-a426-0e015e50f00e", "type": "user", "display": "7thnovravi@gmail.com"}, {"value": "81be1b19-894f-41ef-8124-819bcf43a463", "type": "user", "display": "abinash.shrestha09@gmail.com"}], "urn:scim:schemas:com_pingone:1.0": {"createTimeStamp": 1604477643874, "lastModifiedTimeStamp": 1605235695177, "accountId": "440bde6f-4242-4004-8fdf-0ee639157859", "directoryId": "2213a684-276a-4be9-95de-b5c9834a99a9"}}]}'

        self.assertEqual(
            self.init_pingone.get_groups(),
            loads_response["resources"]
        )

    @patch("xplorers_pingone.XplorersPingOne.get_groups")
    def test_get_group_by_name(self, get_groups_mock):
        """
        module --> get_group_by_name
        """
        get_groups_mock.return_value = get_groups_response["resources"]
        sample_group_name = "arn:aws:iam::722704729150:role/XplorersSes,arn:aws:iam::722704729150:saml-provider/PingOneXplorers"

        # Valid group name test
        self.assertEqual(
            self.init_pingone.get_group_by_name(sample_group_name),
            get_groups_response["resources"][0]
        )

        # Invalid group name test
        self.assertEqual(
            self.init_pingone.get_group_by_name("not-a-valid-group"),
            "Group with name not-a-valid-group not found!"
        )

    @patch("xplorers_pingone.XplorersPingOne.get_groups")
    def test_get_group_by_id(self, get_groups_mock):
        """ module --> get_group_by_id """
        get_groups_mock.return_value = get_groups_response["resources"]
        sample_group_id = "4fd74dab-823b-40f0-8768-b77d300ec2b8"

        # Valid group ID test
        self.assertEqual(
            self.init_pingone.get_group_by_id(sample_group_id),
            get_groups_response["resources"][0]
        )

        # Invalid group ID test
        self.assertEqual(
            self.init_pingone.get_group_by_id("not-a-valid-id"),
            "Group with ID not-a-valid-id not found!"
        )

    @patch("xplorers_pingone.XplorersPingOne.get_groups")
    def test_get_groups_by_starts_with(self, get_groups_mock):
        """ module --> get_groups_by_starts_with """
        get_groups_mock.return_value = get_groups_response["resources"]

        # Valid group
        self.assertEqual(
            self.init_pingone.get_groups_by_starts_with("arn:"),
            [get_groups_response["resources"][0]]
        )
 
        # Invalid group
        self.assertEqual(
            self.init_pingone.get_groups_by_starts_with("not-a-group"),
            []
        )

    @patch("xplorers_pingone.loads")
    @patch("xplorers_pingone.requests")
    def test_add_user_to_group(self, requests_mock,
                         loads_mock):
        """ module --> add_user_to_group """
        requests_mock.patch.return_value.content = '{"id": "390064f6-30ab-482d-9736-80297806a204", "displayName": "arn:aws:iam::020273681268:role/XplorersMas,arn:aws:iam::020273681268:saml-provider/PingOneXplorers", "schemas": ["urn:scim:schemas:core:1.0", "urn:scim:schemas:com_pingone:1.0"], "meta": {"lastModified": "2020-11-11T17:22:02.058-07:00", "created": "2020-11-04T01:21:33.710-07:00", "location": "https://directory-api.pingone.com.au/v1/group/390064f6-30ab-482d-9736-80297806a204"}, "members": [{"value": "e68cc36b-d761-4159-a426-0e015e50f00e", "type": "user", "display": "7thnovravi@gmail.com"}, {"value": "81be1b19-894f-41ef-8124-819bcf43a463", "type": "user", "display": "abinash.shrestha09@gmail.com"}, {"value": "84d4ccdf-3725-48e1-a125-bf85b96420b4", "type": "user", "display": "adroit_abhi@live.com"}, {"value": "fdeac31a-876f-4c09-a1cf-2e5c2a0834ae", "type": "user", "display": "yoozina.mrjn@gmail.com"}], "urn:scim:schemas:com_pingone:1.0": {"createTimeStamp": 1604478093710, "lastModifiedTimeStamp": 1605140522058, "accountId": "440bde6f-4242-4004-8fdf-0ee639157859", "directoryId": "2213a684-276a-4be9-95de-b5c9834a99a9"}}'

        loads_mock.return_value = add_user_to_group_response

        self.assertEqual(
            self.init_pingone.add_user_to_group(
                "some-user-id",
                "some-group-id"
            ),
            add_user_to_group_response
        )

get_groups_response = {
    "resources":[
        {
            "id":"4fd74dab-823b-40f0-8768-b77d300ec2b8",
            "displayName":"arn:aws:iam::722704729150:role/XplorersSes,arn:aws:iam::722704729150:saml-provider/PingOneXplorers",
            "schemas":[
                "urn:scim:schemas:core:1.0",
                "urn:scim:schemas:com_pingone:1.0"
            ],
            "meta":{
                "lastModified":"2020-11-12T19:48:15.177-07:00",
                "created":"2020-11-04T01:14:03.874-07:00",
                "location":"https://directory-api.pingone.com.au/v1/group/4fd74dab-823b-40f0-8768-b77d300ec2b8"
            },
            "members":[
                {
                    "value":"e68cc36b-d761-4159-a426-0e015e50f00e",
                    "type":"user",
                    "display":"7thnovravi@gmail.com"
                },
                {
                    "value":"81be1b19-894f-41ef-8124-819bcf43a463",
                    "type":"user",
                    "display":"abinash.shrestha09@gmail.com"
                }
            ],
            "urn:scim:schemas:com_pingone:1.0":{
                "createTimeStamp":1604477643874,
                "lastModifiedTimeStamp":1605235695177,
                "accountId":"440bde6f-4242-4004-8fdf-0ee639157859",
                "directoryId":"2213a684-276a-4be9-95de-b5c9834a99a9"
            }
        }
    ]
}

add_user_to_group_response = {
    'id':'390064f6-30ab-482d-9736-80297806a204',
    'displayName':'arn:aws:iam::020273681268:role/XplorersMas,arn:aws:iam::020273681268:saml-provider/PingOneXplorers',
    'schemas':[
        'urn:scim:schemas:core:1.0',
        'urn:scim:schemas:com_pingone:1.0'
    ],
    'meta':{
        'lastModified':'2020-11-11T17:22:02.058-07:00',
        'created':'2020-11-04T01:21:33.710-07:00',
        'location':'https://directory-api.pingone.com.au/v1/group/390064f6-30ab-482d-9736-80297806a204'
    },
    'members':[
        {
            'value':'e68cc36b-d761-4159-a426-0e015e50f00e',
            'type':'user',
            'display':'7thnovravi@gmail.com'
        },
        {
            'value':'81be1b19-894f-41ef-8124-819bcf43a463',
            'type':'user',
            'display':'abinash.shrestha09@gmail.com'
        },
        {
            'value':'84d4ccdf-3725-48e1-a125-bf85b96420b4',
            'type':'user',
            'display':'adroit_abhi@live.com'
        },
        {
            'value':'fdeac31a-876f-4c09-a1cf-2e5c2a0834ae',
            'type':'user',
            'display':'yoozina.mrjn@gmail.com'
        }
    ],
    'urn:scim:schemas:com_pingone:1.0':{
        'createTimeStamp':1604478093710,
        'lastModifiedTimeStamp':1605140522058,
        'accountId':'440bde6f-4242-4004-8fdf-0ee639157859',
        'directoryId':'2213a684-276a-4be9-95de-b5c9834a99a9'
    }
}
