from behave import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

delay = 15


@given('the homepage is loaded')
def load_page(context):
    context.browser.get('http://o2.pl/')
    context.browser.maximize_window()
    try:
        akcept_polityka = context.browser.find_element_by_xpath('//div[contains(text(), \'PRZEJDŹ DALEJ\')]')
        akcept_polityka.click()
    except NoSuchElementException():
        print('No element found')

    try:
        home = WebDriverWait(context.browser, delay).until(
            EC.visibility_of_element_located(
                (
                    By.ID, 'app-inner'
                )
            )
        )

    except TimeoutException:
        print("Loading took too much time!")

    assert 'o2 - Serce Internetu' in context.browser.title


use_step_matcher('re')


@when('I hover the mouse over widget in the (?P<position>top-left|top-right|bottom-right) corner')
def hover_over(context, position):

    if position == 'top-left':
        left_widget = context.browser.find_element_by_class_name('bu4XW')
        hover = ActionChains(context.browser).move_to_element(left_widget)
        hover.perform()

    elif position == 'top-right':
        try:
            top_right_widget = WebDriverWait(context.browser, delay).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH, '//div[@data-st-area="ST-CrnrML-main-area"]'
                    )
                )
            )
            hover = ActionChains(context.browser).move_to_element(top_right_widget)
            hover.perform()
        except TimeoutException:
            print("Loading took too much time!")

    else:
        try:
            bottom_right_widget = WebDriverWait(context.browser, delay).until(
                EC.visibility_of_element_located(
                    (
                        By.ID, 'quizzesCircle'
                    )
                )
            )
            hover = ActionChains(context.browser).move_to_element(bottom_right_widget)
            hover.perform()
        except TimeoutException:
            print("Loading took too much time!")


@step('I fill (?P<input_field>username|password) with \'(?P<credentials>.*)\'')
def enter_credentials(context, input_field, credentials):
    if input_field == 'username':
        login_input = context.browser.find_element_by_xpath('//form[@id=\'_poczta_zaloguj\']/input[@name=\'username\']')
        login_input.send_keys(credentials)
    else:
        password_input = context.browser.find_element_by_xpath(
            '//form[@id=\'_poczta_zaloguj\']/input[@name=\'password\']'
        )
        password_input.send_keys(credentials)


@step('I click (?P<operation>Zaloguj się|Graj teraz!|Plus) button') #zielonego pojecia nie mam czemu nie przyjmuje {label}
def click_operation(context, operation):
    if operation == 'Zaloguj się':
        operation_click = context.browser.find_element_by_xpath(
            '//form[@id=\'_poczta_zaloguj\']/button[contains(text(),\'{operation}\')]'.format(operation=operation)
        )
        operation_click.click()
    elif operation == 'Plus':
        operation_click = WebDriverWait(context.browser, delay).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH, '//span[@icon="category-plus"]'
                )
            )
        )
        operation_click.click()


    else:
        operation_click = context.browser.find_element_by_xpath(
            '//div[contains(text(),\'{operation}\')]'.format(operation=operation)
        )
        operation_click.click()


@then('login form is visible')
def visibility_of_login_form(context):
    login_field = WebDriverWait(context.browser, delay).until(
        EC.visibility_of_element_located(
            (
                By.XPATH, '//form[@id=\'_poczta_zaloguj\']/input[@name=\'username\']'
            )
        )
    )

    password_field = context.browser.find_element_by_xpath('//form[@id=\'_poczta_zaloguj\']/input[@name=\'password\']')

    assert login_field.is_displayed() and password_field.is_displayed()


@then("I am redirected to my mailbox")
def redirection_to_mailbox(context):
    context.browser.switch_to.window(context.browser.window_handles[1])
    try:
        recived_messages_area = WebDriverWait(context.browser, delay).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH, '//div[contains(@class, \'ContainerBox\') and contains(., \'Odebrane\')]'
                )
            )
        )

    except TimeoutException:
        print("Loading took too much time!")

    assert 'Poczta o2' in context.browser.title


@then("I am redirected to the login page with message about wrong credentials")
def step_impl(context):
    context.browser.switch_to.window(context.browser.window_handles[1])
    try:
        login_area = WebDriverWait(context.browser, delay).until(
            EC.visibility_of_element_located(
                (
                    By.CLASS_NAME, 'login-area'
                )
            )
        )

    except TimeoutException:
        print("Loading took too much time!")
    error_message = context.browser.find_element_by_id('login-error-message')
    print(error_message.text)
    assert 'Podany login i/lub hasło są nieprawidłowe.\nSpróbuj jeszcze raz.' == error_message.text


@then("button (?P<button>.*) is visible")
def visibility_of_button(context, button):
    which_button = WebDriverWait(context.browser, delay).until(
        EC.visibility_of_element_located(
            (
                By.XPATH, '//div[contains(text(),{button})]'.format(button=button)
            )
        )
    )
    assert which_button.is_displayed()


@then("Quiz page available")
def quiz_page(context):
    try:
        quiz_area = WebDriverWait(context.browser, delay).until(
            EC.title_contains('quizy')
        )

    except TimeoutException:
        print("Loading took too much time!")

    assert 'o2 - testy, quizy, sondy - o2 - Serce Internetu' in context.browser.title





@when('I select "(?P<category>.+)" from available categories')
def step_impl(context, category):
    category_icon = WebDriverWait(context.browser, delay).until(
        EC.element_to_be_clickable(
            (
                By.XPATH, '//span[contains(text(), \'{category}\')]//parent::span//parent::div//preceding-sibling::div//parent::a'.format(category=category)
            )
        )
    )
    category_icon.click()


@then('I am able to see all topics from "(?P<stream>.+)"')
def step_impl(context, stream):

    displayed_stream = context.browser.find_element_by_xpath('//div[@data-st-area="ST-Index-RStream-'+stream+'"]')
    assert displayed_stream.is_displayed()


@then('"(?P<topic>.+)" is not displayed anymore at list of available categories')
def step_impl(context, topic):

    stream_menu = WebDriverWait(context.browser, delay).until(
        EC.visibility_of_element_located(
            (
                By.XPATH, '//div[@data-st-area=\'ST-Index-RStream-menu\']'
            )
        )
    )
    try:
        stream = context.browser.find_element_by_xpath(
            '//span[contains(text(), \'{topic}\')]//parent::span//parent::div//preceding-sibling::div//parent::a'.format(
                topic=topic)
        )

    except NoSuchElementException():
        return True


    #tutaj jestem w trakcie - ten step nie jest skończony


@then("I am able to see all categories")
def step_impl(context):
    list_of_all_categories = context.browser.find_element_by_class_name('_3zW-M')
    assert list_of_all_categories.is_displayed()


@when('I click "(?P<topic>.+)"')
def step_impl(context, topic):
    topic = WebDriverWait(context.browser,delay).until(
        EC.element_to_be_clickable(
            (
                By.XPATH, '//div[contains(text(), \'{topic}\')]//parent::button'.format(topic=topic)
            )
        )
    )
    topic.click()


@step("I click Zapamiętaj")
def step_impl(context):
    zapamietaj_button = context.browser.find_element_by_xpath('//button[contains(text(), \'Zapamiętaj\')]')
    zapamietaj_button.click()

    
use_step_matcher('parse')


