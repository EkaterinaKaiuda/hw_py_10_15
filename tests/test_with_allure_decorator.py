import allure
from allure_commons.types import Severity
from selene import browser
from selene.support.conditions import have, be



@allure.tag('UI')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'e.kauda')
@allure.feature('Issues tab')
@allure.story('Visibility of created issues')
@allure.link('https://github.com', name='Resource for testing')
def test_check_issue_tab_with_decorator():
    open_rep()
    open_issue_tab()
    find_element()


@allure.step('Открываем репозиторий')
def open_rep():
    browser.open('https://github.com/EkaterinaKaiuda/hw_py_3.15')


@allure.step('Переходим на табу issues')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Ищем первый issue')
def find_element():
    browser.all('.js-issue-row').element_by(have.text('#1')).should(be.visible)
