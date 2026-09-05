from .robot_kronos import RobotKronos
from .robot_auditor import RobotAuditor
from .robot_matrix import RobotMatrix

FABRICA = {
    "kronos": RobotKronos(),
    "auditor": RobotAuditor(),
    "matrix": RobotMatrix()
}
