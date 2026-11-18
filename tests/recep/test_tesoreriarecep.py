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

    #1. Ir a la interfaz de "Tesoreria"
    page.get_by_role("navigation").get_by_role("link", name="Tesorería", exact=True).click()
    page.wait_for_timeout (500)

    #2. Ver detalle de un socio
    page.locator("table tbody tr").first.locator("button").first.click()
    page.wait_for_timeout(450)

    #3. Cancelar "Ver detalle"
    page.get_by_role("button", name="Cancelar", exact=True).click(force=True)
    page.wait_for_timeout(500)

    #4. Realizar un nuevo cobro
    page.get_by_role("button", name="Nuevo", exact=False).click()
    page.wait_for_timeout(500)
    
    #5. Buscar en "Nuevo cobro"
    buscador = page.locator("#busqueda-socio-cobro")
    buscador.fill("47852685")
    buscador.press("Enter")
    page.wait_for_timeout(600)
    page.get_by_role("button", name="Seleccionar", exact=True).first.click(force=True)
    page.get_by_role("button", name="Cancelar", exact=True).first.click(force=True)

    #6. Buscar por estado
    page.locator("app-select[etiqueta='Estado'] button").click()
    page.get_by_role("listbox").get_by_text("Pendiente", exact=True).click(force=True)
    page.locator("app-select[etiqueta='Estado'] button").click()
    page.get_by_role("listbox").get_by_text("Vencida", exact=True).click(force=True)
    page.locator("app-select[etiqueta='Estado'] button").click()
    page.get_by_role("listbox").get_by_text("Pagada", exact=True).click(force=True)
    page.locator("app-select[etiqueta='Estado'] button").click()
    page.get_by_role("listbox").get_by_text("Anulada", exact=True).click(force=True)
    page.locator("app-select[etiqueta='Estado'] button").click()
    page.get_by_role("listbox").get_by_text("Todos", exact=True).click(force=True)
    page.wait_for_timeout(1000)

    #7. Buscar por tipo
    page.locator("app-select[etiqueta='Tipo'] button").click()
    page.get_by_role("listbox").get_by_text("Social", exact=True).click(force=True)
    page.locator("app-select[etiqueta='Tipo'] button").click()
    page.get_by_role("listbox").get_by_text("Actividad", exact=True).click(force=True)
    page.locator("app-select[etiqueta='Tipo'] button").click()
    page.get_by_role("listbox").get_by_text("Todos", exact=True).click(force=True)
    page.wait_for_timeout(1000)

