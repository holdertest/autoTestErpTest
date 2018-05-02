*** Settings ***
Library           Collections
Library           json
Library           demjson
Library           ../apitest/HardwareRelate.py
Library           ../common/Generator.py

*** Variables ***

*** Test Cases ***
GetBinding
    ${data}    get_binding
    ${data}    Loads    ${data}
    ${ApiNote}    Get From Dictionary    ${data}    ApiNote
    log    ${ApiNote}
    ${ResultMsg}    Get From Dictionary    ${ApiNote}    ResultMsg
    ${NoteMsg}    Get From Dictionary    ${ApiNote}    NoteMsg
    Should Be Equal    ${ResultMsg}    成功
    Should Be Equal As Strings    ${NoteMsg}    OK

AuthorizeCheck
    ${data}    get_binding
    ${data}    Loads    ${data}
    ${ApiNote}    Get From Dictionary    ${data}    ApiNote
    log    ${ApiNote}

GetInfo
    ${data}    get_binding
    ${data}    Loads    ${data}
    ${ApiNote}    Get From Dictionary    ${data}    ApiNote
    log    ${ApiNote}

*** Keywords ***
