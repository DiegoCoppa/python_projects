from django.db import models
from django.utils import timezone
import datetime

class DccDepts(models.Model):
    def __str__(self):
        return self.dcc_dept
    dcc_dept = models.CharField(max_length=20,default='')
    dcc_centro = models.CharField(max_length=20,default='')
    dcc_PermisosDept = models.IntegerField(default=0)
    dcc_CentroDeCosto = models.IntegerField(default=0)

class DccUsers(models.Model):
    def __str__(self):
        return self.dcc_user
    dcc_user = models.CharField(max_length=10,default='')
    dcc_pass_full = models.CharField(max_length=8,default='')
    dcc_nombre_full = models.CharField(max_length=150,default='')
    dcc_belong_Dept = models.ForeignKey(DccDepts, on_delete=models.CASCADE,default=1)
    dcc_permisosuser = models.IntegerField(default=0)
    dcc_Email = models.CharField(max_length=150,default='')

class DccProcs(models.Model):
    def __str__(self):
        return self.dcc_proc
    dcc_proc_nombre = models.CharField(max_length=20,default='')
    dcc_dept_manager = models.ForeignKey(DccDepts, on_delete=models.CASCADE,default=1)
    dcc_root_folder = models.CharField(max_length=150,default='')
    
class DccCerts(models.Model):
    def __str__(self):
        return self.dcc_proc
    tipo = models.CharField(max_length=10,default='')
    dcc_numero_certificado = models.IntegerField(default=0)
    dcc_numero_parcial = models.IntegerField(default=0)
    dcc_user = models.ForeignKey(DccUsers, on_delete=models.CASCADE,default=1)
    dcc_proc = models.ForeignKey(DccProcs, on_delete=models.CASCADE,default=1)
    dcc_root_folder = models.CharField(max_length=150,default='')
    pub_date = models.DateTimeField('date published')


"""
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.dcc_user.id, filename)
"""
"""
class XmlDocuments(models.Model):
    def __str__(self):
        return self.xmldocument
    description = models.CharField(max_length=255, blank=True)
    xmldocument = models.FileField(upload_to='xml/documents/%Y%m%d%M%S')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    dcc_user = models.ForeignKey(DccUsers, on_delete=models.CASCADE,default=1)
    #xmldocument = models.FileField(upload_to=user_directory_path)

        
"""
      
      
      
    
     
	 
		
  
    
