import os
from playwright.sync_api import Page
from dotenv import load_dotenv

load_dotenv()

def test_socios_recep(page: Page):
    # 1. Login en el entorno de staging (stg)
    page.goto("https://stg.blueopendata.com/bsports-club/login")
    page.get_by_text("Prefer", exact=False).click()
    page.get_by_placeholder("Email o usuario").fill(os.getenv("RECEP_EMAIL"))
    page.locator("input[type='password']").fill(os.getenv("RECEP_PASSWORD"))
    page.get_by_role("button", name="INGRESAR").click()
    page.wait_for_timeout(300)
    
    # 2. Ir a la sección de Socios desde la sidebar
    page.get_by_role("navigation").get_by_role("link", name="Socios", exact=True).click()
    page.wait_for_timeout(200)
    
    # Definimos el contenedor exclusivo de los filtros superiores
    zona_filtros = page.locator("fieldset")
    
    # 3. Apagamos el "ACTIVO" inicial que viene marcado por defecto
    zona_filtros.get_by_text("ACTIVO", exact=True).click()
    page.wait_for_timeout(100)
    
    # 4. Secuencia rápida de encendido y apagado de filtros (a 1 segundo)
    estados = ["ACTIVO", "MOROSO", "INHABILITADO", "SUSPENDIDO", "INACTIVO"]
    
    for estado in estados:
        zona_filtros.get_by_text(estado, exact=True).click()
        page.wait_for_timeout(100)
        zona_filtros.get_by_text(estado, exact=True).click()
        page.wait_for_timeout(100)
        
    # 5. Buscar el contenedor que dice NUEVO TITULAR y hacer clic en el botón naranja real que tiene adentro
    page.get_by_text("NUEVO TITULAR").locator("..").get_by_role("button").click()
    page.wait_for_timeout(300)

    # 6. Hacer clic en el botón Cancelar del formulario de socios
    page.get_by_role("button", name="Cancelar").click()
    page.wait_for_timeout(200)

    # 7. Escribir "Santiago" en el campo de búsqueda superior
    page.get_by_placeholder("Nombre, apellido o DNI").fill("Santiago")
    page.wait_for_timeout(100)

    # 8. Hacer clic en el botón "Buscar" al lado del input
    page.get_by_role("button", name="Buscar", exact=True).click()
    page.wait_for_timeout(300)
    
    # 9. Dirigirse a la sección "Actividades" en la sidebar
    page.get_by_role("navigation").get_by_role("link", name="Actividades", exact=True).click()
    page.wait_for_timeout(300)

    # 10. Hacer clic en el botón "+" al lado de "Nueva actividad"
    page.get_by_text("Nueva actividad").locator("..").get_by_role("button").click()
    page.wait_for_timeout(200)

    # 11. Hacer clic únicamente en el "Cancelar" visible del formulario de actividades
    page.locator("div:has-text('NUEVA ACTIVIDAD')").get_by_role("button", name="Cancelar").click()
    page.wait_for_timeout(200)

    # 12. Hacer clic en el primer botón "ojo" (Ver) de la tabla
    page.locator("table tbody tr").first.locator("button").first.click()
    page.wait_for_timeout(300)
    
    # Hacer clic en el botón naranja "Cerrar" del modal de visualización actual
    page.get_by_role("button", name="Cerrar", exact=True).first.click()
    page.wait_for_timeout(200)

    # 13. Hacer clic en el segundo botón (Editar con el ícono del lápiz) de la primera fila
    page.locator("table tbody tr").first.locator("button").nth(1).click()
    page.wait_for_timeout(300)

    # 14. Hacer clic en el botón Cancelar del modal de edición de actividades
    page.locator("div:has-text('ACTIVIDAD')").get_by_role("button", name="Cancelar").first.click()
    page.wait_for_timeout(200)

    # 15. Hacer clic en el tercer botón (Inscribir) de la primera fila
    page.locator("table tbody tr").first.locator("button").nth(2).click()
    page.wait_for_timeout(300)

    # 16. Hacer clic en el botón naranja "Cerrar" de la tabla
    page.get_by_role("button", name="Cerrar", exact=True).first.click()
    page.wait_for_timeout(200)

    # 17. Hacer clic en el cuarto boton (Desactivar activdad) de la primera fila
    page.locator("table tbody tr").first.locator("button").nth(3).click()
    page.wait_for_timeout(300)

    # 18. Hacer clic en el botón rojo "Cerrar" de la tabla
    page.get_by_role("button", name="CANCELAR", exact=False).first.click()
    page.wait_for_timeout(200)


