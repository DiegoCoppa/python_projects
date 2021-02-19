# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
import os 
from sys import exc_info
from .forms import NameForm
#from .forms import UploadFileForm
from .forms import DocumentFormXml
from .models import DccUsers, DccDepts, XmlDocuments
from .functions import parsexml


def get_user(request):
    try:
        if(request.method == 'GET'):
            form = NameForm()
            
            return render(request, 'dcc/get_user.v1.html', {'form': form})
        
        elif request.method == 'POST':
            # create a form instance and populate it with data from the request:
            formInfo = NameForm(request.POST) #usa el forms.py
            if formInfo.is_valid():
                #el user guardado en el forms que subió el usuario
                user_accessing=str(formInfo.cleaned_data['user'])
                try:
                    #asigna el usuario 
                    userListedString=str(list((DccUsers.objects.filter(dcc_user=user_accessing)))[0])
                    userListed={userListedString}
                    return HttpResponseRedirect(reverse('access',args=(userListedString,)))
                except Exception as ex:
                    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(ex).__name__, ex.args)
                    print (message)
            else: 
                print("not valid")
        
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print (message)

def access(request,userListedString):
    try:
        
        if(request.method == 'GET'):
                      
            ###Info general###
            #busco en la base de datos la info del usuario
            Name=str(DccUsers.objects.get(dcc_user=userListedString).dcc_nombre_full)
            permiso=str(DccUsers.objects.get(dcc_user=userListedString).dcc_permisosuser)
            departamento=str(DccUsers.objects.get(dcc_user=userListedString).dcc_belong_Dept)
            mail=str(DccUsers.objects.get(dcc_user=userListedString).dcc_Email)
            Centro=str(DccUsers.objects.get(dcc_user=userListedString).dcc_belong_Dept.dcc_centro)

            # creo una form para preapararme a subir el archivo form + model
            form = DocumentFormXml()
            
            #lista de documentos guardados y que solo el usuario creó
            documents = XmlDocuments.objects.filter(dcc_user=DccUsers.objects.get(dcc_user=userListedString).id)            
            
            #info del usuario de la base de datos  + los archivos para pasárselo al http
            user = {
                'user' : userListedString,
                'Name' : Name,
                'permisos' : permiso,
                'departamento' : departamento,
                'email': mail,
                'Centro': Centro,
                'form' : form,
                'documents': documents
                }
                        
            return render(request, 'dcc/access.v1.html', user)
        elif request.method == 'POST':
                      
           #uploaded docs handled with forms + models
           form = DocumentFormXml(request.POST, request.FILES)
                    
           if  form.is_valid():
                              
               xmldocument=form.save(commit = False) #verque es
               xmldocument.dcc_user = DccUsers.objects.get(dcc_user=userListedString)
               xmldocument.save()
               #xmltohttp(userListedString, xmldocument)
               
               ###Info general###
               Name=str(DccUsers.objects.get(dcc_user=userListedString).dcc_nombre_full)
               
               #documentos que subió el usuario
               documents = XmlDocuments.objects.filter(dcc_user=DccUsers.objects.get(dcc_user=userListedString).id)            

               user = {
                'user' : userListedString,
                'Name' : Name,
                'documents': documents
                }
               
               return render(request, 'dcc/get_file.v1.html', user)
         
           else:
               print (form.errors)
               return HttpResponse(form.errors)
    
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print (message)
        
        
def xmltohttp(request):
    return