from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `admin` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `xxx` VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `admin`;"""


MODELS_STATE = (
    "eJztWl1v2jAU/StVnjqpmwItEPZGWat1XanUomnSOkVOYkJEsGnirKAu/32242ATQkbKWg"
    "LjhdJ7rx373K9jh2dtjB3ohx86zthD2sejZw2BMaRfFhUnRxqYTKSYCQiwfG4J5iZWSAJg"
    "EyocAD+EVOTA0A68CfEwmx1Fvs+E2KaGHnKlKELeYwRNgl1IhjCgih8/qdhDDpzCMP13Mj"
    "IHHvSdhYV6Dns2l5tkNuGyK0QuuSF7mmXa2I/GSBpPZmSI0dzaQ4RJXYhgAAhk05MgYstn"
    "qxPbTHeUrFSaJEtUxjhwACKfKNu1TCnTTLN32zfvL/qmqZUAyMaIgUuXGvLdu2wJ7+u1s9"
    "aZcdo8M6gJX+Zc0oqTR0tgkoEcnl5fi7keEJBYcIwlqNPpdBnV7hAE+bAK8wyudMFZXFMU"
    "i4BNBRJZGU1vAe0YTE0fIpcMGZ6NRgGQ3zp33c+du2Nq9Y49EtPwT5KiJ1T1RBfHLH4HIw"
    "VsJrCAPXoCgWMuaXAdr7JdVo3r46wEIOBy7Ngm2Q5EPnd9EOblOZcXprmdWhyyfF+ynP8t"
    "keapfZXzXHuIWqfQoZ8QtB6ixpnOvrcHurYj2S/dE5LIgWxdSy46FyMvr++gD/jOl90iMv"
    "s+maU6Hlo7/OM0/lKpSL/4VQskjoIQ5pbIRFNcJKXNoUweymSly6RhDSAtjUC3kjK51QJ5"
    "ogQxgcCmcW+WCubFQX8P6spAb1hWnToA6saaDvgH0b7UjpbAX0b+EgfQc9E1nHEHXNFFAW"
    "TnBbqol305014Av6odUXEAnubFOBOJFBeKBiRJzejcdzufLrT41cj/OuzhBqBZH7PPNT25"
    "AYV4jcZA/diwmk3qx0Zt8BC1db2detYwmpt7k+/azHR/BYOAcS7ozC2Spp8AjQPuphGcKT"
    "4QoTB3otAm44SSDAMcuUN1lCQTuUFE5Wa2TceF3CbdQw65Uba3mt2EitGB3uwLvQkRLoGq"
    "sK54g03qQ+N00Hq7pqpSmMlTTqSuZozCvOKEsWHZrOgaeq0yVHFPqXmj7ZxWjJSz679yjF"
    "wZUeVq8aZ1uIB4p/erG7Lu9CJ3x8Bdl1wrQbU1Zq3yvc2ItbxS+m95tYQgS6sXDjCLvHqB"
    "OWdp9SLp3pxXc+yLiXV61M0h1sopeDWxVg7dB2K9UwW9iFgfyMmb3RiWOsKQnTjCGE79cI"
    "TZ0yPMi14HrqQdZd4Gvpxx7NSd7Ku+IuzAwLOHec1eaAp7PZA2h1a/L63+FwxCkXfrFkxl"
    "SJWL5rZ/N6W2JJZUJRAW5nuIbk3X10CXWq1El+syNzwYEXG7v4jwl/vb3oorHjkkg7Lj2e"
    "To95HvhRViVWVvI/LAZWCwmcdh+OirmB7fdL5n4e5+vT3n4OCQuAGfhU9wvu0fBMZ/APld"
    "CIU="
)
