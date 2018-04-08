def test_user_fb_reg(app):
    app.open_main_page()
    app.session.reg_with_fb(mail="mail14test@yahoo.com", password="12345qwerty")
    app.session.check_is_reg_page_fb()
    app.session.logout_fb()


def test_user_fb_login(app):
    app.session.log_with_fb(mail="mail14test@yahoo.com", password="12345qwerty")
    app.session.check_is_logged_in_fb()
    app.session.logout_fb()
