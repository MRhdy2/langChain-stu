from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` ADD `addr` VARCHAR(255) NOT NULL COMMENT '教室' DEFAULT '';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` DROP COLUMN `addr`;"""


MODELS_STATE = (
    "eJztWltv4jgU/itVnmakmVVKCYR9o8xUc22lFq1W2o4iJzEharAZx9mCuvnvazsOdkLIkG"
    "FKA8MLpeccO/Z3bp8dnowZ9mEU/zH0ZyEy/jx7MhCYQfalqHhzZoD5XIm5gAI3EpZgZeLG"
    "lACPMuEERDFkIh/GHgnnNMR8dpREERdijxmGKFCiBIXfE+hQHEA6hYQp/vnGxCHy4QLG+b"
    "/zB2cSwsgvLDT0+bOF3KHLuZB9RPRKGPKnuY6Ho2SGlPF8SacYraxDRLk0gAgSQCGfnpKE"
    "L5+vTm4z31G2UmWSLVEb48MJSCKqbdd1lMxwnOubsXP3fuw4RgOAPIw4uGypsdh9wJfwtn"
    "Pe7Xfti17XZiZimStJP80erYDJBgp4rsdGKvSAgsxCYKxAXSwW66iOpoBUwyrNS7iyBZdx"
    "zVGsAzYXKGRVNO0D2hlYOBFEAZ1yPC2rBsi/hrejD8PbV8zqNX8kZuGfJcW1VHUyXZry+J"
    "08aGBzgQu8h0dAfGdNgzt4k+26ataZlSUAgUBgxzfJdyDzeRSBuCrPhbw2zb3c4pTlx5Ll"
    "4m+DNM/t25znxn3Sv4A++4Sgf59YXZN/H0xM40CyX7knpokP+brWXHQpR159voUREDtfd4"
    "vM7LtslvZ4aOvwT/P4y6Uy/dJnLZA4ITGsLJGZpr5IKptTmTyVyVaXSdudQFYagelmZfJF"
    "C+QbLYiB75MmeOf2+8PbMBqj3bOsAcPZBd3W4Ewh8Fh9cRoVjeKgHxeP1oS47bod5gBo2l"
    "s64BdUlbW2vwb+OvJXmMAwQJ/hUjjgI1sUQF5VQZF9aaxmOgrgN7V9JibgcdX0SpHIcGFo"
    "QJrViuHdaPjuvZE+2yFrG5b2FaDlGPPPLT25A1V7jgZs8HrV6zE/WueT+2RgmoPcs7bd29"
    "2bYtdOiWVpGBDObaG/ssjIVQY0JsJND3Cp+UCGwsqJUpuNk0o6JTgJpvooRdoqg4jJnTId"
    "Sms5ZL6HChKpbW8zi4w1oxONPBYaGSPcAFVp3fIGm9UH62LS319T1SnM/LEiUjczRWnecm"
    "JuuR4vurZ53hqqeKRHIGvgX7Ts8MOvWZsxcm1Em6vFXutwDfHO77F3ZN35hfmBgbstudaC"
    "6sWYtc73diPW6urut+XVCoIyrS4cYIq8usCcy7S6SLp359UC+3pinR91K4i1dgreTKy1Q/"
    "eJWB9UQa8j1idysrcbw0ZHGHoQRxjb75yOMEd6hPmp164baUeTt64/zzgO6k72WV/FDiEJ"
    "vWlVs5ea2l4PlM2p1R9Lq/8Xkljm3bYFUxvS5qL50r9PK7yAZUnVAGFpfoTonpvmFugyq4"
    "3oCl3phgcjKm/3iwh/uru53nDFo4aUUPZDj579dxaFcYtYVdPbiCpwORh85lkcf490TF99"
    "Hf5dhnv05eZSgINjGhAxi5jg8qV/eJn+DzUFeCI="
)
