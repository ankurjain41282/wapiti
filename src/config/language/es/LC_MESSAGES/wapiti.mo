��    O      �  k         �     �     �     �     �          '     @  '   U     }     �     �  "   �  %   �          &     F     ]     z           �     �     �     �     �     	      "	     C	     a	     j	     x	     �	     �	     �	  
   �	     �	     �	     �	     
     
     
     &
     @
     ^
  &   e
     �
     �
     �
      �
     �
     �
     �
          +  	   3     =     E     _  
   s     ~     �     �     �     �  #   �     �  	   �  
   �     �  	   �                 	        $  "   )  
   L     W     c  L  o     �     �  �  �     �     �     �     �  )        8     T     g  #   |  &   �      �     �     �           !     �  @  g   *     �  �   �  c   J     �  >  �  �       �     �    �  h  �  
   3      >      J      j   -   |      �      �      �      �      �   #   !     0!  >   7!     v!     {!     �!  �  �!  _   R#     �#  s   �#    5$     M%     f%     u%     }%     �%  
   �%     �%     �%     �%     �%     �%  #   �%     &  
   &     %&     1&     =&     I&     U&  c  X&  �  �+     i3  $   m3  	   �3  
   �3     �3     A   (      #           C                 '           )       0   G             E   5          .   1         I           +       &      8              =          6   D   O   	          -      K      4          9   
             %      <   $           "          !       L   ,           F   B       N   3   ?       H   /   :   @             J   *   >      ;          M   7          2                (QUERY_STRING) (QUERY_STRING) in 500 Error description 500 HTTP Error code coming from 500 HTTP Error code in 500 HTTP Error code with 500 HTTP Error code. A report has been generated in the file Attacking forms (POST) Attacking urls (GET) Blind SQL Injection Blind SQL Injection (QUERY_STRING) Blind SQL Injection (QUERY_STRING) in Blind SQL Injection coming from Blind SQL Injection description Blind SQL Injection in Blind SQL Injection solution CRLF CRLF Injection (QUERY_STRING) in CRLF description CRLF solution Commands execution Commands execution description Commands execution solution Cross Site Scripting Cross Site Scripting description Cross Site Scripting solution Evil url File Handling File Handling description File Handling solution Form Forms Forms Info Found XSS in Found permanent XSS attacked by Found permanent XSS in From Intputs Invalid link argument Looking for permanent XSS Make sure the url is correct. Method No links or forms found in this page ! Open Report Resource consumption Resource consumption description Resource consumption solution SQL Injection SQL Injection description SQL Injection solution Selects TextAreas Timeout Timeout (QUERY_STRING) in Timeout coming from Timeout in To URLS URLs Upload Scripts Upload scripts found Wapiti-SVN (wapiti.sourceforge.net) XSS attackGET attackPOST attacked by caused by coming from in lswwwDoc wapityDoc with with a browser to see this report. with field with fields with params Project-Id-Version: Wapiti 2.1.0
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2009-05-05 12:45+0200
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: David del Pozo <dpozog@grupogesfor.com>
Language-Team: Spanish <dpozog@grupogesfor.com>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
 (QUERY_STRING) (QUERY_STRING) en Error interno del servidor. El servidor encontró un inesperado condición que le impiden el cumplimiento de la solicitud.<ul>  <li><a href='http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5'>      Consorcio World Wide Web: HTTP/1.1 Definiciones de códigos de estado (en inglés)      </a></li>  <li><a href='http://en.wikipedia.org/wiki/List_of_HTTP_status_codes#5xx_Server_Error'>      Wikipedia: Lista de códigos de estado de HTTP (en inglés)      </a></li></ul> Error HTTP 500 viniendo de Error HTTP 500 en Error HTTP 500 con Error HTTP 500 Un informe ha sido generado en el fichero Atacando formularios (POST) Atacando URL (GET) Inyección ciega SQL Inyección ciega SQL (QUERY_STRING) Inyección ciega SQL (QUERY_STRING) en Inyección ciega SQL viniendo de La inyección SQL ciega es una técnica que explota una vulnerabilidad que ocurre en la base de datos de una aplicación. Este tipo de vulnerabilidad es dificil de detectar que la inyección SQL normal porque no muestra mensajes de error en la página web. Inyección ciega SQL en Para protegerse contra las inyecciones SQL, las entradas de información que el usuario introduce en la aplicación no deben ser directamente colocadas en sentencias SQL. En vez de eso, las entradas deben ser limipiadas o filtradas o bien se deben usar sentencias parametrizadas. CRLF Inyección CRLF (QUERY_STRING) en El término CRLF se refiere al retorno de carro (ASCII 13, \r) y al salto de línea(ASCII 10, \n). Suelen usarse para delimitar la terminación de una línea, sin embargo, funcionan de forma diferente en los sistemas operativos más populares hoy en día. Por ejemplo: en Windows tanto el retorno de carro (CR) como el salto de línea (LF) son requeridos para indicar el final de la línea, mientras que en Linux/UNIX solo se necesita un salto de línea (LF). Esta combinación de retorno de carro y salto de línea se usa por ejemplo cuando se presiona 'Intro' en el teclado. Dependiendo de la aplicación que se esté usando, la presión de 'Intro' normalmente indica a la aplicación el comienzo de una nueva línea o el envío de un comando. Comprobar los parámetros enviados por el usuario y evitando que se inserten CRLF mediante su filtrado. Ejecución de comandos Este ataque consiste en ejecutar comandos del sistema en el servidor. El atacante intenta inyector estos comandos en los parametros de la petición al servidor. Preferiblemente no usar las entradas de un usuario cuando se manejen llamadas al sistema de ficheos Cross Site Scripting Cross-site scripting (XSS) es un tipo de vulnerabilidad de sistemas infomáticos que se encuentra comunmente en aplicaciones web que permite la inyección de código por usuarios maliciosos dentro de las páginas vistas por otros usuarios. Normalmente el código inyectado sueles ser HTML y lenguajes del lado cliente. La mejor forma de proteger una aplicación web de los ataques XSS es asegurarse de que la aplicacion realiza validación de todas las cabeceras, cookies, query strings, campos de formularios y campos ocultos. La codificación de los datos proporcionados por el usuario en el servidor puede también defenderse de vulnerabilidades XSS mediante la prevencion de inserción de script transmitidos por los usuarios desde formularios. Las aplicaciones puede ganar una significativa protección de los ataques basados en JavaScript mediante la conversión apropiada codificación en HTML de los siguientes caracteres: &lt;, &gt;, &amp;, &quot;, ', (, ), #, %, ; , +, - URL vulnerable Manejo de archivos Este ataque es también conocido como Path Transversal or Directory Transversal, su objetivo acceder a directorios y ficheros que son almacenados fuera del directorio en el que se encuentre la aplicación web. El atacante intenta explorar los ditectorios guardados en el servidor web usando algunas técnicas como por ejemplo, la manipulación de variables que referencian ficheros con secuencias de 'punto punto barra (../)' y sus variantes para mover hasta el directorio raíz para navegar a través del sistema de archivos. Preferiblemente no usar las entradas de un usuario cuando se manejen llamadas al sistema de ficheros<br>Usar indices mejor que porciones del nombre del fichero cuando se usen ficheros de lenguaje (por ejemplo el valor 5 para la entrada de datos de usuario por el nombre Checoslovaco, en vez de esperar que el usuario introduzca 'Checoslovaco').<br>Asegurar que el usuario no pueda la ruta entera a un fichero.<br>Validar la entrada de datos del usuario, solo aceptando las bien conocidas.<br>Usar jaulas (chrooted jails) y tener políticas de acceso para restringir por quien puede ser obtenido o salvado un fichero. Formulario Formularios Información de los formularios Encontrado XSS en Encontrados XSS permanentes atacados mediante Encontrado XSS permanente en De Entradas Argumento link (URL) inválido Buscando XSS permantentes Asegurate de que la URL es correcta Metodo ¡No se han encontrado enlaces ni formularios en esta página! Abre Informe Consumo de recursos Un atacante puede formar a una víctima a consumir más recursos de los que le está permitido consumir debido al nivel de acceso del atacante. El programa puede potencialmente fallar liberando un recurso del sistema o puede liberarlo incorrectamente. Si un recurso no es adecuadamente liberado no estará disponible para poder ser reutilizado. También puede ser un falso positivo debido al corto timeout usado en el para realizar el ataque. Configurar adecuadamente el software para evitar el consumo de memoria o la caída del sistema. Inyección SQL La inyección SQL es una técnica que explota una vulnerabilidad que ocurre en la base de datos de una aplicación. Para protegerse contra las inyecciones SQL, las entradas de información que el usuario introduce en la aplicación no deben ser directamente colocadas en sentencias SQL. En vez de eso, las entradas deben ser limipiadas o filtradas o bien se deben usar sentencias parametrizadas. Seleccionables (Selects) Areas de texto Timeout Timeout (QUERY_STRING) en Timeout viniendo de Timeout en A URLs URLs Scripts de subida Scripts de upload encontrados Wapiti-SVN (wapiti.sourceforge.net) XSS Ataque GET Ataque POST atacado por causado por viniendo de en  lswww explora un sitio web y extrae los enlaces y formularios (incluyendo sus campos).
 
 Usage: python lswww.py http://server.com/base/url/ [opciones]
 
 Las opciones soportadas son:
 -s <url>
 --start <url>
 	Para especificar una URL con la que empezar
 
 -x <url>
 --exclude <url>
 	Para excluir una URL del análisis (por ejemplo scripts de logout)
 	También se permite el uso del comodín (*)
 	Ejemplo: -x http://server/base/?page=*&module=test
 	o -x http://server/base/admin/* para excluir un directorio
 
 -p <url_proxy>
 --proxy <url_proxy>
 	Especifica un proxy
 	Ejemplo: -p http://proxy:port/
 
 -c <cookie_file>
 --cookie <cookie_file>
 	Para usar una cookie
 
 -a <login%password>
 --auth <login%password>
 	Establece credenciales para autenticación HTTP
 	No funciona con Python 2.4
 
 -r <parameter_name>
 --remove <parameter_name>
 	Borra un parámetro de las URL
 
 -v <level>
 --verbose <level>
 	Establece el nivel de logs
 	  0: only print results
 	  1: pinta un punto (.) por cada URL encontrada (logs por defecto)
 	  2: pinta cada URL
 
 -t <timeout>
 --timeout <timeout>
 	Establece el tiempo del timeout (en segundos)
 
 -n <limit>
 --nice <limit>
 	Define el límite de URL a leer con el mismo patrón
 	Usar esta opción para prevenir bucles infinitos
 	Este parámetro debe ser mayor de 0
 
 -h
 --help
 	Para sacar este mensaje de uso de Wapiti  Wapiti - Escáner de vulnerabilidades de aplicaciones web
 
 Uso: python wapiti.py http://server.com/base/url/ [opciones]
 
 Las opciones soportadas son:
 -s <url>
 --start <url>
 	Para especificar una URL con la que empezar
 
 -x <url>
 --exclude <url>
 	Para excluir una URL del análisis (por ejemplo scripts de logout)
 	También se permite el uso del comodín (*)
 	Ejemplo: -x http://server/base/?page=*&module=test
 	o -x http://server/base/admin/* para excluir un directorio
 
 -p <url_proxy>
 --proxy <url_proxy>
 	Especifica un proxy
 	Ejemplo: -p http://proxy:port/
 
 -c <cookie_file>
 --cookie <cookie_file>
 	Para usar una cookie
 
 -t <timeout>
 --timeout <timeout>
 	Establece el tiempo del timeout (en segundos)
 
 -a <login%password>
 --auth <login%password>
 	Establece credenciales para autenticación HTTP
 	No funciona con Python 2.4
 
 -r <parameter_name>
 --remove <parameter_name>
 	Borra un parámetro de las URL
 
 -n <limit>
 --nice <limit>
 	Define el límite de URL a leer con el mismo patrón
 	Usar esta opción para prevenir bucles infinitos
 	Este parámetro debe ser mayor de 0
 
 -m <module>
 --module <module>
 	Establece el uso de un conjunto de opciones de escaneo/ataque
 	GET_ALL: solo usa peticiones mediante GET (no POST)
 	GET_XSS: solo ataques XSS con el método HTTP GET
 	POST_XSS: solo ataques XSS con el método  HTTP POST
 
 -u
 --underline
 	Para resaltar en color los parámetros de las vulnerabilidades en la salida
 
 -v <level>
 --verbose <level>
 	Establece el nivel de logs por pantalla
 	0: silencioso (default), 1: pinta cada URL, 2: pinta cada ataque
 
 -f <type_file>
 --reportType <type_file>
 	Establece el tipo de informe
 	xml:  Informe en formato XML
 	html: Informe en formato HTML
 
 -o <output>
 --output <output_file>
 	Establece el nombre del informe
 	Si el tipo de informe seleccionado es HTML, este parámetro debe ser un directorio
 
 -h
 --help
 	Para sacar este mensaje de uso de Wapiti con con un navegador para ver el informe con campo con campos con parámetros 