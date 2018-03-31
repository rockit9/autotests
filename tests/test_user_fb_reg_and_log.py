
def test_user_reg(app):
    app.open_main_page()
    app.session.reg_with_fb(mail="mail14test@yahoo.com", password="12345qwerty")
    app.session.check_is_reg_page()
    app.session.logout()


def test_user_login(app):
    app.open_main_page()
    app.session.log_with_fb(mail="mail14test@yahoo.com", password="12345qwerty")
    app.session.check_is_logged_in()
    app.session.logout()
