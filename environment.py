from selenium import webdriver


def before_all(context):
    print("Executing before all")


def before_feature(context, feature):
    print("Before feature\n")


# Scenario level objects are popped off context when scenario exits
def before_scenario(context, scenario):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    context.browser = webdriver.Chrome(chrome_options=chrome_options)
    print("Before scenario\n")


def after_scenario(context, scenario):
    context.browser.quit()
    print("After scenario\n")


def after_feature(context, feature):
    print("\nAfter feature")


def after_all(context):
    print("Executing after all")
