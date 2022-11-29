# Simple Plotter
This tool is used to check the results of numerical calculations.

(Not for formal plotting.)

- Python 3 + Matplotlib

## Feature
- The first column is treated as the common `x` and the second and subsequent columns as separate plots.

## Supported Format
- The first line must be a comment line beginning with `#`.

- The first line is separated by spaces except `#`, and elements are treated as `xlabel`, `plot label 1`, `plot label 2`, ..., from left to right.

### Example
```
# x    y1    y2    y3    ...
  0    1.111    2.222    3.333
100    2.222    4.444    6.666
...
```

## Usage
- Plotting of `hoge.dat`

```
./plot.py hoge.dat
```
