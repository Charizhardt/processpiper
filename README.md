[![license](https://img.shields.io/badge/license-mit-brightgreen.svg?style=plastic)](https://en.wikipedia.org/wiki/MIT_License)
[![CodeFactor](https://www.codefactor.io/repository/github/csgoh/processpiper/badge?style=plastic)](https://www.codefactor.io/repository/github/csgoh/processpiper)
![code size](https://img.shields.io/github/languages/code-size/csgoh/processmapper?style=plastic)

# ProcessPiper (Business Process Diagram as Code)
A python library to generate business process diagram using code. 

## Why ProcessPiper?
1. Generate professional business process diagrams with Python code, eliminating the need for manual drawing and complex tools.
2. Improve teamwork by utilising source code repositories for change monitoring, collaboration, and diagram history.
3. Enhance precision by generating diagrams with code, sharing/exporting them in PNG format, and integrating them with Python tools.

You can see the sample code and output for design concept below.

```python
from processpiper import ProcessMap, EventType, ActivityType, GatewayType

def test_case5():
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
        my_process_map.save("my_process_map_test_case05.png")


if __name__ == "__main__":
    test_case5()
```

![Process Map](https://github.com/csgoh/processpiper/blob/main/images/test/test_auto_case1.png)


## Development Status

It is still under development :construction: Beta version v0.1 will be release soon.

Initial release would only cover the following basic business process elements. Other element types will be introduced in subsequence releases.

* Event: Start, End, Timer, Intermediate
* Activity: Task, Subprocess
* Gateway: Inclusive, Exclusive, Parallel

Any ideas or suggestions, please send it to me via [GitHub Discussions](https://github.com/csgoh/processmapper/discussions).


Thank you for checking out my project. If you have found ProcessPiper useful and would like to show your appreciation, consider buying me a coffee or flat white :coffee: and keep me going. To buy me a coffee, simply follow this link: 

<a href="https://www.buymeacoffee.com/csgoh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

## Implementation Checklist and Progress

These are a list of items that need to be implemented or fixed before the initial release.
<br>:white_check_mark: Implement Start, End and Timer Event elements
<br>:white_check_mark: Implement Task Activity elements
<br>:white_check_mark: Implement Inclusive, Exclusive and Parallel Gateway elements
<br>:white_check_mark: Implement pool and lane
<br>:white_check_mark: Implement diagram title
<br>:white_check_mark: Implement diagram footer
<br>:white_check_mark: Implement placement (left to right) of for elements in the same lane ![Process Map](https://github.com/csgoh/processpiper/blob/main/images/test/test_case6.png)
<br>:white_check_mark: Implement placement (top down, left to right) of elements in the same pool but different lane ![Process Map](https://github.com/csgoh/processpiper/blob/main/images/test/test_case7.png)
<br>:white_check_mark: Automatically change surface size based on the element layout
<br>:white_check_mark: Implement placement (top to bottom) of elements in the different pool
<br>:white_check_mark: Add label to connector
<br>:white_check_mark: Implement Intermediate Event Element
<br>:white_check_mark: Implement Subprocess Activity Element ![Process Map](https://github.com/csgoh/processpiper/blob/main/images/test/test_case9.png)
<br>:white_check_mark: Connection that crosses pool boundary will be drawn as a dotted line
<br>:white_check_mark: Fix the connection alignment issue
<br>:white_check_mark: Support colour themes
![Process Map](https://github.com/csgoh/processpiper/blob/main/images/test/test_case10-BLUEMOUNTAIN.png)
![Process Map](https://github.com/csgoh/processpiper/blob/main/images/test/test_case10-GREENTURTLE.png)
![Process Map](https://github.com/csgoh/processpiper/blob/main/images/test/test_case10-ORANGEPEEL.png)
![Process Map](https://github.com/csgoh/processpiper/blob/main/images/test/test_case10-GREYWOOF.png)
<br>:white_check_mark: Connection that crosses pool boundary should begin with a white circle/dot and end with a white arrow.
<br>:white_check_mark: Renamed from ProcessMap to ProcessPiper
<br>:white_check_mark: Clean up code
<br>:white_square_button: More testing!
