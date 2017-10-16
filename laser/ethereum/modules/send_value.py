from z3 import *
import re
import logging

def execute(svm):

    for node_addr in svm.send_eth_nodes:

        logging.info("Checking node at " + str(node_addr) )

        for paths in svm.paths[node_addr]:

            logging.info("Path " + str(paths) )

            s = Solver()

            for edge in paths:

                if (edge.condition is not None):

                    s.add(edge.condition)

            s.add(svm.env['caller'] == 0x1234)

            print(s)

            if (s.check() == sat):

                m = s.model()

                solution = str(m)
                # solution = re.sub("(\d+)",  lambda m: hex(int(m.group(1))), solution)
                # solution = re.sub("[0-9a-f]{32}[\],\)]*", "(...)", solution)

                logging.info(solution)

            else:

                logging.info("unsat")