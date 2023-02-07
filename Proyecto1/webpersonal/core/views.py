from django.shortcuts import render, HttpResponse

# Create your views here.


html_base = """
<h1>Mi web Personal</h1>
<ul>
    <li><a href="/">Home<a/></li>
    <li><a href="/about">About<a/></li>
    <li><a href="/portfolio">Portfolio<a/></li>
    <li><a href="/contacto">Contacto<a/></li>
</ul>    
"""


def home(request):
    return HttpResponse(html_base+"<h2>Home</h2><p>Este es el home</p>")


def about(request):
    return HttpResponse(html_base+"<h2>Acerca De</h2><p>Este es el about </p>")


def portfolio(request):
    return HttpResponse(html_base + "<h2>Portfolio</h2><p>Este es el portfolio </p>")

# crear una pagina de contacto


def contacto(request):
    return HttpResponse(html_base+"<h2>Contacto</h2><p>Este es el contacto </p>")
