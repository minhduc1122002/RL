REGISTRY = {}

from .basic_controller import BasicMAC
from .separate_controller import SeparateMAC
from .smmae_controller import SMMAEMAC

REGISTRY["basic_mac"] = BasicMAC
REGISTRY["separate_mac"]=SeparateMAC
REGISTRY["smmae_mac"] = SMMAEMAC