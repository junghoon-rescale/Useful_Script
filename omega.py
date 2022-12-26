import sys
import math

rpm_str = sys.argv[1]
rpm = float(rpm_str)

def convert(rpm):
    
    rps = rpm/30.0*math.pi
    return rps

def main():

    rps = convert(rpm)
    print('RPM: ' + str(rpm) + '\t' + 'radian/sec: ' + str(format(rps, ".4f")))

if __name__=="__main__":
    main()
