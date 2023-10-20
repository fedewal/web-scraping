# import requests
# import scrapy
# from lxml import html

# encabezados = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
# }

# url = "https://www.wikipedia.org/"

# respuesta = requests.get(url,headers=encabezados)

# parser = html.fromstring(respuesta.text)

# ingles = parser.get_element_by_id("js-link-box-en")
# ingles = parser.xpath("//a[@id='js-link-box-en']/strong/text()")

# print(ingles)


from selenium import webdriver

# Inicializar el navegador
driver = webdriver.Chrome()

# Abrir una página web
driver.get("https://www.covercompany.com.uy/catalogo/iphone-14-128gb-6gb-ram-5g-6-1-chip-a15-bionic-oled-retina-xdr-midnight_2-3386_9521")

driver.execute_script("window.elements = [];")

# Definir una función JavaScript que maneje los clics
click_handler_script = '''
    window.addEventListener('click', function(event) {
        var element = event.target;
        if (element) {
            console.log(element);
            elements.push(element);
        }
    });

    // Agregar evento 'mouseover' para cambiar el fondo a naranja tenue
    document.addEventListener('mouseover', function(event) {
        var element = event.target;
        if (element) {
            element.style.backgroundColor = 'rgba(255, 165, 0, 0.5)'; // Color naranja tenue
        }
    });

    // Agregar evento 'mouseout' para restaurar el fondo
    document.addEventListener('mouseout', function(event) {
        var element = event.target;
        if (element) {
            element.style.backgroundColor = ''; // Restaurar el fondo
        }
    });
'''

# Ejecutar el script en el navegador
driver.execute_script(click_handler_script)
# Esperar a que el usuario interactúe con la ventana
input("Haz clic en elementos de la página y posiciona el mouse sobre ellos. Luego presiona Enter para finalizar.")

elements = driver.execute_script("return window.elements;")
print(elements)
print(elements[0].get_attribute('xpath'))

# Cerrar el navegador
driver.quit()