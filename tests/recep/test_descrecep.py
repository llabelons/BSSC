import os
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

    # 1. Dirigirse a la sección "Descuentos" de la sidebar
    page.get_by_role("navigation").get_by_role("link", name="Descuentos", exact=True).click()
    page.wait_for_timeout(500)    

    #2. Crear nuevo descuento
    page.get_by_role("button", name="Nuevo descuento", exact=True).click(force=True)
    #SELECCIONAR PORCENTAJE
    page.get_by_text("Seleccionar tipo", exact=False).click()
    page.get_by_role("listbox").get_by_text("Porcentaje", exact=True).click(force=True)
    #SELECCIONAR MONTO FIJO 
    page.locator("app-select button").filter(has_text="Porcentaje").click()
    page.get_by_role("listbox").get_by_text("Monto fijo", exact=True).click(force=True)
    page.get_by_role("button", name="Cancelar", exact=True).click(force=True)
    page.wait_for_timeout(1000)

    #3. Editar descuento
    page.locator("table tbody tr").first.locator("button").first.click()
    page.get_by_role("button", name="Cancelar", exact=True).click(force=True)
    page.wait_for_timeout(1000)

    #4. Borrar evento
    page.locator("table tbody tr").first.locator("button").nth(1).click()
    page.get_by_role("button", name="Cancelar", exact=True).click(force=True)
    page.wait_for_timeout(1000)    

    #0. Buscar por titulo
    buscador = page.get_by_placeholder("Buscar por título")
    buscador.fill("beneficio inscripcion")
    buscador.press("Enter")
    page.wait_for_timeout(500)