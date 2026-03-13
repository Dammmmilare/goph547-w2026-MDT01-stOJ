"""
GOPH 547 - Midterm Exam Solutions (Improved Version)
Course: Gravity Theory I

Parts
------
I   Multiple Choice
II  Vector Operations and Curvilinear Coordinates
III Gravitational Flux and Equivalent Surface Density
IV  Theoretical Gravity in a Rotating Frame
"""

import numpy as np

# provided constants for the calculation.

G = 6.67430e-11           # Gravitational constant [m^3 kg^-1 s^-2]
M_EARTH = 5.972e24        # Mass of Earth [kg]
A_EQUATOR = 6378137       # Radius of the equator [m]
FLATTENING = 1 / 298.257  # Earth flattening
OMEGA_EARTH = 7.292115e-5 # Rate of rotation of the earth [rad/s]


# Driver Functions to support our calculations.

def vector_magnitude(v):
    return np.sqrt(np.sum(v**2))


def gravitational_field_cartesian(M, position):
    """
    g = -GM r / |r|^3
    """
    r = vector_magnitude(position)
    return -G * M * position / r**3


def spherical_angles(position):
    """
    Returns latitude (θ) and longitude (φ)
    """
    x, y, z = position
    r = vector_magnitude(position)

    theta = np.arcsin(z / r)
    phi = np.arctan2(y, x)

    return theta, phi


def theta_unit_vector(position):
    """
    Unit vector in latitudinal direction
    """
    theta, phi = spherical_angles(position)

    sin_t = np.sin(theta)
    cos_t = np.cos(theta)

    cos_p = np.cos(phi)
    sin_p = np.sin(phi)

    return np.array([
        -sin_t * cos_p,
        -sin_t * sin_p,
        cos_t
    ])


# ============================================================
# PART I — MULTIPLE CHOICE
# ============================================================

def part_i_answers():

    answers = {
        1: "b) There is a net influx",
        2: "a and d",
        3: "a, b, and c",
        4: "a and b",
        5: "b, c, and d",
        6: "d) A direction in the xz-plane",
        7: "d",
        8: "a",
        9: "-GMx/r³",
        10: "b and d"
    }

    print("\nPART I - MULTIPLE CHOICE\n")

    for q, ans in answers.items():
        print(f"Q{q:02d}: {ans}")

    return answers


# ============================================================
# PART II — VECTOR OPERATIONS
# ============================================================

def part_ii_solution():

    print("\nPART II - VECTOR OPERATIONS\n")

    M = 8.681e25
    position = np.array([55e6, 55e6, 32.5e6])

    r = vector_magnitude(position)

    # gravitational field
    g = gravitational_field_cartesian(M, position)

    g_mag = vector_magnitude(g)

    g_r = -G * M / r**2

    # flux through sphere
    flux = -4 * np.pi * G * M

    # theta unit vector
    theta_hat = theta_unit_vector(position)

    print("Position (m):", position)
    print("Distance r:", f"{r:.3e}")

    print("\nGravity Components (m/s^2)")
    print("gx =", g[0])
    print("gy =", g[1])
    print("gz =", g[2])

    print("\n|g| =", g_mag)
    print("Radial component =", g_r)

    print("\nTotal Flux =", flux)

    print("\nθ-hat =", theta_hat)

    return {
        "g": g,
        "g_mag": g_mag,
        "g_r": g_r,
        "flux": flux,
        "theta_hat": theta_hat
    }


# ============================================================
# PART III — GRAVITATIONAL FLUX
# ============================================================

def part_iii_solution():

    print("\nPART III - GRAVITATIONAL FLUX\n")

    m1 = 8.54e5
    m2 = 3.26e6
    m3 = 5.21e6

    r = 270

    M_enc = m1 + m2 + m3

    flux = -4 * np.pi * G * M_enc

    area = 3 * np.pi * r**2

    rho_star = M_enc / area

    print("Total Mass =", M_enc)
    print("Flux =", flux)
    print("Equivalent Surface Density =", rho_star)

    return {
        "M_enc": M_enc,
        "flux": flux,
        "rho_star": rho_star
    }


# ============================================================
# PART IV — THEORETICAL GRAVITY
# ============================================================

def part_iv_solution():

    print("\nPART IV - THEORETICAL GRAVITY\n")

    latitude_deg = 25.05
    latitude = np.radians(latitude_deg)

    rotation_period = 23.93 * 3600

    omega = 2 * np.pi / rotation_period

    sin2 = np.sin(latitude)**2

    r_theta = A_EQUATOR * (1 - FLATTENING * sin2)

    GM = G * M_EARTH

    g_grav = GM / r_theta**2

    centrifugal = omega**2 * r_theta * np.cos(latitude)**2

    g_theoretical = g_grav - centrifugal

    # International Gravity Formula
    g_IGF = 9.780318 * (
        1
        + 0.0053024 * sin2
        - 0.0000058 * np.sin(2 * latitude)**2
    )

    print("Radius =", r_theta)
    print("Gravitational term =", g_grav)
    print("Centrifugal term =", centrifugal)

    print("\nTheoretical gravity =", g_theoretical)
    print("IGF gravity =", g_IGF)

    print("Difference =", g_IGF - g_theoretical)

    return {
        "g_theoretical": g_theoretical,
        "g_IGF": g_IGF,
        "difference": g_IGF - g_theoretical
    }


# ============================================================
# MAIN
# ============================================================

def main():

    print("\nGOPH 547 MIDTERM SOLUTIONS\n")

    part_i_answers()

    ii = part_ii_solution()

    iii = part_iii_solution()

    iv = part_iv_solution()

    print("\nSUMMARY\n")

    print("Part II |g| =", ii["g_mag"])
    print("Part III Flux =", iii["flux"])
    print("Part IV g =", iv["g_theoretical"])


if __name__ == "__main__":
    main()