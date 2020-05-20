#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pymor.analyticalproblems.domaindescriptions import RectDomain
from pymor.analyticalproblems.elliptic import StationaryProblem
from pymor.discretizers.builtin import discretize_stationary_cg
from pymor.analyticalproblems.functions import ExpressionFunction, LincombFunction
from pymor.parameters.functionals import ProjectionParameterFunctional, ExpressionParameterFunctional
from pymor.parameters.spaces import CubicParameterSpace
from time import sleep
from ipywidgets import interact, widgets


# In[ ]:


rhs = ExpressionFunction('(x[..., 0] - 0.5)**2 * 1000', 2, ())


# In[ ]:


problem = StationaryProblem(
        domain=RectDomain(),
        rhs=rhs,
        diffusion=LincombFunction(
            [ExpressionFunction('1 - x[..., 0]', 2, ()), ExpressionFunction('x[..., 0]', 2, ())],
            [ProjectionParameterFunctional('diffusionl', 0), ExpressionParameterFunctional('1', {})]
        ),
        parameter_space=CubicParameterSpace({'diffusionl': 0}, 0.01, 0.1),
        name='2DProblem'
    )


# In[ ]:


args = {'N': 100, 'samples': 10}
m, data = discretize_stationary_cg(problem, diameter=1. / args['N'])
U = m.solution_space.empty()
for mu in m.parameter_space.sample_uniformly(args['samples']):
    U.append(m.solve(mu))


# In[ ]:


Us = U * 1.5
plot = m.visualize((U, Us), title='Solution for diffusionl=0.5')

