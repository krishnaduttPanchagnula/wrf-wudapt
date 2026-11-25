# Quality bar — do not lower these

These are the specific failures from the original thesis that this rebuild must not repeat.

1. **No causal claim from a correlational fit.** Proposal effects come from counterfactual WRF runs
   (perturbed land surface / urban parameters), never from perturbing one input of a regression
   fitted to the baseline run.
2. **LCZ must enter the physics**, not just the post-processing. Urban parameters in WRF come from
   the LCZ map (height, density, albedo, imperviousness, anthropogenic heat), with provenance recorded.
3. **Independent validation.** Compare against station observations, not an interpolated gridded
   product that shares ancestry with the model. Report bias, RMSE and MAE; keep a held-out period.
4. **No circular predictors.** Do not select features by correlation with the target from the same
   simulation, and do not use variables that are algebraic/diagnostic functions of the target.
5. **Defined skill metric.** If an ML emulator is used: RMSE/MAE/R² on blocked (by time and by LCZ)
   hold-outs, prediction intervals, and monotonicity checks. "Accuracy" alone is not a result.
6. **No extrapolation beyond training support.** Scenario values outside the training range are
   either rejected or handled by the physics model, not by a nearest-neighbour clamp.
7. **Reproducibility.** Every input has a URL, retrieval date, license and checksum; namelists,
   environment and random seeds are committed.
8. **Internal consistency.** Narrative conclusions must be checked against the tables that support
   them (the thesis claimed 20% LAI cooling > 30% while its Appendix B shows the opposite).
9. **Verify interventions bite.** Before reporting a counterfactual result, check that the
   perturbed field is actually read by the model. Perturbing `LAI` in `wrfinput` changed nothing
   (Noah re-derives it); `SMOIS` did. A zero-effect perturbation is a failed experiment, not a result.

Shortcuts are allowed only with a comment of the form
`shortcut: <limitation>, <when to upgrade>`.
