from utils import getForgeApplicationFilename
from os import system

def main():
  print('Inicializando server')
  system(f'./run.sh')

if __name__ == '__main__':
  main()