# Drivebase parameters. None of these should ever be changed by users

# All constents will be defined here
TIRE_DIAMETER = 56  # mm
AXLE_TRACK = 103  # distance between the wheels, mm

# Max/min Drivebase parameters (absolute values)
# The maximum number that can be used for speed is 977, but there is no speed
# difference above 600
DB_MAX_SPEED_MMSEC = 600

# The drivebase can accept speeds down to zero, but is not very efficient and
# quite erratic. Realistically, 30 is a good minimum speed
DB_MIN_SPEED_MMSEC = 30

# The max acceleration number that can be entered is 9775, but realistically
# there is no difference above 500, so we are going to use that as the max
DB_MAX_ACCEL_MMSEC2 = 500

# Lowest usable accelleration, determined by testing
DB_MIN_ACCEL_MMSEC2 = 5

# Max and min turning speeds, determined by testing
# These have not been validated yet!!!!
DB_MAX_TURN_RATE_DEGSEC = 360
DB_MIN_TURN_RATE_DEGSEC = 20
DB_MAX_TURN_ACCEL_DEGSEC2 = 1200
DB_MIN_TURN_ACCEL_DEGSEC2 = 10

# Not sure how these are used
DB_MAX_TORQUE_MNM = 1000  # milli-newton-meters
DB_MIN_TORQUE_MNM = 1000

# Large Motor usable parameters
LG_MOT_MAX_VOLTAGE = 9000  # mV
LG_MOT_MIN_VOLTAGE = 3000  # mV
LG_MOT_MAX_TORQUE = 560

# Medium Motor usable parameters
MED_MOT_MAX_SPEED_DEGSEC = 1100
MED_MOT_MAX_ACCEL_DEGSEC2 = 20000
MED_MOT_MIN_ACCEL_DEGSEC2 = 50
MED_MOT_MIN_SPEED_DEGSEC = 100
MED_MOT_MAX_TORQUE = 1000
MED_MOT_MIN_TORQUE = 600


def Rescale(val, in_min, in_max, out_min, out_max):
    if val == 0:
        return 0
    neg = val / abs(val)  # will either be 1 or -1
    val = abs(val)
    if in_max == in_min:
        return 0
    if val < in_min:
        val = in_min
    if val > in_max:
        val = in_max
    retVal = out_min + (val - in_min) * (
        (out_max - out_min) / (in_max - in_min)
    )
    if retVal > out_max:
        retVal = out_max
    if retVal < out_min:
        retVal = out_min
    return retVal * neg


def RescaleStraightSpeed(speedPct):
    return Rescale(
        speedPct,
        1,
        100,
        DB_MIN_SPEED_MMSEC,
        DB_MAX_SPEED_MMSEC,
    )


def RescaleStraightAccel(accelPct):
    return Rescale(
        accelPct,
        1,
        100,
        DB_MIN_ACCEL_MMSEC2,
        DB_MAX_ACCEL_MMSEC2,
    )


def RescaleTurnSpeed(turnSpeedPct):
    return Rescale(
        turnSpeedPct,
        1,
        100,
        DB_MIN_TURN_RATE_DEGSEC,
        DB_MAX_TURN_RATE_DEGSEC,
    )


def RescaleTurnAccel(turnAccelPct):
    return Rescale(
        turnAccelPct,
        1,
        100,
        DB_MIN_TURN_ACCEL_DEGSEC2,
        DB_MAX_TURN_ACCEL_DEGSEC2,
    )


def RescaleMedMotSpeed(medMotSpeedPct):
    return Rescale(
        medMotSpeedPct,
        1,
        100,
        MED_MOT_MIN_SPEED_DEGSEC,
        MED_MOT_MAX_SPEED_DEGSEC,
    )


def RescaleMedMotAccel(medMotAccelPct):
    return Rescale(
        medMotAccelPct,
        1,
        100,
        MED_MOT_MIN_ACCEL_DEGSEC2,
        MED_MOT_MAX_ACCEL_DEGSEC2,
    )


def RescaleMedMotTorque(medMotTorquePct):
    return Rescale(
        medMotTorquePct,
        1,
        100,
        MED_MOT_MIN_TORQUE,
        MED_MOT_MAX_TORQUE,
    )
