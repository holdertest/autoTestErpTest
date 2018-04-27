*** Settings ***
Library           Collections
Library           ../apitest/HardwareRelate.py
Library           ../common/Generator.py

*** Variables ***

*** Test Cases ***
case1
    ${headers}=    authorizecheck

case2
    ${headers}=    login
    ${l1}    create list
    ${string}    generateAllRule    8
    append to list    ${l1}    ${string}
    ${string}    generateAllRule    8
    append to list    ${l1}    ${string}
    log    ${l1}

*** Keywords ***
