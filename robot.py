import wpilib
import wpilib.drive
import rev
import phoenix5

#elev = elevação

class TestRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.motor_left_front = rev.CANSparkMax(1, rev.CANSparkLowLevel.MotorType.kBrushless)
        self.motor_left_back = rev.CANSparkMax(2, rev.CANSparkLowLevel.MotorType.kBrushless)
        self.motor_right_front = phoenix5.WPI_TalonSRX(3)
        self.motor_right_back = phoenix5.WPI_TalonSRX(4)
        self.motor_elev = phoenix5.WPI_VictorSPX(5)

        
        self.motors_left = wpilib.MotorControllerGroup(self.motor_left_front, self.motor_left_back)
        self.motors_right = wpilib.MotorControllerGroup(self.motor_right_front, self.motor_right_back)
        self.motor_right.setInverted(True)
        
        self.joystick = wpilib.Joystick(0)
        
        self.drive = wpilib.drive.DifferentialDrive(self.motors_left, self.motors_right)

    def autonomousPeriodic(self) -> None:
         pass

    def teleopInit(self):
         self.drivetrain.setSafetyEnabled(True)


    def teleopPeriodic(self):
        self.drivetrain.arcadeDrive(-self.joystick.getRawAxis(1), self.joystick.getRawAxis(0), True)

        if self.joystick.getRawButton(1):
            self.motor_elev.set(1.0)
        else:
            self.motor_elev.set(0.0)