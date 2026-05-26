import QuantLib as ql
import xloil as xlo

@xlo.func(
    help='Return the QuantLib version as a string.',
)
def qlVersion(Trigger = None):
    return ql.__version__

