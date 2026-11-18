import os
import re
from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_login_exitoso_con_email_y_password(page):
    """
    [TC] AUTH-SC-01 - Inicio de sesión exitoso con Email
    """
    login_page = LoginPage(page)
    login_page.navigate()
    
    login_page.login_with_password(
        email=os.getenv("SOCIO_EMAIL"),
        password=os.getenv("SOCIO_PASSWORD")
    )

    # Verificaciones
    expect(page).not_to_have_url(re.compile(r".*/login.*"))
    expect(page.locator("#auth-password-email")).not_to_be_visible()

    #Nos dirigimos hacia la interfaz de "QR"
    