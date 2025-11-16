*** Settings ***
Resource  C:/Users/path/to/robot/files.robot


Suite Setup  run keywords       Open Login Page     Valid Login
Suite Teardown     close browser