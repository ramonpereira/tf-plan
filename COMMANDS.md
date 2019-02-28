### LQR 1D Navigation

```bash
python3.5 tfplan ../rddl/deterministic/lqr_1d_nav/lqr_1d_nav_instance-problem0.rddl -m offline -b 128 -hr 100 -e 1000 -lr 0.005 -v --viz=lqr_1d_nav

python3.5 tfplan ../rddl/deterministic/lqr_1d_nav/lqr_1d_nav_instance-problem1.rddl -m offline -b 128 -hr 100 -e 1000 -lr 0.005 -v --viz=lqr_1d_nav

python3.5 tfplan ../rddl/deterministic/lqr_1d_nav/lqr_1d_nav_instance-problem2.rddl -m offline -b 128 -hr 100 -e 1000 -lr 0.005 -v --viz=lqr_1d_nav
```


### LQR 2D Navigation

```bash
python3.5 tfplan ../rddl/deterministic/lqr_2d_nav_single_unit/lqr_2d_nav_single_unit-problem0.rddl -m offline -b 128 -hr 100 -e 1 -lr 0.005 -v --viz=lqr_2d_nav

python3.5 tfplan ../rddl/deterministic/lqr_2d_nav_single_unit/lqr_2d_nav_single_unit-problem1.rddl -m offline -b 128 -hr 100 -e 1 -lr 0.005 -v --viz=lqr_2d_nav

python3.5 tfplan ../rddl/deterministic/lqr_2d_nav_single_unit/lqr_2d_nav_single_unit-problem2.rddl -m offline -b 128 -hr 100 -e 1 -lr 0.005 -v --viz=lqr_2d_nav
```

### LQG 2D Navigation with Multi-Units

```bash
python3.5 tfplan ../rddl/deterministic/lqr_2d_nav_multi_unit/lqr_2d_nav_multi_unit-problem0.rddl -m offline -b 128 -hr 100 -e 1000 -lr 0.005 -v --viz=lqr_2d_multi_unit

python3.5 tfplan ../rddl/deterministic/lqr_2d_nav_multi_unit/lqr_2d_nav_multi_unit-problem1.rddl -m offline -b 128 -hr 100 -e 1000 -lr 0.005 -v --viz=lqr_2d_multi_unit

python3.5 tfplan ../rddl/deterministic/lqr_2d_nav_multi_unit/lqr_2d_nav_multi_unit-problem2.rddl -m offline -b 128 -hr 100 -e 1000 -lr 0.005 -v --viz=lqr_2d_multi_unit
```