from enum import Enum


class CompanyTypesEnum(Enum):
    FOUNDATION_OWNED = "foundation-owned"
    INVESTOR_OWNED = "investor-owned"


class JobsEnum(Enum):
    OWNER = "owner"
    WORKER = "worker"
