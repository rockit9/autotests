def test_user_vk_reg(app):
    app.open_main_page()
    app.session.switch_to_another_local(lang="ru")
    app.session.reg_with_vk(mail="matison88@mail.ru", password="nfyznfyz")
    app.session.check_is_reg_page_vk()
    app.session.logout_vk()


def test_user_vk_login(app):
    app.session.log_with_vk(mail="matison88@mail.ru", password="nfyznfyz")
    app.session.check_is_logged_in_vk()
    app.session.logout_vk()
