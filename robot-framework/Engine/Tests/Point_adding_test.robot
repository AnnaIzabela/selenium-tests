*** Settings ***
Library  SeleniumLibrary

Resource  C:/Users/path/to/robot/files.robot
Suite Setup  run keywords       Open Login Page     Valid login
Test Teardown  Reload Page
Suite Teardown     close browser


*** Test Cases ***
Add Point
    ${add_point}    set variable    xpath=//div[@class='navigation-items']/button[4]
    SeleniumLibrary.Wait Until Page Contains Element    ${add_point}
    Click element   ${add_point}
    Click button    xpath=//button[@class='mat-flat-button mat-accent']

