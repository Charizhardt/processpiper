from processpiper import ProcessMap, EventType, ActivityType, GatewayType


def test_case03():
    with ProcessMap(
        "Sample Test Process", colour_theme="BLUEMOUNTAIN"
    ) as my_process_map:
        with my_process_map.add_lane("End User") as lane1:
            start = lane1.add_element("Start", EventType.START)
            enter_keyword = lane1.add_element("Enter Keyword", ActivityType.TASK)

        with my_process_map.add_pool("System Search") as pool1:
            with pool1.add_lane("Database System") as lane2:
                login = lane2.add_element("Login", ActivityType.TASK)
                search_records = lane2.add_element("Search Records", ActivityType.TASK)
                result_found = lane2.add_element("Result Found?", GatewayType.EXCLUSIVE)
                display_result = lane2.add_element("Display Result", ActivityType.TASK)
                logout = lane2.add_element("Logout", ActivityType.TASK)
                end = lane2.add_element("End", EventType.END)

            with pool1.add_lane("Log System") as lane3:
                log_error = lane3.add_element("Log Error", ActivityType.TASK)

        start.connect(login, "User \nAuthenticates").connect(
            enter_keyword, "Authenticated"
        ).connect(search_records, "Search Criteria")
        search_records.connect(result_found, "Result").connect(display_result, "Yes")
        display_result.connect(logout).connect(end)
        result_found.connect(log_error, "No").connect(display_result)

        my_process_map.set_footer("Generated by ProcessPiper")
        my_process_map.draw()
        my_process_map.save("images/test/my_process_map3.png")
        my_process_map.export_to_bpmn("test_case03.bpmn")


if __name__ == "__main__":
    test_case03()
