import math


def Moment(Fy,Zx,Omega = 1.67):
    """
    Gets allowable bending moment(Ma) for a steel beam.

    Mn = (Fy*Zx)

    Ma = Mn/Omega

    Ma : Allowable bending moment,
    Fy : Yeild stress,
    Zx : Plastic section modulus about neutral axis,
    Omega: Factor of safety for bending moment(1.67),
    Mn : Nominal moment strength
    """
    Mn = (Fy*Zx)
    Ma = Mn/Omega
    return Ma

def MinimumZx(Ma, Fy, Omega = 1.67):
    """
    Get the minimum plastic section modulus (Zx) about neutral axis for a steel beam

    Zx = (Ma* Omega)/Fy

    Ma : Allowable bending moment,
    Fy : Yeild stress(,
    Zx : Plastic section modulus about neutral axis,
    Omega: Factor of safety for bending moment(1.67),
    Mn : Nominal moment strength
    """

    if Omega <= 1.0:
        raise ValueError('Omega must be greater than 1.0')

    Zx = (Ma* Omega)/Fy
    return Zx

def Shear(Fy, Aw, Omega = 1.5):
    """
    Get the allowable shear strength(Va) for a steel beam.

    Vn = 0.6*Fy*Aw

    Va = Vn/Omega

    Va : Allowable shear strength,
    Vn : Nominal shear,
    Fy : Yeild stress,
    Omega: Factor of safety for sheer(1.5)

    """

    Vn = 0.6*Fy*Aw
    Va = Vn/Omega

    return Va



