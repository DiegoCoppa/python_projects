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
from .functions import readxlsfun


def get_user(request):
    # if this is a POST request we need to process the form data
    try:
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            formInfo = NameForm(request.POST) #usa el forms.py
            # check whether it's valid:
            if formInfo.is_valid():
                #el user guardado en el forms que subió el usuario
                user_accessing=str(formInfo.cleaned_data['user'])
                #print(user_accessing)
                try:
                    userListedString=str(list((DccUsers.objects.filter(dcc_user=user_accessing)))[0])
                    #print(userListedString)
                    userListed={userListedString}
                    return HttpResponseRedirect(reverse('access',args=(userListedString,)))
                except Exception as ex:
                    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(ex).__name__, ex.args)
                    print (message)
            else: 
                print("not valid")
        else:
            
            
            form = NameForm()
            return render(request, 'dcc/get_user.v1.html', {'form': form})
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print (message)

def access(request,userListedString):
    try:
        if request.method == 'POST':
           #print("post")
           #uploaded docs handled with forms + models
           form = DocumentFormXml(request.POST, request.FILES)
           print(form.data['dcc_user'])
           
           #uploaded docs handled with forms + models
           #form = UploadFileForm(request.POST, request.FILES)
           
           if  form.is_valid():
               #print(request.FILES['file'])
               #handle_uploaded_file(request.FILES['file'],userListedString)
               
               #uploaded docs handled with forms + models
               newdoc = XmlDocuments(xmldocument=request.FILES['xmldocument'])
               newdoc.save()
               #handle_uploaded_file(request.FILES['file'])
               
               #print(str(newdoc.objects.get()))
               
               #print(newdoc.xmldocument)
               #DocumentsXml.objects.last().dcc_user_id=DccUsers.objects.get(dcc_user=userListedString).dcc_user_id
               return render(request, 'dcc/access.v1.html')
               #return HttpResponse("holass")
         
           else:
               print (form.errors)
               return HttpResponse(form.errors)
        else:
            #print("only get")
            #busco en la base de datos la info del usuario
            Name=str(DccUsers.objects.get(dcc_user=userListedString).dcc_nombre_full)
            permiso=str(DccUsers.objects.get(dcc_user=userListedString).dcc_permisosuser)
            departamento=str(DccUsers.objects.get(dcc_user=userListedString).dcc_belong_Dept)
            mail=str(DccUsers.objects.get(dcc_user=userListedString).dcc_Email)
            Centro=str(DccUsers.objects.get(dcc_user=userListedString).dcc_belong_Dept.dcc_centro)
            #Busco los 
            documents= XmlDocuments.objects.all()
            
            # creo una form para preapararme a subir el archivo form + model
            form = DocumentFormXml()
            
            # creo una form para preapararme a subir el archivo
            #form = UploadFileForm
            
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
            #lista de documentos guardados
            return render(request, 'dcc/access.v1.html', user)
        
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print (message)
 

def handle_uploaded_file(f,userListedString):
    with open('/media/diego/E4D5-3D00/dcc.fisica/xmlsFolder/'+userListedString+'/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def xmltohttp(request,userListedString):
    return HttpResponse("done")
    """
    try:
        
        documents = XmlDocuments.objects.all()
        return render(request,'dcc/get_file.html', {'documents': documents})
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print (message)
"""