import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time
from optparse import OptionParser

from pymor.domaindescriptions.basic import LineDomain, RectDomain, TorusDomain, CircleDomain
from pymor.analyticalproblems.elliptic import StationaryProblem
from pymor.discretizers.cg import discretize_instationary_cg, discretize_stationary_cg
from pymor.functions.basic import ConstantFunction, LincombFunction, ExpressionFunction
from pymor.parameters.functionals import ProjectionParameterFunctional, ExpressionParameterFunctional
from pymor.parameters.spaces import CubicParameterSpace
from time import sleep
from ipywidgets import interact, widgets

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

    rhs = ExpressionFunction('(x[..., 0] - 0.5)**2 * 1000', 2, ())

    problem = StationaryProblem(
        domain=RectDomain(),
        rhs=rhs,
        diffusion=LincombFunction(
            [ExpressionFunction('1 - x[..., 0]', 2, ()),
             ExpressionFunction('x[..., 0]', 2, ())],
            [ProjectionParameterFunctional(
                'diffusionl', 0), ExpressionParameterFunctional('1', {})]
        ),
        parameter_space=CubicParameterSpace({'diffusionl': 0}, 0.01, 0.1),
        name='2DProblem'
    )

    args = {'N': 100, 'samples': 10}
    m, data = discretize_stationary_cg(problem, diameter=1. / args['N'])
    U = m.solution_space.empty()
    for mu in m.parameter_space.sample_uniformly(args['samples']):
        U.append(m.solve(mu))

    Us = U * 1.5
    plot = m.visualize((U, Us), title='Solution for diffusionl=0.5')
