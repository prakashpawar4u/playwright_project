@echo off

:: Check if build number is provided as an argument
if "%1"=="" (
    echo Usage: run_tests.bat [build_number]
    exit /b 1
)

set BUILD_NUMBER=%1

:: Create allure-results directory if it doesn't exist
if not exist allure-results mkdir allure-results

:: Copy previous history if it exists
if exist allure-report\history (
  xcopy /E /I /Y allure-report\history allure-results\history
)

:: Create executor.json
(
echo {
echo   "name": "Local Machine",
echo   "type": "local",
echo   "url": "http://192.168.56.114:8001/",
echo   "buildOrder": %BUILD_NUMBER%,
echo   "buildName": "Local Test Run #%BUILD_NUMBER%",
echo   "buildUrl": "http://192.168.56.114:8001/",
echo   "reportUrl": "http://192.168.1.6:8001/",
echo   "reportName": "Allure Report for Local Test Run #%BUILD_NUMBER%"
echo }
) > allure-results\executor.json

:: Copy categories.json to allure-results directory
copy categories.json allure-results\categories.json

:: Run tests and generate Allure results
pytest -s -v .\tests --alluredir allure-results

:: Generate Allure report
allure generate allure-results --clean -o allure-report

:: Serve the Allure report on a specific port
cd allure-report
python -m http.server 8001
