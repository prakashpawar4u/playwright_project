def test_add_test_case(test_case_management_page):
    test_case_management_page.navigate("http://192.168.56.114:8012/addTestcaseFlow")
    test_case_management_page.add_test_case("Test Case 1", "Detailed Test Plan")
    # Add assertions to verify the test case was added
