import os
import random
from playwright.sync_api import Page
from dotenv import load_dotenv

load_dotenv()

def test_eventos_recep(page: Page):
    #0. Login en stg
    page.goto("https://stg.blueopendata.com/bsports-club/login")
    page.get_by_text("Prefer", exact=False).click()
    page.get_by_placeholder("Email o usuario").fill(os.getenv("RECEP_EMAIL"))
    page.locator("input[type='password']").fill(os.getenv("RECEP_PASSWORD"))
    page.get_by_role("button", name="INGRESAR").click()
    page.wait_for_timeout(500)

    # 1. Dirigirse a la sección "Eventos" de la sidebar
    page.get_by_role("navigation").get_by_role("link", name="Eventos", exact=True).click()
    page.wait_for_timeout(500)

    #2. Crear un nuevo evento
    page.get_by_text("Nuevo evento").locator("..").get_by_role("button").click()
    page.wait_for_timeout(500)

    #3. Cancelar al crear evento
    page.locator("button:has-text('Cancelar')").last.click()
    page.wait_for_timeout(500)

    #4. Editar un evento
    page.locator("table tbody tr").first.locator("button").first.click()
    page.wait_for_timeout(500)

    #5. Cancelar edición
    modal_editar = page.get_by_role("dialog", name="Editar evento")
    modal_editar.get_by_role("button", name="Guardar evento", exact=True).click()
    page.wait_for_timeout(500)

    #6. Cancelar un evento
    page.locator("table tbody tr").first.locator("button").nth(1).click()
    page.wait_for_timeout(500)

    #7. Clic en boton de cancelar en "Cancelar evento"
    modal_cancelar = page.get_by_role("alertdialog")
    modal_cancelar.get_by_role("button", name="Cancelar", exact=True).click()
    page.wait_for_timeout(500)

    #8. Eliminar un evento
    page.locator("table tbody tr").first.locator("button").nth(2).click()

    #9. Cancelar "Eliminar evento" 
    modal_eliminar = page.get_by_role("alertdialog")
    # Forzamos la espera explícita a que aparezca antes de interactuar
    modal_eliminar.wait_for(state="visible") 
    modal_eliminar.get_by_role("button", name="Cancelar", exact=True).click()
    page.wait_for_timeout(500)

    #10. Buscar evento por nombre o descripcion
    eventos_posibles = [
        "partido pampero vs alvear",
        "Rifa Solidaria",
        "Fecha 5",
        "basquet",
        "teniss especial",
        "polo",
        "Fecha 4",
        "Fecha 1",
        "Sky",
        "holaqsy",
        "Competición",
        "agua caliente",
        "Partido de tennis chico",
        "Futbol",
    ]   
    evento_aleatorio = random.choice(eventos_posibles)

    buscador = page.get_by_role("searchbox", name="BUSCAR")
    buscador.fill(evento_aleatorio)
    buscador.press("Enter")
    page.wait_for_timeout(500)

    #11. Dirigirse a la sección "Entradas de eventos" de la sidebar
    page.get_by_role("navigation").get_by_role("link", name="Entrada", exact=False).click()
    page.wait_for_timeout(500)

    #13. Generar un nuevo evento
    page.locator("table tbody tr").first.locator("button").first.click()
    page.wait_for_timeout(500)

    #14. Cancelar el "Generar nuevo evento"
    page.get_by_role("button", name="Cerrar", exact=True).click(force=True)
    page.wait_for_timeout(500)

    #15. Ver historial de un evento
    page.locator("table tbody tr").first.locator("button").nth(3).click()
    page.wait_for_timeout(500)

    #16. Cancelar "Ver historial de un evento"
    page.get_by_role("button", name="Cerrar", exact=True).click(force=True)
    page.wait_for_timeout(500)

    #12. Buscar evento por nombre o descripcion
    buscador = page.get_by_placeholder("Título o descripción")
    buscador.fill("entrega de trofeo")
    buscador.press("Enter")
    page.wait_for_timeout(500)
    # Hacemos click en el botón de la tabla para abrir el modal (sin asignarlo a una variable)
    page.locator("table tbody tr").first.locator("button").first.click()
    page.wait_for_timeout(1000)
    # Buscamos el botón Cerrar directamente en la página con coincidencia exacta
    page.get_by_role("button", name="Cerrar", exact=True).click(force=True)
