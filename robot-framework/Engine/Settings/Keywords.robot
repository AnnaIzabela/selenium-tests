*** Settings ***
Resource   C:/Users/path/to/robot/files.robot

Resource  Engine/Settings/Settings.robot

*** Keywords ***
Open Login Page
    Open Browser    ${URL}  ${BROWSER}

Input Valid Login
    Input text      ${USER_NAME}        user_email@example.com

Input Invalid Login
    Input text      ${USER_NAME}        dochrupania

Input Valid Password
    Input text      ${PASSWORD}     user_login

Input Invalid Password
    Input text    ${PASSWORD}       marchewka


Click Login Button
    Click Button    ${LOGIN_BUTTON}

Assert User Logo
    wait until element is visible   xpath=//div[@class='logo-container']
    page should contain element     xpath=//div[@class='logo-container']

Assert Empty Login Text
    wait until element is visible   ${LOGIN_BUTTON}
    wait until element is visible    Pole 'login' jest wymagane
    page should contain element      Pole 'login' jest wymagane
Valid login
    Input Valid Login
    Input Valid Password
    Click Login Button