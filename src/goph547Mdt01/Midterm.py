# GOPH 547 - Midterm Exam W2026
# Parts:
# I  :  Multiple Choice
# II  :  Vector Operations and Curvilinear Coordinates
# III :  Gravitational Flux and Equivalent Surface Density
# IV  :  Theoretical Gravity in a Rotating Frame

import numpy as np

# Provided constants for the calculation.
G = 6.67430e-11           # Gravitational constant [m^3 kg^-1 s^-2]
M_EARTH = 5.972e24        # Mass of Earth [kg]
A_EQUATOR = 6378137       # Radius of the equator [m]
FLATTENING = 1 / 298.257  # Earth flattening
OMEGA_EARTH = 7.292115e-5 # Rate of rotation of the earth [rad/s]

# FUNCTIONS
def vector_magnitude(v):
    """Compute magnitude of a vector"""
    return np.sqrt(np.sum(v**2))


def gravitational_field_cartesian(M, position):
    """
    Gravitational field in Cartesian coordinates:
    g = -GM * r / |r|^3
    Derived from g = -∇U, where U = -GM/r
    """
    r = vector_magnitude(position)
    return -G * M * position / r**3


def spherical_angles(position):
    """
    Convert Cartesian coordinates to spherical angles
    θ = latitude, φ = longitude
    """
    x, y, z = position
    r = vector_magnitude(position)
    theta = np.arcsin(z / r)
    phi = np.arctan2(y, x)
    return theta, phi


def theta_unit_vector(position):
    """
    Unit vector in latitudinal (theta) direction:
    i_theta = [-sinθ cosφ, -sinθ sinφ, cosθ]
    Derived from ∂r_hat / ∂θ
    """
    theta, phi = spherical_angles(position)
    sin_t = np.sin(theta)
    cos_t = np.cos(theta)
    cos_p = np.cos(phi)
    sin_p = np.sin(phi)
    return np.array([-sin_t * cos_p, -sin_t * sin_p, cos_t])


# PART I - Multiple Choice Answers

def part_i_answers():
    answers = {
        1: "b) There is a net influx",
        2: "a and d",
        3: "a, b, and c",
        4: "a and b",
        5: "b, c, and d",
        6: "d) A direction in the xz-plane",
        7: "d",
        8: "a and c",
        9: "-GMx/r³",
        10: "b and d"
    }

    print("\nPART I - Multiple Choice Answers")
    for q, ans in answers.items():
        print(f"Q{q:02d}: {ans}")
    return answers

# WRITTEN RESPONSES AND CALCULATIONS
# PART II - Vector Operations and Curvilinear Coordinates

def part_ii_solution():
    print("\nPART II - VECTOR OPERATIONS AND CURVILLINEAR COORDINATES")

    M = 8.681e25
    position = np.array([55e6, 55e6, 32.5e6])
    r = vector_magnitude(position)

    # Gravitational field components
    g = gravitational_field_cartesian(M, position)
    g_mag = vector_magnitude(g)
    g_r = -G * M / r**2

    # Gravitational flux through a spherical surface
    flux = -4 * np.pi * G * M

    # Latitudinal unit vector
    theta_hat = theta_unit_vector(position)

    # Print results with explanations
    print("Observation Position (m):", position)
    print("Distance from origin r (m):", f"{r:.3e}")
    print("\nGravitational field components (m/s^2):")
    print("gx =", g[0])
    print("gy =", g[1])
    print("gz =", g[2])
    print("\nMagnitude of gravity ||g|| =", g_mag)
    print("Radial component g_r along r-hat =", g_r)
    print("\nTotal gravitational flux through enclosing surface Φ =", flux)
    print("Unit vector in latitudinal direction θ-hat =", theta_hat)
    print("\nExplanation:")
    print("1. Gravity g = -∇U with U = -GM/r.")
    print("2. Radial component g_r = magnitude along r-hat.")
    print("3. Flux Φ = -4πGM (Gauss's Law).")
    print("4. θ-hat points north along latitude direction.")

    return {"g": g, "g_mag": g_mag, "g_r": g_r, "flux": flux, "theta_hat": theta_hat}

# PART III - Gravitational Flux and Equivalent Surface Density

def part_iii_solution():
    print("\nPART III - GRAVITATIONAL FLUX & EQUIVALENT SURFACE DENSITY")

    # Mass anomalies
    m1, m2, m3 = 8.54e5, 3.26e6, 5.21e6
    r = 270  # Radius of hemispherical surface

    # Total mass
    M_enc = m1 + m2 + m3

    # Flux through surface
    flux = -4 * np.pi * G * M_enc

    # Equivalent surface density σ* = M_enc / surface area (hemisphere + base)
    area = 3 * np.pi * r**2
    sigma_star = M_enc / area

    # Print results with explanations
    print("Total enclosed mass M_enc =", M_enc)
    print("Gravitational flux Φ =", flux)
    print("Equivalent surface density σ* =", sigma_star)
    print("\nExplanation:")
    print("1. Flux depends only on total mass enclosed (Gauss's Law).")
    print("2. Equivalent surface density = average mass per unit area producing the same flux.")
    print("3. Surface area includes hemisphere + flat base: S = 3πr^2.")

    return {"M_enc": M_enc, "flux": flux, "rho_star": sigma_star}


# PART IV - Theoretical Gravity in a Rotating Frame
def part_iv_solution():
    print("\nPART IV - THEORETICAL GRAVITY / ROTATING FRAME")

    latitude_deg = 25.05
    latitude = np.radians(latitude_deg)
    rotation_period = 23.93 * 3600
    omega = 2 * np.pi / rotation_period
    sin2 = np.sin(latitude)**2

    # Radius at latitude
    r_theta = A_EQUATOR * (1 - FLATTENING * sin2)
    GM = G * M_EARTH

    # Gravitational and centrifugal components
    g_grav = GM / r_theta**2
    centrifugal = omega**2 * r_theta * np.cos(latitude)**2
    g_theoretical = g_grav - centrifugal

    # International Gravity Formula
    g_IGF = 9.780318 * (1 + 0.0053024 * sin2 - 0.0000058 * np.sin(2 * latitude)**2)

    print("Radius at latitude r(θ) =", r_theta)
    print("Gravitational term GM/r^2 =", g_grav)
    print("Centrifugal term ω^2 r cos^2θ =", centrifugal)
    print("\nEffective theoretical gravity =", g_theoretical)
    print("IGF empirical gravity =", g_IGF)
    print("Difference IGF - theoretical =", g_IGF - g_theoretical)
    print("\nExplanation:")
    print("1. Effective gravity includes gravitational and centrifugal terms.")
    print("2. Radius accounts for Earth's flattening: r(θ) = a_e (1 - f sin^2θ).")
    print("3. IGF is empirical, including real shape and mass distribution.")
    print("4. Difference arises because theoretical model assumes perfect ellipsoid and uniform density.")

    return {"g_theoretical": g_theoretical, "g_IGF": g_IGF, "difference": g_IGF - g_theoretical}

# RUN DRIVER FUNCTIONS ABOVE
def main():
    print("\nGOPH 547 MIDTERM SOLUTIONS\n")

    part_i_answers()
    ii = part_ii_solution()
    iii = part_iii_solution()
    iv = part_iv_solution()

    print("\nSummary of Key Values")
    print("Part II |g| =", ii["g_mag"])
    print("Part III Flux =", iii["flux"])
    print("Part IV g =", iv["g_theoretical"])


if __name__ == "__main__":
    main()