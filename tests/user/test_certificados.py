import os
import re
import time
import tempfile
from pathlib import Path

from playwright.sync_api import expect

from pages.login_page import LoginPage          # ← Ajusta la ruta si es diferente
from pages.sidebar_page import SidebarPage
from pages.certificados_page import CertificadosPage

def test_carga_exitosa_de_certificado_medico(page):
    """
    [TC] CERT-SC-01 - Carga y subida exitosa de certificado médico (.png)
    """
    # Crear archivo temporal
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        tmp.write(b"Contenido simulado de imagen de certificado")
        archivo_test_path = tmp.name

    try:
        # 1. Login
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login_with_password(os.getenv("SOCIO_EMAIL"), os.getenv("SOCIO_PASSWORD"))

        sidebar_page = SidebarPage(page)
        certificados_page = CertificadosPage(page)

        # 2. Navegar a Certificados
        sidebar_page.ir_a_certificados()
        expect(page).to_have_url(re.compile(r".*/certificados.*"), timeout=8000)

        # 3. Subir certificado
        certificados_page.cargar_y_subir_certificado(archivo_test_path)

        # 4. Espera opcional
        page.wait_for_timeout(2000)

    finally:
        # Limpieza robusta
        path = Path(archivo_test_path)
        for _ in range(5):
            try:
                if path.exists():
                    path.unlink()
                break
            except PermissionError:
                time.sleep(0.5)
        else:
            try:
                path.unlink(missing_ok=True)
            except PermissionError:
                print(f"Advertencia: no se pudo eliminar el archivo temporal {archivo_test_path}")