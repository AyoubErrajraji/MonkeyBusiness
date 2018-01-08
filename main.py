'''
Created on Nov 25, 2017
@author: lexdewilligen
'''

from menu_lib import slidemenu
from bananattack_lib import main as bananattack
#from escapetheguards_lib import etg as escapetheguards
from crosstheroad_lib import main as crosstheroad
from finalfight_lib import game as finalfight
from fightclub_lib import fightclub
from monkeywar_lib import monkeywar
from purchase_lib import purchase

debug = 6

if debug == 0:
    mymenu = slidemenu.run()
    mymenu.runm()
elif debug == 1:
    mygame = bananattack.main()
#elif debug == 2:
   # mymenu = escapetheguards.run()
    #mymenu.runm()
elif debug == 3:
    mymenu = crosstheroad.main()
elif debug == 4:
    mymenu = finalfight.run()
    mymenu.runm()
elif debug == 5:
    mymenu = fightclub.run()
    mymenu.runm()
elif debug == 6:
    mymenu = monkeywar.run()
    mymenu.runm()
elif debug == 7:
    mymenu = purchase.main()





