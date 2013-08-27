# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

@auth.requires_login()
def datos_manage():
    form = SQLFORM.smartgrid(db.t_datos,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def empresas_manage():
    form = SQLFORM.smartgrid(db.t_empresas,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def sucursales_manage():
    form = SQLFORM.smartgrid(db.t_sucursales,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def departamentos_manage():
    form = SQLFORM.smartgrid(db.t_departamentos,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def puestos_manage():
    form = SQLFORM.smartgrid(db.t_puestos,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def niveles_manage():
    form = SQLFORM.smartgrid(db.t_niveles,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def estados_manage():
    form = SQLFORM.smartgrid(db.t_estados,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def nomina1a_manage():
    form = SQLFORM.smartgrid(db.t_nomina1a,onupdate=auth.archive)
    return locals()

