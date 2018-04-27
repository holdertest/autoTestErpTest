*** Settings ***
Library           Collections
Library           ../story/Warehouse.py
Library           ../common/Login.py
Library           ../common/Generator.py

*** Variables ***

*** Test Cases ***
case1
    ${headers}=    login

case2
    ${headers}=    login
    ${l1}    create list
    ${string}    generateAllRule    8
    append to list    ${l1}    ${string}
    ${string}    generateAllRule    8
    append to list    ${l1}    ${string}
    log    ${l1}

case3
*** Keywords ***
