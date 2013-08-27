### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_niveles',
    Field('f_nivel', type='string',
          label=T('Nivel')),
    auth.signature,
    format='%(f_nivel)s',
    migrate=settings.migrate)

db.define_table('t_niveles_archive',db.t_niveles,Field('current_record','reference t_niveles',readable=False,writable=False))

########################################
db.define_table('t_empresas',
    Field('f_empresa', type='string',
          label=T('Empresa')),
    auth.signature,
    format='%(f_empresa)s',
    migrate=settings.migrate)

db.define_table('t_empresas_archive',db.t_empresas,Field('current_record','reference t_empresas',readable=False,writable=False))

########################################
db.define_table('t_estados',
    Field('f_estado', type='string',
          label=T('Estado')),
    auth.signature,
    format='%(f_estado)s',
    migrate=settings.migrate)

db.define_table('t_estados_archive',db.t_estados,Field('current_record','reference t_estados',readable=False,writable=False))

########################################
db.define_table('t_sucursales',
    Field('f_empresa', type='reference t_empresas',
          label=T('Empresa')),
    Field('f_sucursal', type='string',
          label=T('Sucursal')),
    Field('f_estado', type='reference t_estados',
          label=T('Estado')),
    auth.signature,
    format='%(f_sucursal)s',
    migrate=settings.migrate)

db.define_table('t_sucursales_archive',db.t_sucursales,Field('current_record','reference t_sucursales',readable=False,writable=False))

########################################
db.define_table('t_departamentos',
    Field('f_empresa', type='reference t_empresas',
          label=T('Empresa')),
    Field('f_sucursal', type='reference t_sucursales',
          label=T('Sucursal')),
    Field('f_departamento', type='string',
          label=T('Departamento')),
    auth.signature,
    format='%(f_departamento)s',
    migrate=settings.migrate)

db.define_table('t_departamentos_archive',db.t_departamentos,Field('current_record','reference t_departamentos',readable=False,writable=False))

########################################
db.define_table('t_puestos',
    Field('f_puesto', type='string',
          label=T('Puesto')),
    Field('f_nivel', type='reference t_niveles',
          label=T('Nivel')),
    auth.signature,
    format='%(f_puesto)s',
    migrate=settings.migrate)

db.define_table('t_puestos_archive',db.t_puestos,Field('current_record','reference t_puestos',readable=False,writable=False))

########################################
db.define_table('t_datos',
    Field('f_clave_noi', type='string', unique=True,
          label=T('Clave Noi')),
    Field('f_nombre', type='string', notnull=True, unique=True,
          label=T('Nombre')),
    Field('f_estatus', type='string', notnull=True,
          label=T('Estatus')),
    Field('f_fecha_nacimiento', type='date',
          label=T('Fecha Nacimiento')),
    Field('f_foto', type='upload',
          label=T('Foto')),
    Field('f_email', type='string',
          label=T('Email')),
    Field('f_telefono', type='string',
          label=T('Telefono')),
    Field('f_fecha_alta', type='date', notnull=True,
          label=T('Fecha Alta')),
    Field('f_estatus', type='string',
          label=T('Estatus')),
    Field('f_fecha_baja', type='date',
          label=T('Fecha Baja')),
    Field('f_ife', type='upload',
          label=T('Ife')),
    Field('f_contrato', type='upload',
          label=T('Contrato')),
    Field('f_escolaridad', type='string',
          label=T('Escolaridad')),
    Field('f_observaciones', type='string',
          label=T('Observaciones')),
    Field('f_empresa', type='reference t_empresas',
          label=T('Empresa')),
    Field('f_sucursal', type='reference t_sucursales',
          label=T('Sucursal')),
    Field('f_departamento', type='reference t_departamentos',
          label=T('Departamento')),
    Field('f_puesto', type='reference t_puestos',
          label=T('Puesto')),
    Field('f_nivel', type='reference t_niveles',
          label=T('Nivel')),
    Field('f_fijo_15d', type='string',
          label=T('Fijo 15d')),
    Field('f_noi_15d_max', type='string',
          label=T('Noi 15d Max')),
    auth.signature,
    format='%(f_nombre)s',
    migrate=settings.migrate)

db.define_table('t_datos_archive',db.t_datos,Field('current_record','reference t_datos',readable=False,writable=False))

########################################
db.define_table('t_nomina1a',
    Field('f_nombre', type='reference t_datos',
          label=T('Nombre ')),
    Field('f_dias_lab', type='integer',
          label=T('Dias Lab')),
    Field('f_ingreso_fijo', type='double',
          label=T('Ingreso Fijo')),
    Field('f_unidades', type='integer',
          label=T('Unidades')),
    Field('f_ingreso_comision', type='double',
          label=T('Ingreso Comision')),
    Field('f_ingreso_bono', type='double',
          label=T('Ingreso Bono')),
    Field('f_ingreso_otros', type='double',
          label=T('Ingreso Otros')),
    Field('f_descuento_1', type='double',
          label=T('Descuento 1')),
    Field('f_descuento_2', type='double',
          label=T('Descuento 2')),
    Field('f_total', type='double',
          label=T('Total')),
    auth.signature,
    format='%(f_clave_noi)s',
    migrate=settings.migrate)

db.define_table('t_nomina1a_archive',db.t_nomina1a,Field('current_record','reference t_nomina1a',readable=False,writable=False))
