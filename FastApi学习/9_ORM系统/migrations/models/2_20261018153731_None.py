from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `clas` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL COMMENT '班级名称'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `sno` INT NOT NULL COMMENT '学号',
    `pwd` VARCHAR(255) NOT NULL COMMENT '密码',
    `name` VARCHAR(255) NOT NULL COMMENT '姓名',
    `clas_id` INT NOT NULL,
    CONSTRAINT `fk_student_clas_4be9b492` FOREIGN KEY (`clas_id`) REFERENCES `clas` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `teacher` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL COMMENT '姓名',
    `tno` INT NOT NULL COMMENT '账号',
    `pwd` VARCHAR(255) NOT NULL COMMENT '密码'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `course` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL COMMENT '课程名',
    `teacher_id` INT NOT NULL COMMENT '课程讲师',
    CONSTRAINT `fk_course_teacher_2de38fe7` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student_course` (
    `student_id` INT NOT NULL,
    `course_id` INT NOT NULL,
    FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_student_cou_student_0d222b` (`student_id`, `course_id`)
) CHARACTER SET utf8mb4 COMMENT='学生选课表';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztWW1vmzAQ/isRnzapm8g72bc0a7Wuayo10TRpnZABh6AQOwWzNury32cbiA2BDJq+kC"
    "xf8nJ3NufnznePzaMyxxZ0/Y8DF/jKp9qjgsAc0h8J+UlNAYuFkDIBAYbLDc3YwvCJB0xC"
    "ZRPg+pCKLOibnrMgDkZUigLXZUJsUkMH2UIUIOcugDrBNiRT6FHFz19U7CALPkA//ruY6R"
    "MHulbCTcdiz+ZynSwXXHaByDk3ZE8zdBO7wRwJ48WSTDFaWzuIMKkNEfQAgWx64gXMfeZd"
    "tMp4RaGnwiR0URpjwQkIXCIt19CFTNH14fVYH52NdV0pAZCJEQOXuhoGyWYufGjUW92W1u"
    "y0NGrC3VxLuqvw0QKYcCCHZzhWVlwPCAgtOMYCVP69AetgCrxsXGP7FLLU5TSyMY7boI0F"
    "AluRT08HV7kNuk1o0U8IurdBu6Wy372JqhSDfA4edBcim0wZzu32FoC/928GX/o376jVez"
    "Y7ptsi3CvDSNUIdasVy+vJTAoCExjAnN0Dz9ITGhEenwQWZH5thOg0Gnl+eQNdwFe+GZZo"
    "Z4/CWaoTocLpv4rzL5ZG24+jiRs4D85N1bwxT0sAAjZfEns2e1JcCHHg+TCzRIaa7UVS2B"
    "zL5LFMVrpMasYE0tIIVCMsk29aIE+kJCYQmDTv9VLJnBz076SuDPSaYTRoAKCqFQzAM2T7"
    "RjvaAH8T+XPsQcdGl3DJA3BBnQLIzEr0qF6OxUwHAXxeO6JiD9yvi3EqEykuFA1IwprRHw"
    "36n8+UVX7737G3FWEPVwAtx5h9FozkDhTiJRoDjWPb6HRoHNv1yW3QU9VeHFlN6+weTb5q"
    "PdX9JQw8xrmgtbYIm34INPZ4mGZwKcUgSoV1ECNtOC5SkqmHA3sqjxJkIjOJqFxPt+nVVm"
    "4TryGD3EjLy2c3vmR0pDeHQm98hEugGllXvMGG9aHdnHRfr6nKFGZxn5Gp+YwxMq84YWwb"
    "Jiu6mlqvDFU8UGre7lnNipFydv1XjpFLI6pcLV61Dm8h3vH96o6sO77I3TNwi5JrKanejF"
    "nLfG83Yi2ulP5bXi0gSNPqxAEmyasTzDlNq5Oke3dezbHfTqzjo24GsZZOwfnEWjp0H4n1"
    "XhX0bcT6SE5e7caw1BGG7MURRrMaxyPMgR5hnvQ6MJd2lHkb+HTGsVd3si/6irAPPcecZj"
    "X7SLO11wNhc2z1h9Lqf0PPj/Zd0YIpDaly0SwO8cu3ebapSiAcmR8gunVVLYAutcpFl+tS"
    "NzwYkeh2P4nw19H1MOeKRwxJoWw5Jqn9qbmOXyFWVfY2IgtcBgabee77d66M6bur/o803I"
    "Nv16ccHOwT2+Oz8AlOy3GA529mq793pssj"
)
