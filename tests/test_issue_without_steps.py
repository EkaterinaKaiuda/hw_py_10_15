from selene import browser
from selene.support.conditions import have, be


def test_check_issue_tab():
    browser.open('https://github.com/EkaterinaKaiuda/hw_py_3.15')
    browser.element('#issues-tab').click()
    browser.all('.js-issue-row').element_by(have.text('#1')).should(be.visible)
