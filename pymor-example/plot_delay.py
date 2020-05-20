import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as spla
import scipy.sparse as sps
import sys
import os
import time
from optparse import OptionParser

from pymor.basic import *
from pymor.models.iosys import LinearDelayModel
from pymor.reductors.interpolation import DelayBHIReductor, TFBHIReductor

sys.path.append(os.path.join("../"))
from src.base import plot2d

import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

if __name__ == '__main__':
    argvs = sys.argv
    parser = OptionParser()
    parser.add_option("--dir", dest="dir", default="./")
    opt, argc = parser.parse_args(argvs)
    print(opt, argc)

    obj = plot2d()

    p = InstationaryProblem(
        StationaryProblem(
            domain=LineDomain([0.,1.], left='robin', right='robin'),
            diffusion=ConstantFunction(1., 1),
            robin_data=(ConstantFunction(1., 1), ExpressionFunction('(x[...,0] < 1e-10) * 1.', 1)),
            outputs=(('l2_boundary', ExpressionFunction('(x[...,0] > (1 - 1e-10)) * 1.', 1)),)
        ),
        ConstantFunction(0., 1),
        T=3.
    )

    fom, _ = discretize_instationary_cg(p, diameter=1/100, nt=100)

    lti = fom.to_lti()

    tau = 1.
    g = 5.
    Atau = sps.coo_matrix(([g], ([0], [lti.order - 1])), (lti.order, lti.order)).tocsc()
    Atau = NumpyMatrixOperator(Atau, source_id=lti.solution_space.id, range_id=lti.solution_space.id)
    td_lti = LinearDelayModel(lti.A, (Atau,), (tau,), lti.B, lti.C, E=lti.E)
    print(td_lti)

    w = np.logspace(-1, 2.5, 500)
    td_lti.mag_plot(w, ax=obj.axs)
    obj.axs.set_title('Magnitude plot of the FOM')
    obj.SavePng()

    interp = TFBHIReductor(td_lti)

    r = 3
    sigma = np.logspace(0, 1, r)
    sigma = np.concatenate((1j * sigma, -1j * sigma))
    b = td_lti.input_space.ones(2 * r)
    c = td_lti.output_space.ones(2 * r)

    rom = interp.reduce(sigma, b, c)
    err_rom = td_lti - rom

    obj.new_2Dfig()
    td_lti.mag_plot(w, ax=obj.axs)
    rom.mag_plot(w, ax=obj.axs)
    obj.axs.set_title('Magnitude plot of the FOM and ROM')
    obj.SavePng_Serial()

    obj.new_2Dfig(aspect="auto")
    err_rom.mag_plot(w, ax=obj.axs)
    obj.axs.set_title('Magnitude plot of the error')
    obj.SavePng_Serial()

    delay_interp = DelayBHIReductor(td_lti)

    td_rom = delay_interp.reduce(sigma, b, c)
    err_td_rom = td_lti - td_rom

    obj.new_2Dfig()
    td_lti.mag_plot(w, ax=obj.axs)
    rom.mag_plot(w, ax=obj.axs)
    td_rom.mag_plot(w, ax=obj.axs)
    obj.axs.set_title('Magnitude plot of the FOM and ROMs')
    obj.SavePng_Serial()

    obj.new_2Dfig(aspect="auto")
    err_rom.mag_plot(w, ax=obj.axs, color='tab:orange')
    err_td_rom.mag_plot(w, ax=obj.axs, color='tab:green')
    obj.axs.set_title('Magnitude plot of the errors')
    obj.SavePng_Serial()

