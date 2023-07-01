# TestSimbirsoft
1. Установить виртуальное окружение
2. Установить зависимости
   ```console 
   pip install -r requirements.txt
   ``` 
3. Установить java
4. Запустить сервер
    ```console 
   java -jar selenium-server-standalone-3.5.3.jar -role standalone
   ```
5. Запустить тест с помощью команды 
    ```console 
    pytest --alluredir allureresults
   ```
6. Сформировать отчет Allure о результате работы
    ```console 
   allure serve allureresults
   ```


