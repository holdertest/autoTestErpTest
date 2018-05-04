*** Settings ***
Library           Collections
Library           json
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
    log    ${ResultMsg}
    log    ${NoteMsg}
    Should Be Equal    ${ResultMsg}    成功
    Should Be Equal As Strings    ${NoteMsg}    OK

AuthorizeCheck
    ${data}    authorize_check
    ${data}    Loads    ${data}
    ${ApiNote}    Get From Dictionary    ${data}    ApiNote
    log    ${ApiNote}
    ${ResultMsg}    Get From Dictionary    ${ApiNote}    ResultMsg
    ${NoteMsg}    Get From Dictionary    ${ApiNote}    NoteMsg
    log    ${ResultMsg}
    log    ${NoteMsg}
    Should Be Equal    ${ResultMsg}    成功
    Should Be Equal As Strings    ${NoteMsg}    OK

GetInfo
    ${data}    get_info
    ${data}    Loads    ${data}
    ${ApiNote}    Get From Dictionary    ${data}    ApiNote
    log    ${ApiNote}
    ${ResultMsg}    Get From Dictionary    ${ApiNote}    ResultMsg
    ${NoteMsg}    Get From Dictionary    ${ApiNote}    NoteMsg
    log    ${ResultMsg}
    log    ${NoteMsg}
    Should Be Equal As Strings    ${ResultMsg}    业务成功
    Should Be Equal As Strings    ${NoteMsg}    业务成功

*** Keywords ***
登录
