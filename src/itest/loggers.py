import sys
import os
import logging as lg

def logger():
    def get_logger(level="info"):

        lg.basicConfig(
            format='[%(asctime)s : %(levelname)s : %(module)s: %(message)s]',


            level=lg.DEBUG if level=="debug" else lg.INFO ,


            handlers=[
                lg.FileHandler(os.path.join(os.getcwd(),"logs",'logs.log')),
                lg.StreamHandler(sys.stdout)
            ]
        )


        lgr=lg.getLogger("logger")

        return lgr

    return get_logger














