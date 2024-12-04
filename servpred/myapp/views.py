from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  
            messages.success(request, 'Usuario creado correctamente')
            return redirect('login')  
        else:
            messages.error(request, 'Error al crear el usuario. Por favor, revisa los datos e intenta de nuevo.')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f'Username: {username}, Password: {password}')  
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('welcome')
            else:
                messages.error(request, 'Credenciales incorrectas. Inténtelo de nuevo.')
        else:
            messages.error(request, 'Formulario inválido. Por favor, revise los campos.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return redirect('login') 

def logout_view(request):
    from django.contrib.auth import logout as auth_logout
    auth_logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente')
    return redirect('login')  

def welcome(request):
    return render(request, 'welcome.html')  

def menu(request):
    return render(request, 'menu.html')

def inicio(request):
    return render(request, 'inicio.html')

def monitoreo(request):
    return render(request, 'monitoreo.html')

from django.http import JsonResponse
from .models import Monitor  

def obtener_datos_monitor(request):
    # Consulta todos los datos del modelo Monitor
    datos = Monitor.objects.all().values('id', 'serverm', 'standartm', 'disknamem', 'totalsizem','usedgigasbytsm', 'freegigabytes', 'tempdiskm')
    # Devuelve los datos en formato JSON
    return JsonResponse(list(datos), safe=False)

from django.http import JsonResponse
from .models import DataAnalytic

def obtener_datos_dataanalytic(request):
    try:
        datos = DataAnalytic.objects.all().values(
            'id', 'serverd', 'standartd', 'disknamed', 
            'totalsized', 'usedgigasbytsd', 'freegigabytesd', 
            'usedbytesd', 'freebytesd', 'tempdiskd', 'readwritenspeadd'
        )
        return JsonResponse(list(datos), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def analisispredictivo(request):
    return render(request, 'analisispredictivo.html')

def auditoria(request):
    return render(request, 'auditoria.html')

def analisisdedatos(request):
    return render(request, 'analisisdedatos.html')

def recomendaciones(request):
    return render(request, 'recomendaciones.html')

from django.http import JsonResponse
from .models import CustomUser

def datos_administrador(request):
    usuario = request.user 
    data = {
            'username': usuario.username,
             'correo': usuario.correo,
             'fecha_registro' : usuario.fecha_registro,
            }
    return JsonResponse(data)

def administracion(request):
    return render(request, 'administracion.html')

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import RegistroAuditoria

def auditoria(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nameaudit = request.POST.get('nameaudit')
        ruteaudit = request.POST.get('ruteaudit')
        phoneaudit = request.POST.get('phoneaudit')
        emailaudit = request.POST.get('emailaudit')
        companipositionaudit = request.POST.get('companipositionaudit')
        dateaudit = request.POST.get('dateaudit')
        typeaudit = request.POST.get('typeaudit')
        textaudit = request.POST.get('textaudit')

        # Manejar el archivo adjunto
        typedocument = request.FILES.get('typedocument') if request.FILES else None

        try:
            # Crear un nuevo registro en la base de datos
            reporte = RegistroAuditoria(
                nameaudit=nameaudit,
                ruteaudit=ruteaudit,
                phoneaudit=phoneaudit,
                emailaudit=emailaudit,
                companipositionaudit=companipositionaudit,
                dateaudit=dateaudit,
                typeaudit=typeaudit,
                textaudit=textaudit,
                typedocument=typedocument.read() if typedocument else None  # Convertir archivo en binario
            )
            reporte.save()

            # Devolver respuesta en formato JSON para AJAX
            return JsonResponse({'status': 'success', 'message': 'El reporte se ha agregado exitosamente.'})
        except Exception as e:
            # En caso de error
            return JsonResponse({'status': 'error', 'message': f'Error al agregar el reporte: {e}'})

    return render(request, 'auditoria.html')

from django.http import JsonResponse
from .models import RegistroAuditoria

def obtener_auditorias(request):
    if request.method == 'GET':
        auditorias = RegistroAuditoria.objects.all().values(
            'id', 'nameaudit', 'ruteaudit', 'phoneaudit', 'emailaudit', 
            'companipositionaudit', 'dateaudit', 'typeaudit', 'textaudit'
        )
        data = list(auditorias)
        return JsonResponse(data, safe=False)

from django.http import JsonResponse
from .models import KpiAnalytic  # Asegúrate de que el modelo correcto esté importado

def obtener_kpi_relevantes(request):
    if request.method == 'GET':
        # Obtener todos los registros del modelo KpiAnalytic
        auditorias = KpiAnalytic.objects.all().values(
            'id', 'serverx', 'standardx', 'disknamex', 'costownership',
            'returninvestment', 'durabilityfilespan', 'maintcost'
        )
        
        # Convertir los registros en una lista y enviarlos como JSON
        data = list(auditorias)
        return JsonResponse(data, safe=False)

from django.http import JsonResponse
from .models import Servers  # Asegúrate de que el modelo correcto esté importado

def obtener_servers(request):
    if request.method == 'GET':
        # Obtener todos los registros del modelo Servers
        servers = Servers.objects.all().values(
            'id', 'server', 'standart', 'diskname', 'totalsize',
            'freegigabytes', 'usedbytes', 'freebytes', 'temdisk',
            'readwritenspead'
        )
        
        # Convertir los registros en una lista y enviarlos como JSON
        data = list(servers)
        return JsonResponse(data, safe=False)


from django.http import JsonResponse
from .models import Recomendations  # Asegúrate de que el modelo correcto esté importado

def obtener_recomendations(request):
    if request.method == 'GET':
        # Obtener todos los registros del modelo Servers
        recomendations = Recomendations.objects.all().values(
            'id', 'recomends', 'creaciondate', 'estados'
        )
        
        # Convertir los registros en una lista y enviarlos como JSON
        data = list(recomendations)
        return JsonResponse(data, safe=False)
