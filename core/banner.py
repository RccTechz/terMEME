# coding=utf-8

green = "\033[92m"    
reset = "\033[0m"

def banner():
   """Display the terMEME banner.

   Returns:
      string: Returns the colored terMEME banner.
   """  
   
   return ("""%s

                     _            __  __ ______ __  __ ______ 
                    | |          |  \/  |  ____|  \/  |  ____|
                    | |_ ___ _ __| \  / | |__  | \  / | |__   
                    | __/ _ \ '__| |\/| |  __| | |\/| |  __|  
                    | ||  __/ |  | |  | | |____| |  | | |____ 
                     \__\___|_|  |_|  |_|______|_|  |_|______|
%s""" %(green, reset))
