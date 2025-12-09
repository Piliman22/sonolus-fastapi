from pydantic import BaseModel
from typing import Optional, Dict, Any, List

from .items.background import BackgroundItem
from .items.skin import SkinItem
from .items.effect import EffectItem
from .items.particle import ParticleItem

class DbInfo(BaseModel):
    """
    packのinfoに相当するモデル
    """
    title: str
    
class PackModel(BaseModel):
    """
    パックモデル
    """
    info: DbInfo
    skins: List[SkinItem] = []
    backgrounds: List[BackgroundItem] = []
    effects: List[EffectItem] = []
    particles: List[ParticleItem] = []