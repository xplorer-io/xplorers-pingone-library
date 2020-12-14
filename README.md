## Xplorers PingOne Directory Library

This library is for usage with XplorersBot to enroll and unenroll Xplorers as they join/leave Xplorers Slack group.

### Install pipenv packages

```
make install
```

### Prerequisites

Fetch these secrets from PingOne to initialize the XplorersPingOne class,

* `pingone_dir_client_id` - Client ID of the PingOne Directory in use.
* `pingone_dir_api_key` - PingOne Directory API key for authentication.

### Getting started

* Initialize the XplorersPingOne class as follows,
  ~~~ python3
  init_xplorers_pingone = XplorersPingOne(
    pingone_dir_client_id=pingone_dir_client_id,
    pingone_dir_api_key=pingone_dir_api_key
  )
  ~~~

* Get all PingOne Directory groups
  ~~~ python3
  init_xplorers_pingone.get_groups()
  ~~~

* Search a group by name
  ~~~ python3
  init_xplorers_pingone.get_group_by_name("some-group-name")
  ~~~

* Search a group by ID
  ~~~ python3
  init_xplorers_pingone.get_group_by_id("some-group-id")
  ~~~

* Search a group by searching for a group name that starts with
  ~~~ python3
  init_xplorers_pingone.get_groups_by_starts_with("arn:")
  ~~~

* Invite a new user to Xplorers PingOne.
  ~~~ python3
  init_xplorers_pingone.invite_user("user-email-address")
  ~~~

* Add a user to a group
  ~~~ python3
  init_xplorers_pingone.add_user_to_group("some-user-id", "some-group-id)
  ~~~

### How to build python package before pushing upstream after making changes

* Update `setup.py` with a new version.
* Use the command `python3 setup.py sdist bdist_wheel` to build the package.
* Add and commit to Github.
