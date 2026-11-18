import os
import re
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.sidebar_page import SidebarPage
from pages.actividades_page import ActividadesPage

def test_inscripcion_exitosa_actividad(page):
    """
    [TC] ACT-SC-01 - Inscripción exitosa a la primera actividad disponible
    """
    # 1. Login e inicio de flujo conocido
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_with_password(
        os.getenv("SOCIO_EMAIL"),
        os.getenv("SOCIO_PASSWORD")
    )

    sidebar_page = SidebarPage(page)
    actividades_page = ActividadesPage(page)
    
    # 2. Navegar a Actividades desde la barra lateral
    sidebar_page.ir_a_actividades()
    expect(page).to_have_url(re.compile(r".*/actividades.*"), timeout=7000)
    
    # 3. Ejecutar todo el proceso de inscripción (Click +, Confirmar, Inscribir)
    actividades_page.inscribirse_a_primera_actividad()
    
    # 4. Dejar 5 segundos para observar visualmente el mensaje de éxito final antes de cerrar
    page.wait_for_timeout(1000)
