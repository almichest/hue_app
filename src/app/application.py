from app.hue_controller import HueController

def main():
    controller = HueController()
    controller.open()

if __name__ == '__main__':
   try:
       main()
   except:
       import traceback
       import sys
       traceback.print_exc()
       print ("ERROR")
       sys.exit(1)
