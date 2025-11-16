*** Settings ***
Resource  C:/Users/path/to/robot/files.robot


Suite Setup  run keywords       Open Login Page
Test Teardown  Reload Page
Suite Teardown     close browser



*** Test Cases ***

Login without data
    Element Should Be Disabled    ${LOGIN_BUTTON}

Login with invalid data
    Input Invalid Login
    Input Invalid Password
    Click Login Button
    wait until page contains    Login lub hasło jest nieprawidłowe
    Page should contain   Login lub hasło jest nieprawidłowe


Login without password
    Input Valid Login
    Element Should Be Disabled    ${LOGIN_BUTTON}




Login without user_name
    Input Valid Password
    Element Should Be Disabled    ${LOGIN_BUTTON}



Valid login
    Input Valid Login
    Input Valid Password
    Click Login Button
    Assert User Logo





