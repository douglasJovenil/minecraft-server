from requests import get
from os.path import isfile, isdir
from os import system, listdir, remove, kill
from subprocess import Popen, PIPE
from shutil import rmtree
from zipfile import ZipFile
from time import sleep
from signal import SIGINT

def main():
  urlInstaller = 'https://files.minecraftforge.net/maven/net/minecraftforge/forge/1.16.3-34.1.0/forge-1.16.3-34.1.0-installer.jar'
  urlMod = 'https://ijaminecraft.com/download/map/IJAMinecrafts-OneBlock-1-16-3.zip?v=VERSION'

  modFilename = 'skyblock.zip'
  
  forgeInstallerFilename = 'forgeInstaller.jar'

  forgeApplicationFilename = getForgeApplicationFilename()
  forgeApplicationFileAlreadyExists = isfile(forgeApplicationFilename)

  if (not(forgeApplicationFileAlreadyExists)):
    print('Baixando instalador Forge...')
    # Faz o download do instalador
    response = get(urlInstaller)
    # Salva o instalador no computador
    with open(forgeInstallerFilename, 'wb') as f:
      f.write(response.content)

    print('Configurando o servidor Minecraft...')

    # Executa o instalador
    system(f'java -jar {forgeInstallerFilename} --installServer')
    # Apos a execucao do instalador, a aplicacao forge vai estar no computador
    forgeApplicationFileAlreadyExists = True

    # Cria o arquivo eula
    with open('eula.txt', 'w') as f: f.write('eula=true')

    print('Aguardando primeira inicialização do servidor...')
    process = Popen(f'java -jar {getForgeApplicationFilename()} nogui', shell=True)
    # Aguarda alguns arquivos serem criados para depois finalizar o processo
    while (not(isdir('world/serverconfig'))): pass
    system('pkill java')

    hasJavaProcess = True
    while (hasJavaProcess):
      pipe = Popen(['ps', '-ef'], stdout=PIPE)
      text = str(pipe.communicate()[0])
      if (text.count('java') == 0): hasJavaProcess = False

    # Configura o servidor
    with open('server.properties', 'r') as f:
      content = f.read()
      content = content.replace('online-mode=true', 'online-mode=false')
      content = content.replace('view-distance=10', 'view-distance=20')
    # Salva as configuracoes do servidor
    with open('server.properties', 'w') as f: f.write(content)

    # Baixa os mods
    print('Baixando mods...')
    response = get(urlMod)
    with open(modFilename, 'wb') as f: 
      f.write(response.content)

    rmtree('world')
    mod = ZipFile(modFilename)
    for file in mod.infolist():
      file.filename = f'world/{"/".join(file.filename.split("/")[1:])}'
      mod.extract(file)

    # Remove os arquivos de instalacao
    remove(forgeInstallerFilename)
    remove(f'{forgeInstallerFilename}.log')
    remove(modFilename)
  
  if (forgeApplicationFileAlreadyExists):
    print('Inicializando servidor...')
    system(f'java -jar {getForgeApplicationFilename()} nogui')
    
def getForgeApplicationFilename():
  filesAtDirectory = list(filter(lambda filename: 'forge-' in filename , listdir()))
  filename = filesAtDirectory[0] if len(filesAtDirectory) > 0 else ''
  return filename

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('Finalizando...')