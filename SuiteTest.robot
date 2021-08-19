*** Settings ***

Library     Interview.py

*** Variables ***
${username}   test
${password}   password
${path}
${key}
${val}
${valType}
${status_code}

*** Test Cases ***

rest_api_login
    [Documentation]  NCM rest api login needed to access the api in coming robot test cases
    ${token}=  Interview.login    ${username}   ${password}

    Run Keyword If   ${token}==${none}   Fatal Error   Cant Succeed To login, Check Error.
    Set Suite Variable   ${token}     ${token}

create_items
    ${body}=   Interviw.get_body       key=key      val=val     valType=valType
    ${rc}=  Interview.post    ${token}     ${body}       ${path}
    Run Keyword If   ${rc}[1]!=${status_code}   Fatal Error   Cant Succeed To Post.
    Log     ${rc}[0]['id']

    Set Suite Variable   ${idCreated}    ${rc}[0]['id']

Delete Item Create
    ${items}=    Interview.delete    ${token}    ${idCreated}
    Should Be Equal  ${items}==204

