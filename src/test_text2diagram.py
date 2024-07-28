import inspect
import os
import os.path
from processpiper import text2diagram


def prep_for_test(filename: str):
    path = os.path.join("images/", "test/")

    if not os.path.exists(path):
        os.mkdir(path)

    return os.path.join(path, filename)


def generate_diagram(input_syntax: str, painter_type: str = "PNG"):
    if painter_type == "PNG":
        output_file = prep_for_test(
            f"{inspect.currentframe().f_back.f_code.co_name}.png"
        )
    else:
        output_file = prep_for_test(
            f"{inspect.currentframe().f_back.f_code.co_name}.svg"
        )
<<<<<<< HEAD
    _, img = text2diagram.render(
        input_syntax, output_file, show_code=True, export_to_bpmn=True
    )
    if painter_type == "PNG":
        img.save(output_file)
    else:
        # save gen_code as SVG file
        with open(output_file, "w") as f:
            f.write(img)
=======
    _, img = text2diagram.render(input_syntax, output_file, show_code=True)
    
    # if painter_type == "PNG":
    #     img.save(output_file)
    # else:
    #     # save gen_code as SVG file
    #     with open(output_file, "w") as f:
    #         f.write(img)
>>>>>>> main


def test_text2diagram_01():
    input_syntax = """
    title: Sample Test Process
    colourtheme: BLUEMOUNTAIN
        lane: End User
            (start) as start
            [Enter Keyword] as enter_keyword
            (end) as end
    pool: System Search
        lane: Database System
            [Login] as login
            [Search Records] as search_records
            <Result Found?> as result_found
            [Display Result] as display_result
            [Logout] as logout
        lane: Log System
            [Log Error] as log_error

    start->login: User \\nAuthenticate
    login->enter_keyword: Authenticated
    enter_keyword->search_records: Search Criteria
    search_records->result_found: Result
    result_found->display_result: Yes
    display_result->logout->end
    result_found->log_error: No
    log_error->display_result

    footer: Generated by ProcessPiper
    """
    generate_diagram(input_syntax)


def test_text2diagram_02():
    input_syntax = """
    title: Test Process
    colourtheme: GREENTURTLE
    pool: Pool A
        lane: Lane A
            (start) as start
            [Task 1] as task1
            <branch 1> as branch1
            [@subprocess Sub process 1] as subprocess1
            <@parallel branch 2> as branch2
            <@inclusive branch 3> as branch3
            (end) as end
    pool: Pool B
        lane: Lane B
            (@timer schedule 1) as timer_schedule
            (@intermediate schedule 2) as intermediate_schedule

    start->task1->branch1->subprocess1->branch2->branch3->end
    branch1->timer_schedule->intermediate_schedule->end

    footer: Generated by Process Piper
    """
    generate_diagram(input_syntax)


def test_text2diagram_03():
    input_syntax = """
    title: Pizza Order Process
    colourtheme: BLUEMOUNTAIN
    lane: Customer
            (start) as start
            [Browse PizzaPiper website] as browse_website
            [Order a pizza] as order_pizza
            [Make payment] as make_payment
            [Receive pizza] as receive_pizza
            (end) as end
    pool: Pizza Piper Enterprise
        lane: Pizza Shop
            [Receive order] as receive_order
            [Bake pizza] as bake_pizza
            <Pizza ready?> as pizza_ready
        lane: Pizza Delivery
            [Deliver pizza] as deliver_pizza

    start->browse_website->order_pizza->make_payment
    make_payment->receive_order: Order details
    receive_order->bake_pizza
    bake_pizza->pizza_ready: Yes
    pizza_ready->deliver_pizza->receive_pizza: Freshly baked pizza
    pizza_ready->bake_pizza: No
    receive_pizza->end
    """
    generate_diagram(input_syntax)


def test_text2diagram_04():
    input_syntax = """
    title: This is a test diagram
    colourtheme: GREENTURTLE
    lane: Customer
    (start) as start
    [Do something] as do
    (end) as end

    start->do->end
    """
    generate_diagram(input_syntax)


def test_text2diagram_05():
    input_syntax = """
    # Showcase Process Piper plain text to diagram capability
    title: Make pizza process
    # Set diagram colour theme
    colourtheme: BLUEMOUNTAIN
    lane: Pizza Shop
        (start) as start
        [Put the pizza in the oven] as put_pizza_in_oven
        [Check to see if pizza is done] as check_pizza_done
        <@parallel Done baking?> as done_baking
        [Take the pizza out of the oven] as take_pizza_out_of_oven
        (end) as end

    start->put_pizza_in_oven->check_pizza_done->done_baking
    done_baking->take_pizza_out_of_oven: Yes
    take_pizza_out_of_oven->end
    done_baking->put_pizza_in_oven: No
    """
    generate_diagram(input_syntax)


def test_text2diagram_06():
    input_syntax = """
    title: Signal Example
    colourtheme: GREENTURTLE
    pool: pool 1
    lane: lane 1
        (@signal signal 1) as event1
        (@signal signal 2) as event2
        (@signal signal 3) as event3

    event1->event2->event3
    """
    generate_diagram(input_syntax)


def test_text2diagram_07():
    input_syntax = """
    title: Signal Example
    colourtheme: GREENTURTLE
    pool: pool 1
    lane: lane 1
        (@conditional signal 1) as event1
        (@conditional signal 2) as event2
        (end) as event3

    event1->event2->event3
    """
    generate_diagram(input_syntax)


def test_text2diagram_08():
    input_syntax = """
    title: Signal Example
    colourtheme: GREENTURTLE
    pool: pool 1
    lane: lane 1
        (@message signal 1) as event1
        (@message signal 2) as event2
        (@message signal 3) as event3

    event1->event2->event3
    """
    generate_diagram(input_syntax)


def test_text2diagram_09():
    input_syntax = """
    title: Signal Example
    colourtheme: GREENTURTLE
    pool: pool 1
    lane: lane 1
        (@message signal 1) as event1
        (@message signal 2) as event2
        (@message signal 3) as event3
        (@link signal 4) as event4

    event1->event2->event3->event4
    """
    generate_diagram(input_syntax)


def test_text2diagram_10():
    input_syntax = """
    title: debug01
    width: 8192
    colourtheme: BLUEMOUNTAIN
    lane: customer
        (start) as start
        [brings a defective computer] as activity_9
    lane: crs
        [checks the defect] as activity_10
        [hand out a repair cost calculation] as activity_11
        <the customer decide> as gateway_1
        [are acceptable] as activity_3
        [continues] as activity_4
        [takes her computer] as activity_5
        [consists of two activities] as activity_12
        [execute two activities in an arbitrary order] as activity_13
        [is] as activity_14
        [check the hardware] as activity_15
        [repair the hardware] as activity_16
        [checks the software] as activity_17
        [configure the software] as activity_18
        [test the proper system functionality after each of these activities] as activity_19
        <detect an error> as gateway_6
        [execute another arbitrary repair activity] as activity_8
        (end) as end

    start->activity_9->activity_10->activity_11->gateway_1
    gateway_1->activity_3->activity_4->activity_12
    gateway_1->activity_5->activity_12
    activity_12->activity_13->activity_14->activity_15->activity_16->activity_17->activity_18->activity_19->gateway_6
    gateway_6->activity_8->end
    gateway_6->end
    """
    generate_diagram(input_syntax)


def test_text2diagram_11():
    input_syntax = """title: debug
    width: 10000
    colourtheme: BLUEMOUNTAIN
    pool: Pool
    lane:
        (start) as start
        [the customer receives feedback from the assessor or approver] as activity_14
        (end) as end
        [assess the request] as activity_13
        <Approved?> as gateway_1
        <> as gateway_2
        [deny the loan] as deny_the_loan
        [approve the loan] as approve_the_loan
        [send the request] as send_the_request
        <> as gateway_2_end
        <> as gateway_1_end

    start->activity_13->gateway_1

    gateway_1->gateway_2: No
    gateway_1->approve_the_loan: the loan is \\nsmall
    approve_the_loan->gateway_1_end

    gateway_2->deny_the_loan
    gateway_2->send_the_request: the customer is
    send_the_request->gateway_2_end

    deny_the_loan->gateway_2_end
    gateway_2_end->gateway_1_end

    gateway_1_end->activity_14->end
    """
    generate_diagram(input_syntax)


def test_text2diagram_12():
    input_syntax = """
    title: Demo
    width: 1200
    colourtheme: BLUEMOUNTAIN
    pool: Pool 1
    lane: Lane 1
        (start) as start
        [task 1] as t1
        [task 2] as t2
        (end) as end

    start-(top, top)->t1: label 1 2 3
    t1-(bottom, bottom)->t2->end: finishing
    start->t1: label1
    t1->end: label2
    """

    generate_diagram(input_syntax)


def test_text2diagram_13():
    input_syntax = """
    title: Simulated Reality Assessment Process
    colourtheme: BLUEMOUNTAIN

    # Define the swimlane and BPMN elements
    pool: The World
        lane: You
            (start) as start
            [Create simulation hypotheses] as form_hypotheses
            [Look for glitches] as look_for_glitches
            <Did boss pass twice \\nin same way?> as did_boss_walk_past
            [Start a conversation with a stranger] as ask_stranger_purpose
            <Sounds like a NPC?> as sound_like_npc
            [The World is simulated] as world_is_simulated
            [The World is not simulated] as world_is_not_simulated
            (end) as end
        lane: Stranger
            [Responded 'Princess needs help!'] as stranger_responded

    # Connect all the elements
    start->form_hypotheses->ask_stranger_purpose
    ask_stranger_purpose->stranger_responded
    stranger_responded-(right, left)->sound_like_npc
    look_for_glitches->did_boss_walk_past
    sound_like_npc->look_for_glitches: No
    sound_like_npc->world_is_simulated: Yes
    did_boss_walk_past->world_is_not_simulated: No
    did_boss_walk_past->world_is_simulated: Yes
    world_is_not_simulated->end
    world_is_simulated->end

    footer: Generated by ProcessPiper
    """

    generate_diagram(input_syntax)


def test_text2diagram_14():
    input_syntax = """
    title: Simulated Reality Assessment Process
    colourtheme: BLUEMOUNTAIN

    # Define the swimlane and BPMN elements
    pool: The World
        lane: You
            (start) as start
            [Create simulation hypotheses] as form_hypotheses
            [Look for glitches] as look_for_glitches
            <Did boss pass twice \\nin same way?> as did_boss_walk_past
            [Start a conversation with a stranger] as ask_stranger_purpose
            <Sounds like a NPC?> as sound_like_npc
            [The World is simulated] as world_is_simulated
            [The World is not simulated] as world_is_not_simulated
            (end) as end
        lane: Stranger
            [Responded 'Princess needs help!'] as stranger_responded

    # Connect all the elements
        start->form_hypotheses->ask_stranger_purpose
        ask_stranger_purpose->stranger_responded
        stranger_responded-(right, left)->sound_like_npc
        look_for_glitches->did_boss_walk_past
        sound_like_npc->look_for_glitches: No
        sound_like_npc->world_is_simulated: Yes
        did_boss_walk_past->world_is_not_simulated: No
        did_boss_walk_past->world_is_simulated: Yes
        world_is_not_simulated->end
        world_is_simulated->end

        footer: Generated by ProcessPiper
    """
    generate_diagram(input_syntax, "PNG")
    generate_diagram(input_syntax, "SVG")


if __name__ == "__main__":
    test_text2diagram_01()
    test_text2diagram_02()
    test_text2diagram_03()
    test_text2diagram_04()
    test_text2diagram_05()
    test_text2diagram_06()
    test_text2diagram_07()
    test_text2diagram_08()
    test_text2diagram_09()
    test_text2diagram_10()
    test_text2diagram_11()
    test_text2diagram_12()
    test_text2diagram_13()
    test_text2diagram_14()
