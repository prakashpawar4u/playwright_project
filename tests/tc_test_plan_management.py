def test_maintain_test_cases(test_plan_management_page):
    test_plan_management_page.navigate("http://192.168.56.114:8012/testPlanManagement")
    test_plan_management_page.maintain_test_cases("Release 1", "Feature 1")
    # Add assertions to verify the test plan maintenance
