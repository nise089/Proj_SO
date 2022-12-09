from enum import Enum


class CompanyTypesEnum(Enum):
    FOUNDATION_OWNED = "foundation-owned" # todo replace with company B
    INVESTOR_OWNED = "investor-owned" # todo replace with company A


class JobsEnum(Enum):
    OWNER = "owner"
    WORKER = "worker"
