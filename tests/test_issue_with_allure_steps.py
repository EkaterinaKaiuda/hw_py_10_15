import allure
from selene import browser
from selene.support.conditions import have, be


def test_check_issue_tab_allure_step():
    with allure.step('Открываем репозиторий'):
        browser.open('https://github.com/EkaterinaKaiuda/hw_py_3.15')

    with allure.step('Переходим на табу issues'):
        browser.element('#issues-tab').click()

    with allure.step('Ищем первый issue'):
        browser.all('.js-issue-row').element_by(have.text('#1')).should(be.visible)
