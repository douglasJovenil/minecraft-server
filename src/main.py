from requests import get
from os.path import isfile
from os import system, listdir, remove
from subprocess import Popen
from shutil import move

def main():
  urlInstaller = 'https://files.minecraftforge.net/maven/net/minecraftforge/forge/1.16.3-34.1.0/forge-1.16.3-34.1.0-installer.jar'
  urlMod = 'https://media.forgecdn.net/files/3014/251/stoneBlock-1.0.37.zip'

  modFilename = 'stoneblock.zip'
  
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

    # Roda o servidor forge para criar o arquivo server.properties
    process = Popen(f'java -jar {getForgeApplicationFilename()} nogui')

    # Aguarda o arquivo server.properties ser criado
    while (not(isfile('server.properties'))): pass
    # Aguarda o arquivo server.properties ser escrito
    with open('server.properties', 'r') as f: 
      while(len(f.read()) == 0): pass
    # Para o servidor
    process.kill()

    # Configura o servidor
    with open('server.properties', 'r') as f:
      content = f.read()
      content = content.replace('online-mode=true', 'online-mode=false')
      content = content.replace('view-distance=10', 'view-distance=20')
    # Salva as configuracoes do servidor
    with open('server.properties', 'w') as f: f.write(content)

    # Remove os arquivos de instalacao
    remove(forgeInstallerFilename)
    remove(f'{forgeInstallerFilename}.log')

    # Baixa os mods
    print('Baixando mods...')
    response = get(urlMod)
    with open(modFilename, 'wb') as f: 
      f.write(response.content)
    move(modFilename, './mods')

  
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