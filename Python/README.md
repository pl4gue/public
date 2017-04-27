# Python :ghost: :ghost: :ghost: 
Codigos en python



# Comandos
    # DESCARGAR ZIP
    >>>   curl -L -o master.zip http://github.com/zoul/Finch/zipball/master
    # DESCARGAR REPO
    >>>   git clone git@github.com:pabloag4/Python.git
    >>>   git add .  #(en ./Python )
    >>>   git commit -m "Comentario"
    >>>   git push   
  
  

# Entorno
    # Clave Pública
    >>>   //Crear clave
    >>>   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
                >>>   enter
                >>>   pass/pass
    >>>   //Iniciar agent segundo plano
    >>>   eval "$(ssh-agent -s)"
    >>>   //Añadir tu clave al ssh-Agent
    >>>   ssh-add ~/.ssh/id_rsa
    >>>   //Copiar en portapapeles la clave publica (~/.ssh/id_rsa.pub)
    >>>   //Dentro de GitHub :  Settings >> SSH and GPG >> Add New
    >>>   //Probar conexion
    >>>   ssh -T git@github.com
    
    
    
    
![image](command.png)
