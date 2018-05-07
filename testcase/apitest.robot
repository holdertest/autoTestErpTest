*** Settings ***
Library           Collections
Library           json
Library           ../apitest/EquipmentsBAuthorizeCheck.py
Library           ../apitest/EquipmentsBGetBinding.py
Library           ../apitest/EquipmentsBGetInfo.py
Library           ../apitest/StoreBGetList.py
Library           ../apitest/UserBNewLogin.py
Library           ../apitest/DishesTypeBGetList.py

*** Variables ***

*** Test Cases ***
EquipmentsBGetBinding
    ${data}    equipmentsb_getbinding
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
    ${data}    equipmentsb_authorizecheck
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
    ${data}    equipmentsb_getinfo
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
    ${data}    storeb_getlist
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
    ${data}    userb_newlogin
    ${data}    Loads    ${data}
    ${ApiNote}    Get From Dictionary    ${data}    ApiNote
    log    ${ApiNote}
    ${ResultMsg}    Get From Dictionary    ${ApiNote}    ResultMsg
    ${NoteMsg}    Get From Dictionary    ${ApiNote}    NoteMsg
    log    ${ResultMsg}
    log    ${NoteMsg}
    Should Be Equal    ${ResultMsg}    成功
    Should Be Equal As Strings    ${NoteMsg}    OK：查询成功

DishesTypeBGetList
    ${data}    dishestypeb_getlist
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
