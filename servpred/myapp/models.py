from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, correo, contrasena, **extra_fields):
        if not correo:
            raise ValueError('El correo debe ser proporcionado')
        user = self.model(correo=correo, **extra_fields)
        user.set_password(contrasena)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, contrasena, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(correo, contrasena, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['']

    def __str__(self):
        return self.correo

class Servers(models.Model):
    id = models.AutoField(primary_key=True)
    server = models.CharField(max_length=100)
    standart = models.DateTimeField(auto_now_add=True)
    diskname = models.CharField(max_length=100)
    totalsize = models.DecimalField(max_digits=12, decimal_places=2)
    freegigabytes = models.DecimalField(max_digits=12, decimal_places=2)
    usedbytes = models.DecimalField(max_digits=5, decimal_places=2)
    freebytes = models.DecimalField(max_digits=5, decimal_places=2)
    temdisk = models.DecimalField(max_digits=5, decimal_places=2)
    readwritenspead = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.server
    
class Recomendations(models.Model):
     id = models.AutoField(primary_key=True)
     recomends = models.CharField(max_length=100)
     creaciondate = models.DateTimeField(auto_now_add=True)
     estados = models.CharField(max_length=100)

     def __str__(self):
         return self.recomends

class RegistroAuditoria(models.Model):
    id = models.AutoField(primary_key=True)
    nameaudit = models.CharField(max_length=200, unique=True)
    ruteaudit = models.CharField(max_length=15, blank=True, null=True)
    phoneaudit = models.CharField(max_length=200, blank=True, null=True)
    emailaudit = models.EmailField(max_length=200, blank=True, null=True)
    companipositionaudit = models.CharField(max_length=200, blank=True, null=True)
    dateaudit = models.DateField(blank=True, null=True)
    typeaudit = models.CharField(max_length=200, blank=True, null=True)
    typedocument = models.BinaryField(blank=True, null=True)
    textaudit = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nameaudit} - {self.ruteaudit}'

class Monitor(models.Model):
    id = models.AutoField(primary_key=True)
    serverm = models.CharField(max_length=100)
    standartm = models.DateTimeField(auto_now_add=True)
    disknamem = models.CharField(max_length=100)
    totalsizem = models.DecimalField(max_digits=12, decimal_places=2)
    usedgigasbytsm = models.DecimalField(max_digits=12, decimal_places=2)
    freegigabytes = models.DecimalField(max_digits=12, decimal_places=2)
    tempdiskm = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.serverm
    
class DataAnalytic(models.Model):
    id = models.AutoField(primary_key=True)
    serverd = models.CharField(max_length=100)
    standartd = models.DateTimeField(auto_now_add=True)
    disknamed = models.CharField(max_length=100)
    totalsized = models.DecimalField(max_digits=12, decimal_places=2)
    usedgigasbytsd = models.DecimalField(max_digits=12, decimal_places=2)
    freegigabytesd = models.DecimalField(max_digits=5, decimal_places=2)
    usedbytesd = models.DecimalField(max_digits=12, decimal_places=2)
    freebytesd = models.DecimalField(max_digits=12, decimal_places=2)
    tempdiskd = models.DecimalField(max_digits=5, decimal_places=2)
    readwritenspeadd = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.serverd
    
class KpiAnalytic(models.Model):
    id = models.AutoField(primary_key=True)
    serverx = models.CharField(max_length=100)
    standardx = models.DateField(auto_now_add=True)
    disknamex = models.CharField(max_length=100)
    costownership = models.DecimalField(max_digits=1000, decimal_places=2)
    returninvestment = models.DecimalField(max_digits=1000, decimal_places=2)
    durabilityfilespan = models.DecimalField(max_digits=1000, decimal_places=2)
    maintcost = models.DecimalField(max_digits=1000, decimal_places=2)

    def __str__(self):
        return self.costownership
    





