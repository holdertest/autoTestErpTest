*** Settings ***
Library           Collections
Library           json
Library           demjson
Library           ../apitest/HardwareRelate.py
Library           ../common/Generator.py

*** Variables ***

*** Test Cases ***
case1
    ${data}    authorize_check
    ${data}    Loads    ${data}
    ${ApiNote}    Get From Dictionary    ${data}    ApiNote
    log    ${ApiNote}
    ${ResultMsg}    Get From Dictionary    ${ApiNote}    ResultMsg
    ${NoteMsg}    Get From Dictionary    ${ApiNote}    NoteMsg
    Should Be Equal    ${ResultMsg}    成功
    Should Be Equal As Strings    ${NoteMsg}    OK

case2
    ${headers}=    login
    ${l1}    create list
    ${string}    generateAllRule    8
    append to list    ${l1}    ${string}
    ${string}    generateAllRule    8
    append to list    ${l1}    ${string}
    log    ${l1}

case3
    ${data}    authorizecheck
    log    ${data}
    ${apinote}    Get From Dictionary    ${data}    ApiNote
    log    ${apinote}

*** Keywords ***
