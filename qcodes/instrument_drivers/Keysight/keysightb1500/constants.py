from enum import Enum, IntEnum, IntFlag
from typing import Set, Union


class StrEnum(str, Enum):
    pass


class InstrClass(StrEnum):
    SMU = 'SMU'
    CMU = 'CMU'


class SlotNr(IntEnum):
    ALL = 0
    MAINFRAME = 11
    SLOT01 = 1
    SLOT02 = 2
    SLOT03 = 3
    SLOT04 = 4
    SLOT05 = 5
    SLOT06 = 6
    SLOT07 = 7
    SLOT08 = 8
    SLOT09 = 9
    SLOT10 = 10


class ChNr(IntEnum):
    SLOT_01_CH1 = 1
    SLOT_02_CH1 = 2
    SLOT_03_CH1 = 3
    SLOT_04_CH1 = 4
    SLOT_05_CH1 = 5
    SLOT_06_CH1 = 6
    SLOT_07_CH1 = 7
    SLOT_08_CH1 = 8
    SLOT_09_CH1 = 9
    SLOT_10_CH1 = 10

    SLOT_01_CH2 = 102
    SLOT_02_CH2 = 202
    SLOT_03_CH2 = 302
    SLOT_04_CH2 = 402
    SLOT_05_CH2 = 502
    SLOT_06_CH2 = 602
    SLOT_07_CH2 = 702
    SLOT_08_CH2 = 802
    SLOT_09_CH2 = 902
    SLOT_10_CH2 = 1002


ChannelList = Set[Union[ChNr, int]]


class Abort(IntEnum):
    DISABLED = 1
    ENABLED = 2


class TriggerPort(IntEnum):
    EXT_TRIG_IN = -1
    EXT_TRIG_OUT = -2
    DIO_1 = 1
    DIO_2 = 2
    DIO_3 = 3
    DIO_4 = 4
    DIO_5 = 5
    DIO_6 = 6
    DIO_7 = 7
    DIO_8 = 8
    DIO_9 = 9
    DIO_10 = 10
    DIO_11 = 11
    DIO_12 = 12
    DIO_13 = 13
    DIO_14 = 14
    DIO_15 = 15
    DIO_16 = 16


class SweepMode(IntEnum):
    LINEAR = 1
    LOG = 2
    LINEAR_TWO_WAY = 3
    LOG_TWO_WAY = 4


class LinearSweepMode(IntEnum):
    LINEAR = 1
    LINEAR_TWO_WAY = 3


class APIVersion(IntEnum):
    B1500 = 0
    CLASSIC = 1


class VOutputRange(IntEnum):
    AUTO = 0

    MIN_0V2 = 2
    MIN_0V5 = 5
    MIN_2V = 20
    MIN_5V = 50
    MIN_20V = 200
    MIN_40V = 400
    MIN_100V = 1000
    MIN_200V = 2000
    MIN_500V = 5000
    MIN_1500V = 15000
    MIN_3000V = 30000
    MIN_10000V = 103


class VMeasRange(IntEnum):
    AUTO = 0

    MIN_0V2 = 2
    MIN_0V5 = 5
    MIN_2V = 20
    MIN_5V = 50
    MIN_20V = 200
    MIN_40V = 400
    MIN_100V = 1000
    MIN_200V = 2000
    MIN_500V = 5000
    MIN_1500V = 15000
    MIN_3000V = 30000
    MIN_10000V = 103

    FIX_0V2 = -2
    FIX_0V5 = -5
    FIX_2V = -20
    FIX_5V = -50
    FIX_20V = -200
    FIX_40V = -400
    FIX_100V = -1000
    FIX_200V = -2000
    FIX_500V = -5000
    FIX_1500V = -15000
    FIX_3000V = -30000
    FIX_10000V = -103


class IOutputRange(IntEnum):
    AUTO = 0

    MIN_1pA = 8
    MIN_10pA = 9
    MIN_100pA = 10
    MIN_1nA = 11
    MIN_10nA = 12
    MIN_100nA = 13
    MIN_1uA = 14
    MIN_10uA = 15
    MIN_100uA = 16
    MIN_1mA = 17
    MIN_10mA = 18
    MIN_100mA = 19
    MIN_1A = 20
    MIN_2A = 21
    MIN_20A = 22
    MIN_40A = 23

    FIX_500A = 26
    FIX_2000A = 28


class IMeasRange(IntEnum):
    AUTO = 0

    MIN_1pA = 8
    MIN_10pA = 9
    MIN_100pA = 10
    MIN_1nA = 11
    MIN_10nA = 12
    MIN_100nA = 13
    MIN_1uA = 14
    MIN_10uA = 15
    MIN_100uA = 16
    MIN_1mA = 17
    MIN_10mA = 18
    MIN_100mA = 19
    MIN_1A = 20
    MIN_2A = 21
    MIN_20A = 22
    MIN_40A = 23

    FIX_1pA = -8
    FIX_10pA = -9
    FIX_100pA = -10
    FIX_1nA = -11
    FIX_10nA = -12
    FIX_100nA = -13
    FIX_1uA = -14
    FIX_10uA = -15
    FIX_100uA = -16
    FIX_1mA = -17
    FIX_10mA = -18
    FIX_100mA = -19
    FIX_1A = -20
    FIX_2A = -21
    FIX_20A = -22
    FIX_40A = -23

    FIX_500A = -26
    FIX_2000A = -28


class RangingMode(IntEnum):
    AUTO = 0
    FIXED = 2


class CompliancePolarityMode(IntEnum):
    AUTO = 0
    MANUAL = 1


class LinearSearchMode(IntEnum):
    VALUE_LEQ_TARGET = 0
    VALUE_GEQ_TARGET = 1


class BinarySearchMode(IntEnum):
    LIMIT = 0
    REPEAT_COUNT = 1


class Polarity(IntEnum):
    NEGATIVE = 0
    POSITIVE = 1


class CalibrationType(IntEnum):
    OPEN = 1
    SHORT = 2
    LOAD = 3


class AutoPeriod(IntEnum):
    AUTO_EFFECTIVE_MINIMUM = 0
    AUTO_LONGEST = -1


# Command specific Enums

class AAD:
    class Type(IntEnum):
        HIGH_SPEED = 0
        HIGH_RESOLUTION = 1
        HIGH_SPEED_PULSED = 2


class ACT:
    class Mode(IntEnum):
        AUTO = 0
        PLC = 2


class ADJ:
    class Mode(IntEnum):
        AUTO = 0
        MANUAL = 1
        LOAD_ADAPTIVE = 2


class ADJQuery:
    class Mode(IntEnum):
        USE_LAST = 0
        MEASURE = 1


class AIT:
    class Type(IntEnum):
        HIGH_SPEED = 0
        HIGH_RESOLUTION = 1
        HIGH_SPEED_PULSED = 2

    class Mode(IntEnum):
        AUTO = 0
        MANUAL = 1
        LOAD_ADAPTIVE = 2
        MEAS_TIME_MODE = 3


class AITM:
    pass  # TODO remove
    # Mode = APIVersion


class AV:
    class Mode(IntEnum):
        AUTO = 0
        MANUAL = 1


class BDM:
    class Interval(IntEnum):
        SHORT = 0
        LONG = 1

    class Mode(IntEnum):
        VOLTAGE = 0
        CURRENT = 1


class BGI:
    pass  # TODO remove
    # SearchMode = BinarySearchMode


class BGV:
    pass  # TODO remove
    # SearchMode = BinarySearchMode


class BSM:
    class Mode(IntEnum):
        NORMAL = 0
        CAUTIOUS = 1

    # Abort = Abort # TODO remove

    class Post(IntEnum):
        START_VAL = 1
        STOP_VAL = 2
        OUTPUT_AT_SEARCH_TARGET = 3


class BSSI:
    pass  # TODO remove
    # Polarity = Polarity


class BSSV:
    pass  # TODO remove
    # Polarity = Polarity


class BSVM:
    class DataOutputMode(IntEnum):
        SEARCH = 0
        SEARCH_AND_SENSE = 1


class CLCORR:
    class Mode(IntEnum):
        CLEAR_ONLY = 1
        CLEAR_AND_SET_DEFAULT_FREQ = 2


class CMM:
    class Mode(IntEnum):
        COMPLIANCE_SIDE = 0
        FORCE_SIDE = 3
        CURRENT = 1
        VOLTAGE = 2
        CURRENT_AND_VOLTAGE = 4


class CORRQuery:
    pass  # TODO remove
    # Corr = CalibrationType


class CORRST:
    pass  # TODO remove
    # Corr = CalibrationType


class DCORR:
    pass  # TODO remove

    # Corr = CalibrationType

    class Mode(IntEnum):
        Cp_G = 100
        Ls_Rs = 400


class DI:
    pass  # TODO remove
    # CompPolarity = CompliancePolarityMode


class DIAG:
    class Item(IntEnum):
        TRIGGER_IO = 1
        HIGH_VOLTAGE_LED = 3
        DIGITAL_IO = 4
        INTERLOCK_OPEN = 6
        INTERLOCK_CLOSE = 7


class DV:
    pass  # TODO remove
    # CompPolarity = CompliancePolarityMode


class ERCMAGRD:
    class Guard(IntEnum):
        COMMON_AC = 1
        FLOATING = 2


class ERHPP:
    class Path(IntEnum):
        OPEN = 0
        HVSMU = 1
        HCSMU = 2
        HPSMU = 3
        HVSMU_WITH_R_SERIES = 4


class ERHPQG:
    class State(IntEnum):
        OPEN = 0
        GATE_CHARGE = 1
        IV = 2


class ERHVP:
    class State(IntEnum):
        OPEN = 0
        HVSMU = 1
        HVMCU = 2


class ERHVPV:
    class State(IntEnum):
        OPEN = 0
        HVMCU_DC = 1
        CAPACITANCE_CHARGE = 2


class ERMOD:
    class Mode(IntEnum):
        GENERAL_PURPOSE = 0
        SMU_PGU_SELECTOR_16440A = 1
        N1258A_N1259A = 2
        N1265A = 4
        N1266A = 8
        N1268A = 16
        N1272A = 32


class ERPFDP:
    class State(IntEnum):
        OPEN = 0
        UHCUL_AND_UHCUH = 1
        GNDU_AND_HVSMU_HVMCU = 2
        GNDU_AND_MP_HPSMU = 3
        GNDU_AND_OPEN = 4


class ERPFGP:
    class State(IntEnum):
        OPEN = 0
        CONNECTED = 1


class ERPFGR:
    class State:
        R_0 = 0
        R_10 = 10
        R_100 = 100
        R_1000 = 1000


class ERR:
    class Mode(IntEnum):
        READ_ALL = 0
        READ_ONE = 1


class ERRX:
    class Mode(IntEnum):
        CODE_AND_MESSAGE = 0
        CODE_ONLY = 1


class ERSSP:
    class Port(IntEnum):
        SELECTOR_1_OUT_1 = 0
        SELECTOR_1_OUT_2 = 1
        SELECTOR_2_OUT_1 = 2
        SELECTOR_2_OUT_2 = 3

    class Status(IntEnum):
        ALL_OPEN = 0
        SMU_ON = 1
        PGU_ON = 2
        PGU_OPEN = 3


class FMT:
    class Format(IntEnum):
        ASCII_12_DIGITS_WITH_HEADER_CRLF_EOI = 1
        ASCII_12_DIGITS_NO_HEADER_CRLF_EOI = 2
        BINARY_4_BYTE_CRLF_EOI = 3
        BINARY_4_BYTE_EOI = 4
        ASCII_12_DIGITS_WITH_HEADER_COMMA = 5
        ASCII_13_DIGITS_WITH_HEADER_CRLF_EOI = 11
        ASCII_13_DIGITS_NO_HEADER_CRLF_EOI = 12
        BINARY_8_BYTE_CRLF_EOI = 13
        BINARY_8_BYTE_EOI = 14
        ASCII_13_DIGITS_WITH_HEADER_COMMA = 15
        ASCII_13_DIGITS_WITH_HEADER_CRLF_EOI_4155_4156_COMPATIBLE = 21
        ASCII_13_DIGITS_NO_HEADER_CRLF_EOI_4155_4156_COMPATIBLE = 22
        ASCII_13_DIGITS_WITH_HEADER_COMMA_4155_4156_COMPATIBLE = 25

    class Mode(IntEnum):
        ONLY_MEASUREMENT_DATA = 0
        PRIMARY_SOURCE_OUTPUT_DATA = 1
        SYNCHRONOUS_SWEEP_SOURCE_OUTPUT_DATA = 2
        SWEEP_SOURCE_1 = 1
        SWEEP_SOURCE_2 = 2
        SWEEP_SOURCE_3 = 3
        SWEEP_SOURCE_4 = 4
        SWEEP_SOURCE_5 = 5
        SWEEP_SOURCE_6 = 6
        SWEEP_SOURCE_7 = 7
        SWEEP_SOURCE_8 = 8
        SWEEP_SOURCE_9 = 9
        SWEEP_SOURCE_10 = 10


class HVSMUOP:
    class SourceRange(IntEnum):
        SINGLE_CH = 1
        PLUSMINUS_1500V = 2
        PLUS_3000V = 3
        MINUS_3000V = 4


class IMP:
    class MeasurementMode(IntEnum):
        R_X = 1
        G_X = 2
        Z_THETA_RAD = 10
        Z_THETA_DEG = 11
        Y_THETA_RAD = 20
        Y_THETA_DEG = 21
        Cp_G = 100
        Cp_D = 101
        Cp_Q = 102
        Cp_Rp = 103
        Cs_Rs = 200
        Cs_D = 201
        Cs_Q = 202
        Lp_G = 300
        Lp_D = 301
        Lp_Q = 302
        Lp_Rp = 303
        Ls_Rs = 400
        Ls_D = 401
        Ls_Q = 402


class LGI:
    pass  # TODO remove
    # SearchMode = LinearSearchMode


class LGV:
    pass  # TODO remove
    # SearchMode = LinearSearchMode


class LIM:
    class Mode(IntEnum):
        VOLTAGE = 1
        CURRENT = 2


class LRN:
    class Type(IntEnum):
        OUTPUT_SWITCH = 0

        SLOT1_STATUS = 1
        SLOT2_STATUS = 2
        SLOT3_STATUS = 3
        SLOT4_STATUS = 4
        SLOT5_STATUS = 5
        SLOT6_STATUS = 6
        SLOT7_STATUS = 7
        SLOT8_STATUS = 8
        SLOT9_STATUS = 9
        SLOT10_STATUS = 10

        FILTER = 30

        TM_AV_CM_FMT_MM_SETTINGS = 31

        MEASUREMENT_RANGING_STATUS = 32

        STAIRCASE_SWEEP_MEASUREMENT_SETTINGS = 33

        PULSED_SOURCE_SETTINGS = 34

        QUASI_PULSED_SOURCE_SETTINGS = 37

        DIGITAL_IO_SETTINGS = 38

        CHANNEL_MAPPING = 40

        SMU_MEASUREMENT_OPERATION = 46

        SAMPLING_MEASUREMENT_SETTINGS = 47

        QUASI_STATIC_CV_MEASUREMENT_SETTINGS = 49

        LINEAR_SEARCH_MEASUREMENT_SETTINGS = 50

        BINARY_SEARCH_MEASUREMENT_SETTINGS = 51

        SMU_RESISTOR_STATUS = 53

        AUTOR_RANGING_MODE = 54

        ADC_SETTINGS = 55

        ADC_AVERAGING_INTEGRATION_TIME_SETTINGS = 56

        SOURCE_MEASURE_WAIT_TIME = 57

        TRIGGER_SETTINGS = 58

        MULTI_CHANNEL_SWEEP_SOURCE_SETTINGS = 59

        TIMESTAMP_SETTING = 60

        DISPLAY_SETTING = 61

        ASU_CONNECTION_PATH = 62

        PICOAMPERE_RANGING_MODE = 63

        ASU_CONNECTION_STATUS_INDICATOR = 64

        MFCMU_MEASUREMENT_MODE = 70

        MFCMU_DATA_OUTPUT_MODE = 71

        MFCMU_ADC_SETTING = 72

        MFCMU_MEASUREMENT_RANGE = 73

        SCUU_CONNECTION_STATUS_INDICATOR = 80

        SCUU_CONNECTION_PATH = 81

        MFCMU_ADJUSTMENT_MODE = 90

        CV_DC_BIAS_SWEEP_MEASUREMENT_SETTINGS = 100

        PULSED_SPOT_C_CV_MEASUREMENT_SETTINGS = 101

        C_F_SWEEP_MEASUREMENT_SETTINGS = 102

        CV_AC_LEVEL_SWEEP_MEASUREMENT_SETTINGS = 103

        C_T_SAMPLING_MEASUREMENT_SETTINGS = 104

        MULTI_CHANNEL_PULSED_SPOT_MEASUREMENT_SETTINGS = 105

        MULTI_CHANNEL_PULSED_SWEEP_MEASUREMENT_SETTINGS = 106

        PARALLEL_MEASUREMENT_MODE_SETTING = 110


# TODO remove
LSM = BSM  # TODO LSM has different parameters from BSM

LSSI = BSSI

LSSV = BSSV

LSVM = BSVM


class MCPNX:
    class Mode(IntEnum):
        VOLTAGE = 1
        CURRENT = 2


class MCPT:
    pass  # TODO remove
    # Period = AutoPeriod


class MCPWS:
    pass  # TODO remove
    # Mode = SweepMode


class MCPWNX:
    class Mode(IntEnum):
        VOLTAGE = 1
        CURRENT = 2


class ML:
    class Mode(IntEnum):
        LINEAR = 1
        LOG_10_PER_DECADE = 2
        LOG_25_PER_DECADE = 3
        LOG_50_PER_DECADE = 4
        LOG_100_PER_DECADE = 5
        LOG_250_PER_DECADE = 6
        LOG_500_PER_DECADE = 7


class MM:
    class Mode(IntEnum):
        SPOT = 1
        STAIRCASE_SWEEP = 2
        PULSED_SPOT = 3
        PULSED_SWEEP = 4
        STAIRCASE_SWEEP_WITH_PULSED_BIAS = 5
        QUASI_PULSED_SPOT = 9
        SAMPLING = 10
        QUASI_STATIC_CV = 13
        LINEAR_SEARCH = 14
        BINARY_SEARCH = 15
        MULTI_CHANNEL_SWEEP = 16
        SPOT_C = 17
        CV_DC_SWEEP = 18
        PULSED_SPOT_C = 19
        PULSED_SWEEP_CV = 20
        CF_SWEEP = 22
        CV_AC_SWEEP = 23
        CT_SAMPLING = 26
        MULTI_CHANNEL_PULSED_SPOT = 27
        MULTI_CHANNEL_PULSED_SWEEP = 28


class MSC:
    pass  # TODO remove

    # Abort = Abort

    class Post(IntEnum):
        BASE_VALUE = 1
        BIAS_VALUE = 2


class ODSW:
    class SwitchNormalState(IntEnum):
        NORMALLY_OPEN = 0
        NORMALLY_CLOSED = 1


class OSX:
    # Port = TriggerPort # TODO remove

    class Level(IntEnum):
        LOW = 0
        HIGH = 1
        EDGE = 2


class PAX:
    pass  # TODO remove
    # Port = TriggerPort


class PWDCV:
    pass  # TODO remove
    # Mode = LinearSweepMode


class PWI:
    pass  # TODO remove
    # Mode = SweepMode


class PWV:
    pass  # TODO remove
    # Mode = SweepMode


class QSC:
    pass  # TODO remove
    # Mode = APIVersion


class QSM:
    # Abort = Abort # TODO remove

    class Post(IntEnum):
        START = 1
        STOP = 2


class QSV:
    pass  # TODO remove
    # Mode = LinearSweepMode


class QSZ:
    class Mode(IntEnum):
        DISABLE = 0
        ENABLE = 1
        PERFORM_MEASUREMENT = 2


class RC:
    pass  # TODO remove
    # Mode = RangingMode


class RCV:
    pass  # TODO remove
    # Slot = SlotNr


class RM:
    class Mode(IntEnum):
        DEFAULT = 1
        AUTO_UP = 2
        AUTO_UP_DOWN = 3


class SAP:
    class Path(IntEnum):
        SMU = 0
        AUX = 1


class SIM:
    class Mode(IntEnum):
        PULSE_GEN = 0
        ARB_WAVE_GEN = 1


class SPM:
    class Mode(IntEnum):
        DC_VOLTAGE = 0
        TWO_LEVEL_PULSE_SOURCE_1 = 1
        TWO_LEVEL_PULSE_SOURCE_2 = 2
        THREE_LEVEL_PULSE_SOURCE_1_AND_2 = 3


class SPRM:
    class Mode(IntEnum):
        FREE_RUN = 0
        COUNT = 1
        DURATION = 2


class SPT:
    class Src(IntEnum):
        PULSE_SRC_1 = 1
        PULSE_SRC_2 = 2


class SPV:
    class Src(IntEnum):
        DC_BIAS_SRC = 0
        PULSE_SRC_1 = 1
        PULSE_SRC_2 = 2


class SRE(IntFlag):
    DATA_READY = 1
    WAIT = 2
    INTERLOCK_OPEN = 8
    SET_READY = 16
    ERROR = 32
    RQS = 64


class SSP:
    class Path(IntEnum):
        FORCE1SENSE1_OPEN = 1
        OPEN_FORCE2SENSE2 = 2
        FORCE1SENSE1_FORCE2SENSE2 = 3
        CMUH_CMUL = 4


# TODO remove
# STB = SRE  # bits of the status register have the same meaning as the status


# bit enable register.


class STGP:
    class TriggerTiming(IntEnum):
        DISABLE_TRIGGER = 0
        SYNC_TO_PG_PULSE_OR_START_OF_ALWG_SEQUENCE = 1
        ALWG_PATTERN_CHANGE_OR_START_OF_FIRST_PATTERN = 2
        START_OF_EVERY_ALWG_PATTERN = 3


class TC:
    pass  # TODO remove
    # Mode = RangingMode


class TDI:
    pass  # TODO remove
    # CompPolarity = CompliancePolarityMode


class TDV:
    pass  # TODO remove
    # CompPolarity = CompliancePolarityMode


class TGMO:
    class Mode(IntEnum):
        EDGE = 1
        GATE = 2


class TGP:
    # Port = TriggerPort # TODO remove

    class TerminalType(IntEnum):
        INPUT = 1
        OUTPUT = 2

    class Polarity(IntEnum):
        POSITIVE = 1
        NEGATIVE = 2

    class TriggerType(IntEnum):
        """
        The meaning of the Trigger Type value depends on the value of
        TerminalType
        """
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3


class TGSI:
    class Mode(IntEnum):
        CASE1 = 1
        CASE2 = 2


class TGSO:
    class Mode(IntEnum):
        EDGE = 1
        GATE = 2


class TGXO:
    class Mode(IntEnum):
        EDGE = 1
        GATE = 2


class TM:
    class Mode(IntEnum):
        XE_CMD_AND_GPIB_GET = 1
        XE_CMD = 2
        XE_CMD_AND_EXT_TRIGGER = 3
        XE_CMD_AND_MM_CMD = 4


class TMACV:
    # Mode = RangingMode # TODO remove

    class Range(StrEnum):
        MAX_0V016 = '0.016'
        MAX_0V032 = '0.032'
        MAX_0V064 = '0.064'
        MAX_0V125 = '0.125'
        MAX_0V250 = '0.250'


class TMDCV:
    # Mode = RangingMode # TODO remove

    class Range(IntEnum):
        MFCMU_8V = 8
        MFCMU_12V = 12
        MFCMU_25V = 25
        SMU_100V = 100


class TST:
    # Slot = SlotNr # TODO remove

    class Option(IntEnum):
        RETURN_PASS_FAIL = 0
        PERFORM_TEST_AND_RETURN_PASS_FAIL = 1


class TTC:
    # Mode = RangingMode # TODO remove

    class Range(IntEnum):
        MAX_100OHM = 50
        MAX_300OHM = 100
        MAX_1KOHM = 300
        MAX_3KOHM = 1000
        MAX_10KOHM = 3000
        MAX_30KOHM = 10000
        MAX_100KOHM = 30000
        MAX_300KOHM = 100000
        MAX = 300000


class UNT:
    class Mode(IntEnum):
        MODULE_INFO_ONLY = 0
        MODULE_AND_MAINFRAME_INFO = 1


class VAR:
    class Type(IntEnum):
        INTEGER = 0
        FLOAT = 1


class WACV:
    pass  # TODO remove
    # Mode = SweepMode


class WAT:
    class Type(IntEnum):
        SMU_SOURCE_WAIT_TIME = 1
        SMU_MEASURE_WAIT_TIME = 2
        MFCMU_MEASUREMENT_WAIT_TIME = 3


class WDCV:
    pass  # TODO remove
    # Mode = SweepMode


class WFC:
    pass  # TODO remove
    # Mode = SweepMode


class WI:
    pass  # TODO remove
    # Mode = SweepMode


class WM:
    # Abort = Abort # TODO remove

    class Post(IntEnum):
        START = 1
        STOP = 2


class WMACV:
    # Abort = Abort # TODO remove

    class Post(IntEnum):
        START = 1
        STOP = 2


class WMDCV:
    # Abort = Abort # TODO remove

    class Post(IntEnum):
        START = 1
        STOP = 2


class WMFC:
    # Abort = Abort # TODO remove

    class Post(IntEnum):
        START = 1
        STOP = 2


class WNX:
    class Mode(IntEnum):
        VOLTAGE = 1
        CURRENT = 2


class WS:
    class Mode(IntEnum):
        CONTINUE_IMMEDIATELY_IF_PENDING_TRIGGER = 1
        WAIT_IMMEDIATELY = 2


class WSX:
    class Mode(IntEnum):
        CONTINUE_IMMEDIATELY_IF_PENDING_TRIGGER = 1
        WAIT_IMMEDIATELY = 2


class WV:
    pass  # TODO remove
    # Mode = SweepMode
