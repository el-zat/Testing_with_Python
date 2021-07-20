*** Settings ***
Library rf.Addressbook
Suite Setup Init Fixtures
Suite Teardown Destroy Fixtures

*** Test Cases ***
Ann new group
    Create Group name1, header1, footer1

