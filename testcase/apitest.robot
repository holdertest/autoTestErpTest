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
    ResultCheck    ${data}    成功    OK

EquipmentsBAuthorizeCheck
    ${data}    equipmentsb_authorizecheck
    ResultCheck    ${data}    成功    OK

EquipmentsBGetInfo
    ${data}    equipmentsb_getinfo
    ResultCheck    ${data}    业务成功    业务成功

StoreBGetList
    ${data}    storeb_getlist
    ResultCheck    ${data}    成功    OK

UserBNewLogin
    ${data}    userb_newlogin
    ResultCheck    ${data}    成功    OK：查询成功

DishesTypeBGetList
    ${data}    dishestypeb_getlist
    ResultCheck    ${data}    成功    OK

test
    ${data}    dishestypeb_getlist
    ResultCheck    ${data}    成功    OK

*** Keywords ***
ResultCheck
    [Arguments]    ${arg1}    ${arg2}    ${arg3}
    ${data}    Loads    ${arg1}
    ${ApiNote}    Get From Dictionary    ${data}    ApiNote
    log    ${ApiNote}
    ${ResultMsg}    Get From Dictionary    ${ApiNote}    ResultMsg
    ${NoteMsg}    Get From Dictionary    ${ApiNote}    NoteMsg
    log    ${ResultMsg}
    log    ${NoteMsg}
    Should Be Equal As Strings    ${ResultMsg}    ${arg2}
    Should Be Equal As Strings    ${NoteMsg}    ${arg3}
