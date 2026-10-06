import numpy as np

x = np.array([1, 2, 3, 4], dtype=float)
y = np.array([5, 6, 7, 8], dtype=float)
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# ------------------------------------------------------------------------------
# 1. BASIC ARITHMETIC OPERATORS & CORRESPONDING UFUNCS
# ------------------------------------------------------------------------------
print("=== 1. BASIC ARITHMETIC ===")

# Addition (+) -> np.add
print("Add:", x + y)
print("Add (ufunc):", np.add(x, y))

# Subtraction (-) -> np.subtract
print("Subtract:", x - y)
print("Subtract (ufunc):", np.subtract(x, y))

# Multiplication (*) -> np.multiply
print("Multiply:", x * y)
print("Multiply (ufunc):", np.multiply(x, y))

# True Division (/) -> np.divide
print("Divide:", x / y)
print("Divide (ufunc):", np.divide(x, y))

# Floor Division (//) -> np.floor_divide
print("Floor Divide:", y // x)
print("Floor Divide (ufunc):", np.floor_divide(y, x))

# Modulus (%) -> np.mod or np.remainder
print("Modulus:", y % x)
print("Modulus (ufunc):", np.mod(y, x))

# Exponentiation (**) -> np.power
print("Power:", x ** 2)
print("Power (ufunc):", np.power(x, 2))

# Negative (-) -> np.negative
print("Negative:", -x)
print("Negative (ufunc):", np.negative(x))


# ------------------------------------------------------------------------------
# 2. MATRIX MULTIPLICATION & VECTOR PRODUCTS
# ------------------------------------------------------------------------------

# Matrix Product (@) -> np.matmul
print("Matrix Mult (@):\n", matrix_a @ matrix_b)
print("Matrix Mult (ufunc):\n", np.matmul(matrix_a, matrix_b))

# Dot Product -> np.dot (Inner product for vectors, matrix multiplication for 2D)
vec_a = np.array([1, 2, 3])
vec_b = np.array([4, 5, 6])
print("Vector Dot Product:", np.dot(vec_a, vec_b))   # formula : a.b = a[0]*b[0] + a[1]*b[1] + a[2]*b[2] ... + a[n-1]*b[n-1]

# Cross Product -> np.cross
print("Vector Cross Product:", np.cross(vec_a, vec_b)) # formula : a x b = (a[1]*b[2] - a[2]*b[1])i - (a[0]*b[2] - a[2]*b[0])j + (a[0]*b[1] - a[1]*b[0])k


# ------------------------------------------------------------------------------
# 3. TRIGONOMETRIC & HYPERBOLIC FUNCTIONS
# ------------------------------------------------------------------------------

angles = np.array([0, np.pi/2, np.pi])
print("Sin:", np.sin(angles))
print("Cos:", np.cos(angles))
print("Tan:", np.tan(angles))

# Inverse Trigonometric
vals = np.array([-1, 0, 1])
print("Arcsin (radians):", np.arcsin(vals))
print("Arccos (radians):", np.arccos(vals))
print("Arctan (radians):", np.arctan(vals))

# Conversion between Radians and Degrees
deg = np.array([0, 90, 180])
rad = np.radians(deg)
print("Degrees to Radians:", rad)
print("Radians to Degrees:", np.degrees(rad))

# Hyperbolic Functions
h_vals = np.array([0, 1.0])
print("Sinh:", np.sinh(h_vals))
print("Cosh:", np.cosh(h_vals))
print("Tanh:", np.tanh(h_vals))


# ------------------------------------------------------------------------------
# 4. EXPONENTS AND LOGARITHMS
# ------------------------------------------------------------------------------

# Natural Exponential (e^x)
print("Exp:", np.exp(x))

# Exponential minus 1 (e^x - 1, useful for small x accuracy)
print("Expm1:", np.expm1(x))

# Logarithms (Natural, Base-2, Base-10)
log_vals = np.array([1, np.e, 10, 100])
print("Natural Log (ln):", np.log(log_vals))
print("Base-2 Log (log2):", np.log2([1, 2, 4, 8]))
print("Base-10 Log (log10):", np.log10(log_vals))

# Log(1 + x) for precision with small numbers
print("Log1p:", np.log1p(0.00001))


# ------------------------------------------------------------------------------
# 5. ROUNDING, FLOATS, & MODIFICATION
# ------------------------------------------------------------------------------

float_arr = np.array([-1.7, -1.2, 0.2, 1.5, 1.7, 2.3])

# Round to given decimals
print("Round (decimals=0):", np.round(float_arr))

# Round to nearest integer
print("Rint (Round to nearest integer):", np.rint(float_arr))

# Floor (largest integer <= x) & Ceil (smallest integer >= x)
print("Floor:", np.floor(float_arr))
print("Ceil:", np.ceil(float_arr))

# Truncate (discard fractional part towards zero)
print("Truncate:", np.trunc(float_arr))


# ------------------------------------------------------------------------------
# 6. SUMS, PRODUCTS, DIFFERENCES & REDUCTIONS
# ------------------------------------------------------------------------------

matrix_c = np.array([[1, 2], [3, 4]])

# Sum and Product (Global vs Axis-specific)
print("Global Sum:", np.sum(matrix_c))
print("Sum along Columns (axis=0):", np.sum(matrix_c, axis=0))
print("Sum along Rows (axis=1):", np.sum(matrix_c, axis=1))

print("Global Product:", np.prod(matrix_c))

# Cumulative Operations
print("Cumulative Sum:", np.cumsum(x))
print("Cumulative Product:", np.cumprod(x))

# Differences (x[i+1] - x[i])
diff_arr = np.array([1, 3, 7, 12])
print("First Differences:", np.diff(diff_arr))


# ------------------------------------------------------------------------------
# 7. EXTREMA, ABSOLUTE, & LOGICAL MATHEMATICS
# ------------------------------------------------------------------------------

mixed_arr = np.array([-10, -5, 0, 5, 10])

# Absolute values
print("Absolute:", np.abs(mixed_arr))
print("Absolute (alias):", np.absolute(mixed_arr))

# Element-wise Maximum/Minimum between two arrays
arr_a = np.array([1, 5, 3])
arr_b = np.array([2, 4, 6])
print("Element-wise Max:", np.maximum(arr_a, arr_b))
print("Element-wise Min:", np.minimum(arr_a, arr_b))

# Value Clipping (Trimming extreme values to boundaries)
# Keeps values within [min, max] range
print("Clipped (Range 2 to 7):", np.clip(np.array([1, 3, 5, 8, 10]), 2, 7))


# ------------------------------------------------------------------------------
# 8. COMPLEX NUMBERS
# ------------------------------------------------------------------------------

complex_arr = np.array([1 + 2j, 3 - 4j])

print("Real component:", np.real(complex_arr))
print("Imaginary component:", np.imag(complex_arr))
print("Conjugate:", np.conj(complex_arr))
print("Complex Angle (radians):", np.angle(complex_arr))