import random
import string


def mobile():
    mobile_begin_seed = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '157', '158', '159', '182',
                         '183', '187', '188', '130', '131', '132', '155', '156', '175', '185', '186', '133', '153',
                         '177', '180', '181', '189']
    mobile_seed = string.digits
    mobile = random.choice(mobile_begin_seed) + ''.join(random.choice(mobile_seed) for m in range(8))
    # print(mobile)
    return mobile


if __name__=="__main__":
    mobile()

