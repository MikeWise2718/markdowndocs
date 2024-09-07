---
title: "Template Titles"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- curobo - https://curobo.org/
- Uses Pytorch and CUDA to massivley speed up robot inverse kinematics
- Uses optimization to solve constraints
- Uses two kinds of optimization particle based (MPPI) and `LBFGS`

# ik_example.py
- bare bones example of using `IKSolver`, but it is not really that bare bones
- Config files
   - robot config in `ur5e.yml`
   - other configs loaded in `IKSolver.load_from_robot_config`
     - `base_cfg_file: str = "base_cfg.yml",`
     - `particle_file: str = "particle_ik.yml"`
     - `gradient_file: str = "gradient_ik.yml"` (L-BFGS)

- Load from robot config
   - Creates a list of optimizers, basicaly two kinds
      - a particle optimizer that uses ES or MPPI
      - ES is a modified MPPI (child class)
      - a gradient optimizer that uses Gradient Descent or L-BFGS
    - Questions
        - how does `num_seeds` get used?

- Optimizer hierarch
    - abastract base clase is `OptimizerConfig`
    - Then comes `Optimizer` deriived from `OpitmizerConfig`
    - `NewtonOptConfig` derived from `OptimizerConfig`
    - `NewtonOptBase` derived from `Optimizer` and `NewtonOptConfig`
    - `LBFGSOptConfig` derived from `NewtonOptConfig`
    - `LBFGSOpt` derived from `NewtonOptBase`and `LBFGSOptConfig`
    - `ParticleOptConfig` derived from `OptimizerConfig`
    - `ParticleOptBase` dervied from  `Optimizer` and `ParticleOptConfig`
    - `ParallelMPPI` deriverd from `ParticleOptBase` and `ParllelMPPIConfig`
    - `ParallelESConfig` deriverd from `ParllelMPPIConfig`
    - `ParallelES` deriverd from `ParallelMPPI` and `ParllelESConfig`


- Optimizer Base class methods
  - `optimize`  - Find a solution through optimization given the initial values for variables
      - args opt_tensor (initial value), shift_steps, n_iters
  - `update_params` - Update parameters in the :meth:`curobo.rollout.rollout_base.RolloutBase` instance.
      - args goal (copied to _batch_gal)
  - `reset` - """Reset optimizer."""
  - `update_nproblems` - """Update the number of problems that need to be optimized.
  - `get_nproblem_testor` - """This function takes an input tensor of shape (n_problem,....) and converts it into  (n_particles,...).
  - `reset_seed` - """Reset seeds."""
  - `reset_cuda_graph`  - """Reset CUDA Graphs. This does not work, workaround is to create a new instance."""
  - `reset_shape` -    """Reset any flags in rollout class. Useful to reinitialize tensors for a new shape."""
  
  - `_optimize`  - """Implement this function in a derived class containing the solver.
    - abstract method
  - `_shift` -     """Shift the variables in the solver to hotstart the next timestep
     - abstract method
  - `_update_problem_kernel` - """Update matrix used to map problem index to number of particles.



- Optimal values selected in optiomizer `_update_distribution`
  - uses `torch.topk` and then `torch.index_select`