# ==========================
# Course: DevOps 1803 (2022)
# Name: Zohar Skupinsky
# Date: 8/4/2022
# ==========================

from os.path import join
from time import strftime, sleep
from selenium.webdriver import Chrome, Firefox, Edge


def debug(msg, msg_type="log", action="cont"):
    time_format = "%Y-%m-%d %H:%M:%S"
    timestamp = strftime(time_format)
    # Info about msg_type:
    #   "log" - general logs (default)
    #   "info" - for benchmarks
    #   "err" - for error alerts
    #   "my_log" - for my_log purposes
    msg_type = msg_type.upper()

    print("[%s][%s] %s" % (msg_type, timestamp, msg))
    # Info about action:
    #   cont - continue the normal execution (default),
    #   stop - stops the program execution
    if action == "cont":
        return
    elif action == "stop":
        quit(0)
    else:  # wrong input for arg 'action'! report error & continue to run
        debug("Wrong arg for my_log action!", msg_type="err")


def print_header(assignment):
    print("\n%s Assignment: %s %s" % ("=" * 10, assignment["number"], "=" * 10))
    print("ToDo:\n\t%s" % assignment["todo"])
    print("Solution:")


def the_end():
    print("\n%s THE END! %s" % ("=" * 10, "=" * 10))
    print("Hope you enjoyed testing as I enjoyed writing! :)")
    quit(0)


def press_to_continue():
    input("\n>>> Press any key to continue... <<<\n(all browsers opened by the program will be closed!)")
    debug("Closed all open browsers")
    return None


# NOT in use anymore...
# def continue_or_stop(action="cont"):
#     if action == "stop":
#         the_end()
#
#     sleep(1)
#     msg = "\nContinue to the next assignment? (y,n) "
#     if input(msg).lower() != "y":
#         the_end()
#     else:
#         return None


def get_user_input(message, fix_selection="", term_to_quit="q"):
    # fix_selection: used for my_log & coding-in-progress.
    # if empty - get input from gui
    # if not empty, skip input from user & use the hard-coded selection
    if fix_selection != "":
        return fix_selection

    user_input = input(message).lower()
    if user_input == term_to_quit.lower():
        user_input = "quit"

    return user_input


# Assignments for Class 4 - SELENIUM
def selenium_driver_path(browser):
    # Info for drivers names:
    # chromedriver.exe, geckodriver.exe (firefox), msedgedriver.exe (edge)
    drivers_names = {"chrome": "chromedriver.exe",
                     "edge": "msedgedriver.exe", "msedge": "msedgedriver.exe",
                     "firefox": "geckodriver.exe", "ff": "geckodriver.exe"}
    drivers_path = "c:\\Develop\\Selenium"
    browser = str(browser).lower()
    driver = join(drivers_path, drivers_names[browser])
    debug("driver= %s" % driver)
    return driver


def open_browser(site_url, browser_type="chrome"):
    browser_type = browser_type.lower()

    debug(f"Opening {browser_type}...", msg_type="info")
    if browser_type == "chrome":
        browser = Chrome(executable_path=selenium_driver_path(browser_type))
    elif browser_type == "firefox" or browser_type == "ff":
        browser = Firefox(executable_path=selenium_driver_path(browser_type))
    elif browser_type == "edge" or browser_type == "msedge":
        browser = Edge(executable_path=selenium_driver_path(browser_type))
    else:  # open the default...
        debug("Wrong browser_typ ARG in open_browser! Using default: Chrome.", msg_type="err")
        browser = Chrome(executable_path=selenium_driver_path(browser_type))

    browser.get(site_url)
    debug(f"{browser_type} was opened...", msg_type="info")
    return browser


def operate_on_element(driver, locator1, locator1_type, send_to_element1,
                       locator2, locator2_type, send_to_element2="click"):
    element1 = driver.find_element(locator1_type, locator1)
    element1.send_keys(send_to_element1)

    # clear the source text field PRIOR next use
    sleep(5)
    element1.send_keys(" ")  # trigger the hidden clear button...
    sleep(1)
    if send_to_element2 == "click":
        driver.find_element(locator2_type, locator2).click()

    # return element1  # Not required to return this any more...


def cookie_checker(browsers_cookies, when_got_here):
    if len(browsers_cookies) == 0:
        msg = "The cookies jar is EMPTY! Not even one left for me to taste..."
    else:
        msg = "There are a lot of cookies here!"

    print(" > Checking the Cookies jar %s delete:" % str(when_got_here).upper())
    print(" > %s" % msg)
    print(" > See for your self. Here's the list of ALL the cookies:")
    print(browsers_cookies, "\n")
    return None
