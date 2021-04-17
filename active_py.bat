@echo off
echo: *******************************************
echo: MENU DE ACESSO A AMBIENTE DE DESENVOLVIMETO
echo: *******************************************
echo:
echo:
echo: Opcao 1. Abrir Ambiente de Desevolvimento do backend
echo: Opcao 2. Start em Server do backend 
echo: Opcao 3. Sair
echo: 
echo: 
set /p response= Digite opcao desejada: 
echo: __________________________________
echo:

if %response% equ 1 goto ambient_back
if %response% equ 2 goto server_back
if %response% equ 3 goto quit


:ambient_back 
    cls
    cd ./backend/Scripts
    activate &&  cd .. && echo: AMBIENTE DE DESENVOLVIMENTO DO BACKEND ESTA ATIVADO

:server_back
    cls
    cd ./backend/Scripts
    activate &&  cd ../../_utils && echo Starting server- \ - / - && start "Starr Server Backend" activate_server_back.bat && cd ..
 
:quit
    echo arigatou gozaimasu, itterashai!!!!!!!!
    echo bye bye!!!!! 
    pause
    exit

pause