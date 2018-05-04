*** Settings ***
Library           Collections
Library           json
Library           ../apitest/EquipmentsBAuthorizeCheck.py
Library           ../apitest/EquipmentsBGetBinding.py
Library           ../apitest/EquipmentsBGetInfo.py
Library           ../apitest/StoreBGetList.py
Library           ../apitest/UserBNewLogin.py

*** Variables ***

*** Test Cases ***
EquipmentsBGetBinding
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

EquipmentsBAuthorizeCheck
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

EquipmentsBGetInfo
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

StoreBGetList
    ${data}    get_list
    ${data}    Loads    ${data}
    ${ApiNote}    Get From Dictionary    ${data}    ApiNote
    log    ${ApiNote}
    ${ResultMsg}    Get From Dictionary    ${ApiNote}    ResultMsg
    ${NoteMsg}    Get From Dictionary    ${ApiNote}    NoteMsg
    log    ${ResultMsg}
    log    ${NoteMsg}
    Should Be Equal    ${ResultMsg}    成功
    Should Be Equal As Strings    ${NoteMsg}    OK

UserBNewLogin
    ${data}    new_login
    ${data}    Loads    ${data}
    ${ApiNote}    Get From Dictionary    ${data}    ApiNote
    log    ${ApiNote}
    ${ResultMsg}    Get From Dictionary    ${ApiNote}    ResultMsg
    ${NoteMsg}    Get From Dictionary    ${ApiNote}    NoteMsg
    log    ${ResultMsg}
    log    ${NoteMsg}
    Should Be Equal    ${ResultMsg}    成功
    Should Be Equal As Strings    ${NoteMsg}    OK

*** Keywords ***
