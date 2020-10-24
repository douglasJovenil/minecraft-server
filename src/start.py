from utils import getForgeApplicationFilename
from os import system

def main():
  print('Inicializando server')
  system(f'java -Xmx15360M -Xms1024M -jar {getForgeApplicationFilename()} nogui')

if __name__ == '__main__':
  main()