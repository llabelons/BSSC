import os
import random
from playwright.sync_api import Page
from dotenv import load_dotenv
  
load_dotenv()

def test_eventos_recep(page: Page):
    #0. Login en stg
    page.goto("https://stg.blueopendata.com/bsports-club/login")
    page.get_by_text("Prefer", exact=False).click()
    page.get_by_placeholder("Email o usuario").fill(os.getenv("PROF_EMAIL"))
    page.locator("input[type='password']").fill(os.getenv("PROF_PASSWORD"))
    page.get_by_role("button", name="INGRESAR").click()
    page.wait_for_timeout(500)

    # 1. Dirigirse a la sección "Eventos" de la sidebar
    page.get_by_role("navigation").get_by_role("link", name="Eventos", exact=True).click()
    page.wait_for_timeout(500)

    #2. Crear un nuevo evento
    page.get_by_text("Nuevo evento").locator("..").get_by_role("button").click()
    page.wait_for_timeout(500)

    #3. Cancelar al crear evento
    page.get_by_role("button", name="Cancelar", exact=True).click(force=True)
    page.wait_for_timeout(2000)

    #4. Ver un evento
    page.locator("table tbody tr").first.locator("button").first.click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Cerrar", exact=True).click(force=True)
    page.wait_for_timeout(100)

   #5. Dar de baja
    page.locator("table tbody tr").first.locator("button").nth(2).click()
    page.get_by_role("button", name="Cancelar", exact=True).click(force=True)
    page.wait_for_timeout(100)

    #10. Editar evento
    page.get_by_role("button", name="Editar", exact=True).first.click(force=True)
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Cancelar", exact=True).click(force=True)
    page.wait_for_timeout(100)

    # 12. Buscar evento por nombre o descripcion
    eventos_posibles = [
        "san lorenzo huracan",
        "racing vs boca",
        "racing independiente",
        "recital rock",
        "final copa",
    ]
    evento_aleatorio = random.choice(eventos_posibles)

    buscador = page.get_by_role("searchbox", name="BUSCAR EVENTO")
    buscador.fill(evento_aleatorio)
    buscador.press("Enter")
    page.wait_for_timeout(500)

    # Hacemos click en el botón de la tabla para abrir el modal
    page.locator("table tbody tr").first.locator("button").first.click()
    page.wait_for_timeout(1000)

    # Buscamos el botón Cerrar directamente en la página con coincidencia exacta
    page.get_by_role("button", name="Cerrar", exact=True).click(force=True)

