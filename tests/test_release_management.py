def test_add_feature(release_management_page):
    release_management_page.navigate("http://192.168.56.114:8012/releaseManagement")
    release_management_page.add_feature("New Feature")
    # Add assertions to verify the feature was added
