from django.shortcuts import HttpResponse
from django.shortcuts import render
html_base = """
 <h1>Shopping Car</h1>
 <ul>
   <li><a href="/">Inicio</a></li>
   <li><a href="/articulo/">Articulos</a></li>
   <li><a href="/cliente/">Clientes</a></li>
   <li><a href="/venta/">Ventas</a></li>
   <li><a href="/consulta/">Consultas</a></li>
 </li>
"""
def inicio(request):
    data = {
        'titulo':"Inicio"
    }
    return render(request,'base.html',data)


def articulo(request):
  return HttpResponse(html_base+
    """<h2>Mantenimiento de Articulo</h2>
       <p>List de articulos</p>""")

def cliente(request):
  data = {
      'titulo':'GESTION DE CLIENTES',
      'crear_url': '/crearcliente',
      'listar_url': '/cliente',
      'cancelar_url':'/venta',
  }
  return render(request, "ventas/clientes/listCliente.html",data)

def crearCliente(request):
  data = {
      'titulo':'MANTENIMIENTO DE CLIENTES',
      'crear_url':'/crearcliente',
      'action':'add',
      'listar_url': '/cliente',
  }
  return render(request, "ventas/clientes/formCliente.html",data)

def venta(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "ventas/ventas.html",data)


# ***********novedades************
def novedades(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "novedades/novedades.html",data)
# ***********prestamos************
def lisempleados(request):
  data = {
      'titulo': 'LISTA DE EMPLEADOS',
      'crear_url': '/lisempleados',
      'listar_url': '/novedades',
  }
  return render(request, "novedades/prestamos/lisempleados.html",data)

def lisPrestamos(request):
  data = {
      'titulo':'LISTA DE PRESTAMOS',
      'crear_url': '/nuevoprestamo',
      'action': 'add',
      'listar_url': '/lisprestamos',
      'cancelar_url':'/novedades',
  }
  return render(request, "novedades/prestamos/lisprestamos.html",data)

def nuevoPrestamo(request):
  data = {
      'titulo':'NUEVO PRESTAMO',
      'crear_url': '/lisprestamos',
      'action': 'add',
      'listar_url': '/lisprestamos',
  }
  return render(request, "novedades/prestamos/nuevoprestamo.html",data)

def editarPrestamo(request):
  data = {
    'titulo':'EDITAR PRESTAMO',
    'crear_url': '/lisprestamos',
    'action': 'add',
    'listar_url': '/lisprestamos',
}
  return render(request, "novedades/prestamos/editarprestamo.html",data)

def detallePrestamo(request):
  data = {
  'titulo':'DETALLE DEL PRESTAMO',
  'crear_url': '/detalleprestamo',
  'action': 'add',
  'listar_url': '/lisprestamos',
}
  return render(request, "novedades/prestamos/detalleprestamo.html",data)

# ***********novedades************

def lisDescuentos(request):
  data = {
      'titulo':'LISTA DE DESCUENTOS',
      'crear_url': '/nuevodescuento',
      'action': 'add',
      'listar_url': '/lisdescuento',
      'cancelar_url':'/novedades',
  }
  return render(request, "novedades/descuento/lisdescuento.html",data)

def nuevoDescuentos(request):
  data = {
      'titulo':'NUEVO DESCUENTO',
      'crear_url': '/lisdescuento',
      'action': 'add',
      'listar_url': '/lisdescuento',
      'nuevo_url': '/nuevaempresa',
  }
  return render(request, "novedades/descuento/nuevodescuento.html",data)
def nuevaEmpresa(request):
  data = {
  'titulo':'NUEVA EMPRESA',
  'action': 'add',
  'listar_url': '/nuevodescuento',
}
  return render(request, "novedades/descuento/nuevaempresa.html",data)

def editarDescuentos(request):
  data = {
    'titulo':'EDITAR DESCUENTO',
    'crear_url': '/lisdescuento',
    'action': 'add',
    'listar_url': '/lisdescuento',
}
  return render(request, "novedades/descuento/editardescuento.html",data)

def detalleDescuentos(request):
  data = {
    'titulo':'DETALLE DEL DESCUENTO',
    'crear_url': '/detalledescuento',
    'action': 'add',
    'listar_url': '/lisdescuento',
  }
  return render(request, "novedades/descuento/detalledescuento.html",data)


