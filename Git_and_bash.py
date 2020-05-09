# Status
git status
# acceder a carpeta
cd
#crear un archivo
touch script.py
#editores de texto
gedit about-me.md
nano about-me.md
#crear carpeta
mkdir yeaaa
#añadir todo
git add .
git add script.py
# cargar datos
git commit -m "upload 01.04.2020"
git commit -am "upload 01.04.2020" #realiza el add .
# subirlos
git push
git push origin name-branch
#para elimininar
git rm sript.py
git branch -d #borrar todo
#para volver atras en un commit
git reset HEAD script.py
git reset --hard 829283d892hdjsdh9wshdjka
#para acceder a los cambio, ''q'' para salir del Log
git log
git reflog
git log --graph --all
git diff
#crear un branch
git branch name-branch
#comprobar branchs
git branch
#cambiar a otra branch
git checkout name-branch #OJOOOO machaca directorio
git checkout -b name-branch
git checkout 24957fa28ee41a118573fdb80ccf57b
#poner bash por defecto en MAC
chsh -s /bin/bash
#BASH
#ayuda
man ls
ls --help
ls -a
ls -l
ls -lah
ls -lahr
ls -lahrt
ls -laht
ls -la #ver ocultos
./hola.txt #ejecutar
sudo chmod +x #permisos de ejecucion
#alias
nano .bashrc #modificar los alias para siempre
alias hola='ls -al'
alias #lista todos los alias
which python3 #que esta instalado
conda install python=3.7
#pasa saber donde andas
pwd
du -h -d  1 #saber tamaño carpetas
drwxrwxr-x #r lectura, w escritura, x ejecucion, composicion 1+3+3+3
#instalar
PYTHON3 NATIVO EN UBUNTU NUNCA HAY QUE USARLO
#conda
conda create -n test_env #desde el entorno base
conda activate test_env
conda env list
conda deactivate  =ORDEN CORRECTO
#intalar librerias
conda install -c conda-forge conda-pack
conda list
#necesita internet y conda
conda search libreria
conda remove -n test_env --all
conda env export
conda env create -f ruta/enviromente.yml
#sin internet ni conda
conda install -c conda-forge conda-pack
conda pack
scp test_env.tar.gz #pasar un archivo a otro por la red
tar xzfv test_env.tar.gz -C /test
source test_env/bin/activate
conda-unpack
#borrar
git rm -rf
snap install 
#week02
#ejecutar archivo
bash about-me.md
#visualizar
cat about-me.md
more about-me.md #empieza desde el principio
less about-me.md
tail about-me.md
tail -n 20 about-me.md #muestra ultimas 20 lineas
head about-me.md
#cambiar nombre
mv myfyle.txt myfile
mv myfyle.txt ./data/m1 #tambien mueve o corta, directorio y nuevo nombre
ls -la >> sed.txt
ls -la >> /desktop/sed.txt
-f #siempre en ejecucion
cp -r folder foldercopy #-r para copiar todo el contenio
cp ol* desktop/.
cp ol ../.
#borra
rm -rf 
conda install -c conda-forge jupyterlab jupyterhub nodejs nb_conda_kernels
conda install ipykernel














BASH Bbbbbbbbbbbbb
#Print Hello World in console.
printf "%s\n" "Hello World"
echo 'Hello World'
#Create a new folder named new_dir.
mkdir new_dir
#Delete new_dir folder.
rm -rf new_dir
#Make a copy of sed.txt (located in the lorem folder) to lorem-copy.
cp sed.txt ~/ir/dataptmad0420/extra-work/m1/lab-bash-master/lorem-copy
#Copy the rest of the files located in lorem to lorem-copy using only one code line (tip: use ;).
cp {at.txt,lorem.txt} ~/ir/dataptmad0420/extra-work/m1/lab-bash-master/lorem-copy
cp at.txt lorem.txt ~/ir/dataptmad0420/extra-work/m1/lab-bash-master/lorem-copy
#Locate at lorem folder and show sed.txt content.
cat sed.txt
#Locate at lorem folder and show at.txt and lorem.txt content.
cat at.txt lorem.txt
#Locate at lorem-copy folder and show the first three lines of sed.txt.
sed -n -e 1,3p sed.txt
#Locate at lorem-copy folder and show the last three lines of sed.txt.
tail -n 3 sed.txt
#Add Homo homini lupus. at the end of sed.txt located at lorem-copy.
echo " Homo homini lupus." >> sed.txt
#Locate at lorem-copy folder and show the last three lines of sed.txt. Now you should see Homo homini lupus..
tail -n 3 sed.txt
#Change every et to ET in at.txt located at lorem-copy (tip: use sed).
sed -i -e 's/et/ET/g' at.txt
#Find the active user of the system.
who
#Find out where are you located within the system.
pwd
#List all .txt files located at lorem.
ls -laht *.txt
#Count the number of lines in sed.txt located at lorem.
wc -l sed.txt
#Count the number of files which name starts with lorem located at the whole lab directory.
find -mindepth 1 -type f -name "lorem*" -printf x| wc -c
#Count the number of times et appears in at.txt located at lorem.
grep -o 'et' at.txt |wc -l
#Count the number of times the string et appears in at.txt located at lorem.
grep -o -w 'et' at.txt|wc -l
#Count the number of times the string et appears in every file located at lorem-copy.
grep -w -r -o 'et' |wc -l

#BONUS
#Load your name in the variable name.
name=Carlos_Pinero
#Print that variable.
printf "%s\n" $name
#Create a folder named after the variable name.
mkdir $name
#Delete that folder.
rm -rf $name
#For every folder in lorem print the total number of characters of every file name. Try using a for loop to show every file name.
grep  -r -o '.' | wc -l
#Print every file.
cat *
#Print the number of characters of every file name.
Number of characters of each file.
grep  -r -o '.' sed.txt | wc -l
grep  -r -o '.' lorem.txt | wc -l
grep  -r -o '.' at.txt | wc -l
Number of characters of every file.
grep  -r -o '.' | wc -l
Number of characters of every file name.
ls | grep -o '.'| wc -l
Number of characters of each file name
for x in *;do file=$(echo ''$x''); file=''${file%.*}''; echo ''${file}|grep -o '.'|wc -l ;done
#Print the number of characters of every file name with the following format: lorem has 5 characters lenght
for x in *;do file=$(echo ''$x''); file=''${file%.*}''; a=$(echo ''${file}|grep -o '.'|wc -l); echo ''${file} has ${a} characters lenght''; done
#Show the system processes being executels (show them hierarchically):
#Using top or htop commands.
sudo apt-get install htop
htop
#Using ps command with arguments.
ps -e
ps ax
#Show processor info on screen.
lscpu
#Create 3 new alias and make them available everytime you login your session.
nano .bashrc
alias ..='cd ..'
alias g='git status'
alias i1='cd  ir/dataptmad0420/module-1'
alias i2='cd  ir/dataptmad0420/module-2'
alias i3='cd  ir/dataptmad0420/module-3'
alias ie='cd  ir/dataptmad0420/extra-work'
alias ie1='cd  ir/dataptmad0420/extra-work/m1'
alias ie2='cd  ir/dataptmad0420/extra-work/m2'
alias ie3='cd  ir/dataptmad0420/extra-work/m3'
alias la='ls -laht'
#Compress lorem and lorem-copy folders in a file named lorem-compressed.tar.gz
tar -cvf lorem-compressed.tar.gz lorem lorem-copy
#Uncompress lorem-compressed.tar.gz in lorem-uncompressed folder.
mkdir lorem-uncompressed
tar -xvf lorem-compressed.tar.gz -C lorem-uncompressed
