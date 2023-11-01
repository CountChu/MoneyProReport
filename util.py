#
# FILENAME.
#       util.py - Utility Python Module.
#
# FUNCTIONAL DESCRIPTION.
#       The module provide common APIs for top modules.
#
# NOTICE.
#       Author: visualge@gmail.com (CountChu)
#       Created on 2023/10/15
#       Updated on 2023/11/1
#

import os

def get_latest_csv(dn):

    csv_ls = []
    for bn in os.listdir(dn):
        if os.path.splitext(bn)[1] != '.csv':
            continue 

        csv_ls.append(os.path.join(dn, bn))

    #
    # Read the newest csv.
    #

    csv_ls.sort()
    csv = csv_ls[-1]

    return csv