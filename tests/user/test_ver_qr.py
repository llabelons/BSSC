import os
import re
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.credencial_page import CredencialPage
from pages.sidebar_page import SidebarPage

def test_visualizacion_codigo_qr_y_navegacion_actividades(page):
    """
    [TC] AUTH-SC-02 - Flujo completo: Ver QR, cerrar y navegar a Actividades con pausa visual
    """
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_with_password(
        os.getenv("SOCIO_EMAIL"),
        os.getenv("SOCIO_PASSWORD")
    )

    credencial_page = CredencialPage(page)
    sidebar_page = SidebarPage(page)
    
    # 1. Esperamos la pantalla de la credencial
    expect(page).to_have_url(re.compile(r".*/socio-titular/credencial.*"), timeout=12000)
    
    # 2. Abrimos el QR y validamos que aparezca
    credencial_page.mostrar_qr()
    expect(credencial_page.qr_code_element.first).to_be_visible(timeout=5000)
    
    # 3. Cerramos el QR presionando en "Volver"
    credencial_page.cerrar_qr()
    
    # 4. Navegamos a la sección Actividades desde la Sidebar
    sidebar_page.ir_a_actividades()
    
    # 5. Verificamos que la URL haya cambiado a la sección de actividades
    expect(page).to_have_url(re.compile(r".*/actividades.*"), timeout=7000)

    # 6. Mantenemos el navegador abierto en la pantalla de actividades por 5 segundos (5000 milisegundos)
    page.wait_for_timeout(1500)
