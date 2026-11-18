import os
import re
import random
import string
import time
import tempfile
from pathlib import Path
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.credencial_page import CredencialPage
from pages.sidebar_page import SidebarPage
from pages.perfil_page import PerfilPage
from pages.grupo_familiar_page import GrupoFamiliarPage
from pages.certificados_page import CertificadosPage
from pages.actividades_page import ActividadesPage
from pages.amenities_page import AmenitiesPage


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

    sidebar_page = SidebarPage(page)
    perfil_page = PerfilPage(page)

    # 6. Navegar a la sección de Mi Perfil desde la Sidebar
    sidebar_page.ir_a_perfil()
    expect(page).to_have_url(re.compile(r".*/perfil.*"), timeout=8000)

    # 7. Modificar nuestro nombre y luego guardar cambios
    #Regla para escribir aleatorio
    texto_aleatorio = "".join(random.choices(string.ascii_lowercase, k=10))
    #Comando para que la regla funque
    buscador = page.get_by_role("textbox", name="Nombre *")
    buscador.fill(texto_aleatorio)
    buscador = page.get_by_role("textbox", name="Apellido *")
    buscador.fill(texto_aleatorio)
    # fuardar cambios
    perfil_page.guardar_perfil()

    sidebar_page = SidebarPage(page)
    grupo_familiar_page = GrupoFamiliarPage(page)

    # 8. Navegar a la sección Grupo Familiar
    sidebar_page.ir_a_grupo_familiar()
    expect(page).to_have_url(re.compile(r".*/grupo-familiar.*"), timeout=8000)

    # 9. Abrir el formulario flotante
    grupo_familiar_page.abrir_formulario()

    # 10. Agregar un familiar
    modal = page.get_by_role("dialog", name="Agregar familiar")
    expect(modal).to_be_visible(timeout=5000)

    # Listas de nombres y apellidos reales (sin tildes para evitar problemas en el email)
    nombres_reales = [
        "Tiago",
        "Mateo",
        "Lucas",
        "Valentina",
        "Sofia",
        "Julian",
        "Camila",
        "Martin",
        "Lucia",
        "Nicolas",
        "Bautista",
        "Martina",
        "Joaquin",
        "Emma",
        "Franco",
    ]
    apellidos_reales = [
        "Gomez",
        "Fernandez",
        "Rodriguez",
        "Lopez",
        "Martinez",
        "Perez",
        "Garcia",
        "Sanchez",
        "Romero",
        "Diaz",
        "Torres",
        "Ruiz",
        "Alvarez",
        "Acosta",
        "Benitez",
    ]

    # Elegimos nombre y apellido reales al azar
    nombre_familiar = random.choice(nombres_reales)
    apellido_familiar = random.choice(apellidos_reales)

    # Completamos Nombre y Apellido dentro del modal
    modal.get_by_role("textbox", name="Nombre *").fill(nombre_familiar)
    modal.get_by_role("textbox", name="Apellido *").fill(apellido_familiar)

    # Seleccionamos el parentesco "Hijo"
    modal.get_by_role("button", name="Seleccionar", exact=True).click()
    page.locator("button[role='option']", has_text="Hijo").click()

    # Generamos un email realista y único (ej: tiago.gomez4821@gmail.com)
    email_aleatorio = f"{nombre_familiar.lower()}.{apellido_familiar.lower()}{random.randint(100, 9999)}@gmail.com"
    modal.get_by_role("textbox", name="Email *").fill(email_aleatorio)

    # Generamos DNI (8 dígitos) y Teléfono (10 dígitos) aleatorios
    dni_aleatorio = "".join(random.choices(string.digits, k=8))
    modal.get_by_role("textbox", name="DNI").fill(dni_aleatorio)

    tel_aleatorio = "".join(random.choices(string.digits, k=10))
    modal.get_by_role("textbox", name="Teléfono").fill(tel_aleatorio)

    # Generamos fecha de nacimiento aleatoria y la tipeamos de corrido
    dia = f"{random.randint(1, 28):02d}"
    mes = f"{random.randint(1, 12):02d}"
    anio = str(random.randint(2008, 2015))
    modal.get_by_role("textbox", name="Fecha de nacimiento: día").click()
    page.keyboard.type(f"{dia}{mes}{anio}")

    # Establecemos contraseña fija y confirmamos
    password_fija = "123456"
    modal.locator("input[type='password']").nth(0).fill(password_fija)
    modal.locator("input[type='password']").nth(1).fill(password_fija)
    #Creamos solicitud
    page.get_by_role("button", name="Crear solicitud", exact=True).click()
     # Crear archivo temporal
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        tmp.write(b"Contenido simulado de imagen de certificado")
        archivo_test_path = tmp.name

    try:
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

    sidebar_page = SidebarPage(page)
    # 2. Navegar a la sección Cuotas desde la Sidebar
    sidebar_page.ir_a_cuotas()

    # 3. Verificación formal: Validamos que la URL haya cambiado correctamente
    expect(page).to_have_url(re.compile(r".*/cuotas.*"), timeout=8000)

    sidebar_page = SidebarPage(page)
    actividades_page = ActividadesPage(page)   
    # 2. Navegar a Actividades desde la barra lateral
    sidebar_page.ir_a_actividades()
    expect(page).to_have_url(re.compile(r".*/actividades.*"), timeout=7000)
    
    # 3. Ejecutar todo el proceso de inscripción (Inscribir)
    page.locator("table tbody tr").first.get_by_role("button", name="Inscribir", exact=True).click(force=True)
    modal_inscripcion = page.get_by_role("dialog")
    expect(modal_inscripcion).to_be_visible()
    # Buscamos el botón del desplegable ÚNICAMENTE dentro de este modal
    page.get_by_role("button", name="Cancelar", exact=True).click()

    sidebar_page = SidebarPage(page)
    amenities_page = AmenitiesPage(page)

    # 2. Navegar a la sección de Amenities desde la Sidebar
    sidebar_page.ir_a_amenities()
    expect(page).to_have_url(re.compile(r".*/amenities.*"), timeout=8000)

    # 3. Ejecutar la apertura del formulario de reserva
    amenities_page.abrir_modal_reserva()

    # 4. Verificación formal: Validamos que el cuadro de diálogo de reserva esté visible
    modal = page.get_by_role("dialog")
    expect(modal.first).to_be_visible(timeout=1000)
    page.get_by_role("button", name="Cancelar", exact=True).click()

    sidebar_page = SidebarPage(page)

    # 2. Navegar a la sección Mi calendario desde la Sidebar
    sidebar_page.ir_a_calendario()

    # 3. Verificación formal: Validamos que la URL haya cambiado correctamente
    expect(page).to_have_url(re.compile(r".*/calendario.*"), timeout=8000)

    #Cerrar sesion
    page.get_by_role("button", name="Cerrar sesion", exact=True).click()

