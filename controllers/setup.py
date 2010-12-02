# coding: utf8
# try something like

def crear_tipos_doc(): 
    "Crear inicialmente los tipos de documento más usados"
    data = """\
80 - CUIT
86 - CUIL
87 - CDI
89 - LE
90 - LC
92 - en trámite
96 - DNI
94 - Pasaporte
99 - Consumidor Final"""
    db(db.tipo_doc.cod>0).delete()
    l = []
    for d in data.split("\n"):
        i, desc = d.split(" - ")
        db.tipo_doc.insert(cod=i, desc=desc)
    return dict(ret=SQLTABLE(db(db.tipo_doc.cod>0).select()))
    
def crear_tipos_cbte(): 
    "Crear inicialmente los tipos de comprobantes más usados"
    data = """\
1 - Factura A
2 - Nota de Débito A
3 - Nota de Crédito A
4 - Recibo A
6 - Factura B
7 - Nota de Débito B
8 - Nota de Crédito B
9 - Recibo B
11 - Factura C
12 - Nota de Débito C
13 - Nota de Crédito C
15 - Recibo C
19 - Factura E
20 - Nota de Débito E
21 - Nota de Crédito E
51 - Factura M
52 - Nota de Débito M
53 - Nota de Crédito M
54 - Recibo M"""
    db(db.tipo_cbte.cod>0).delete()
    l = []
    for d in data.split("\n"):
        i, desc = d.split(" - ")
        db.tipo_cbte.insert(cod=i, desc=desc)
    return dict(ret=SQLTABLE(db(db.tipo_cbte.cod>0).select()))
    
def crear_monedas(): 
    "Crear inicialmente las monedas más usadas"
    data = """\
PES - Pesos Argentinos
DOL - Dólar Estadounidense
012 - Real
019 - Yens
060 - Euro"""
    db(db.moneda.id>0).delete()
    l = []
    for d in data.split("\n"):
        i, desc = d.split(" - ")
        db.moneda.insert(cod=i, desc=desc)
    return dict(ret=SQLTABLE(db(db.moneda.id>0).select()))
    

# coding: utf8
# try something like

def crear_tipos_doc(): 
    "Crear inicialmente los tipos de documento más usados"
    data = """\
80 - CUIT
86 - CUIL
87 - CDI
89 - LE
90 - LC
92 - en trámite
96 - DNI
94 - Pasaporte
99 - Consumidor Final"""
    db(db.tipo_doc.cod>0).delete()
    l = []
    for d in data.split("\n"):
        i, desc = d.split(" - ")
        db.tipo_doc.insert(cod=i, desc=desc)
    return dict(ret=SQLTABLE(db(db.tipo_doc.cod>0).select()))
    
def crear_iva(): 
    "Crear inicialmente las alícuotas de IVA más usados"
    data = """\
1 - No gravado
2 - Exento
3 - 0%
4 - 10.5%
5 - 21%
6 - 27%"""
    db(db.iva.cod>0).delete()
    l = []
    for d in data.split("\n"):
        i, desc = d.split(" - ")
        db.iva.insert(cod=i, desc=desc)
    return dict(ret=SQLTABLE(db(db.iva.cod>0).select()))
    
def crear_idiomas(): 
    "Crear inicialmente los idiomas"
    data = """\
1 - Español
2 - Inglés
3 - Portugués"""
    db(db.moneda.id>0).delete()
    l = []
    for d in data.split("\n"):
        i, desc = d.split(" - ")
        db.moneda.insert(cod=i, desc=desc)
    return dict(ret=SQLTABLE(db(db.moneda.id>0).select()))

def crear_umedidas():
    data = """\
1 - kilogramos
5 - litros
7 - unidades
2 - metros
3 - metros cuadrados
4 - metros cúbicos
0 -  """
   
    db(db.umed.cod>=0).delete()
    l = []
    for d in data.split("\n"):
        i, desc = d.split(" - ")
        db.umed.insert(cod=i, desc=desc)
    return dict(ret=SQLTABLE(db(db.umed.id>0).select()))

def crear_paises():
    data = {200: u'ARGENTINA', 202: u'BOLIVIA', 203: u'BRASIL', 204: u'CANADA', 205: u'COLOMBIA', 206: u'COSTA RICA', 207: u'CUBA', 208: u'CHILE', 210: u'ECUADOR', 211: u'EL SALVADOR', 212: u'ESTADOS UNIDOS',  218: u'MEXICO', 221: u'PARAGUAY', 222: u'PERU', 225: u'URUGUAY', 226: u'VENEZUELA', 250: u'AAE Tierra del Fuego - ARGENTINA', 251: u'ZF La Plata - ARGENTINA', 252: u'ZF Justo Daract - ARGENTINA', 253: u'ZF R\xedo Gallegos - ARGENTINA', 254: u'Islas Malvinas - ARGENTINA', 255: u'ZF Tucum\xe1n - ARGENTINA', 256: u'ZF C\xf3rdoba - ARGENTINA', 257: u'ZF Mendoza - ARGENTINA', 258: u'ZF General Pico - ARGENTINA', 259: u'ZF Comodoro Rivadavia - ARGENTINA', 260: u'ZF Iquique', 261: u'ZF Punta Arenas', 262: u'ZF Salta - ARGENTINA', 263: u'ZF Paso de los Libres - ARGENTINA', 264: u'ZF Puerto Iguaz\xfa - ARGENTINA', 265: u'SECTOR ANTARTICO ARG.', 270: u'ZF Col\xf3n - REP\xdaBLICA DE PANAM\xc1', 271: u'ZF Winner (Sta. C. de la Sierra) - BOLIVIA', 280: u'ZF Colonia - URUGUAY', 281: u'ZF Florida - URUGUAY', 282: u'ZF Libertad - URUGUAY', 283: u'ZF Zonamerica - URUGUAY', 284: u'ZF Nueva Helvecia - URUGUAY', 285: u'ZF Nueva Palmira - URUGUAY', 286: u'ZF R\xedo Negro - URUGUAY', 287: u'ZF Rivera - URUGUAY', 288: u'ZF San Jos\xe9 - URUGUAY', 291: u'ZF Manaos - BRASIL', }
    for k,v in data.items():
        db.pais_dst.insert(cod=k, desc=v)
    return dict(ret=SQLTABLE(db(db.pais_dst.id>0).select()))