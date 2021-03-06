#
# @BEGIN LICENSE
#
# Psi4: an open-source quantum chemistry software package
#
# Copyright (c) 2007-2017 The Psi4 Developers.
#
# The copyrights for code used from other parties are included in
# the corresponding files.
#
# This file is part of Psi4.
#
# Psi4 is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3.
#
# Psi4 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with Psi4; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# @END LICENSE
#
"""
List of hybrid functionals
"""

import copy

funcs = []

funcs.append({
    "name": "B5050LYP",
    "x_functionals": {
        "LDA_X": {
            "alpha": 0.08
        },
        "GGA_X_B88": {
            "alpha": 0.42
        }
    },
    "x_hf": {
        "alpha": 0.50
    },
    "c_functionals": {
        "LDA_C_VWN": {
            "alpha": 0.19
        },
        "GGA_C_LYP": {
            "alpha": 0.81
        }
    },
    "description": '    B5050LYP Hyb-GGA Exchange-Correlation Functional\n',
    "citation": '    Y. Shao et. al., J. Chem. Phys., 188, 4807-4818, 2003\n',
})

funcs.append({
    "name": "wPBE0",
    "alias": ["LC-WPBE0"],
    "x_functionals": {
        "GGA_X_HJS_PBE": {
            "omega": 0.3,
            "alpha": 0.75
        }
    },
    "x_hf": {
        "alpha": 0.25,
        "beta": 1.0,
        "omega": 0.3
    },
    "c_functionals": {
        "GGA_C_PBE": {}
    },
    "description":
    '    PBE0 SR-XC Functional (HJS Model)\n',
    "citation":
    '    Henderson et. al., J. Chem. Phys., 128, 194105, 2008\n' + \
    '    Weintraub, Henderson, and Scuseria, J. Chem. Theory. Comput., 5, 754, 2009\n',
})

funcs.append({
    "name": "wPBE",
    "alias": ["LC-WPBE", "LCWPBE"],
    "x_functionals": {
        "GGA_X_HJS_PBE": {
            "omega": 0.4
        }
    },
    "x_hf": {
        "alpha": 0.0,
        "beta": 1.0,
        "omega": 0.4
    },
    "c_functionals": {
        "GGA_C_PBE": {}
    },
    "description":
    '    PBE SR-XC Functional (HJS Model)\n',
    "citation":
    '    Henderson et. al., J. Chem. Phys., 128, 194105, 2008\n' + \
    '    Weintraub, Henderson, and Scuseria, J. Chem. Theory. Comput., 5, 754, 2009\n',
})

# funcs.append({
#     "name": "wB97X-D3",
#     "alias": ["WB97X-D3ZERO"],
#     "x_functionals": {
#         "HYB_GGA_XC_WB97X": {
#             "omega": 0.25,
#             "tweaks": [0.804272, 0.698900, 0.508940, -3.744903, 10.060790,
#                        1.000000, 2.433266, -15.446008, 17.644390, -8.879494,
#                        1.000000, -4.868902, 21.295726, -36.020866, 19.177018]
#         }
#     },
#     "x_hf": {
#         "alpha": 0.195728,
#         "beta": 1.0,
#         "omega": 0.25
#     },
#     "c_functionals": {},
#     "dispersion": {
#         "type": "d3zero",
#         "params": {
#             's6': 1.0,
#             's8': 1.000,
#             'sr6': 1.281,
#             'sr8': 1.094,
#             'alpha6': 14.0
#         }
#     },
#     "description":
#     '    This functional is currently broken - wB97X needs enabled tweaks.\n',
#     "citation":
#     '    Y.-S. Lin, G.-D. Li, S.-P. Mao, J.-D. Chai, J. Chem. Theory Comput., 9, 263-272, 2013\n',
# })

funcs.append({
    "name": "HF",
    "alias": ["SCF"],
    "x_hf": {
        "alpha": 1.0
    },
    "c_functionals": {},
})

funcs.append({
    "name": "HF+D",
    "x_hf": {
        "alpha": 1.0
    },
    "c_functionals": {},
    "dispersion": {
        "type": "das2010",
        "params": {
            "s6": 1.0
        }
    }
})

funcs.append({
    "name": "HF-3c",
    "alias": ["HF3C"],
    "x_hf": {
        "alpha": 1.0
    },
    "c_functionals": {},
    "dispersion": {
        "type": "d3bj",
        "params": {
            's6': 1.000,
            's8': 0.8777,
            'a1': 0.4171,
            'a2': 2.9149
        }
    },
    "description": '    Hartree Fock based 3C composite method with minimal basis set, gCP and D3(BJ)\n',
    "citation": '    Sure et al., J. Comput. Chem., 34, 1672-1685, 2013\n',
})

funcs.append({
    "name": "PBEh-3c",
    "alias": ["PBEH3C"],
    "x_functionals": {
        "GGA_X_PBE": {
            "tweak": [1.0245, 0.12345679],
            "alpha": 0.58
        }
    },
    "x_hf": {
        "alpha": 0.42
    },
    "c_functionals": {
        "GGA_C_PBE": {
            "tweak": [0.03]
        }
    },
    "dispersion": {
        "type": "d3bj",
        "params": {
            's6': 1.000,
            's8': 0.0000,
            'a1': 0.4860,
            'a2': 4.5000
        }
    },
    "description": '    PBE Hybrid based 3C composite method with a small basis set, gCP and D3(BJ)\n',
    "citation": '    Grimme et. al., J. Chem. Phys., 143, 054107, 2015\n',
})

funcs.append({
    "name": "SOGGA11-X",
    "alias": ["SOGGA11X"],
    "x_functionals": {
        "HYB_GGA_X_SOGGA11_X": {
            "use_libxc": True
        }
    },
    "c_functionals": {
        "GGA_C_SOGGA11_X": {}
    },
    "description": '   SOGGA11-X Hybrid Exchange-Correlation Functional\n',
    "citation": '    R. Peverati and D. G. Truhlar, J. Chem. Phys. 135, 191102, 2011\n',
})

funcs.append({
    "name": "MN12-SX",
    "alias": ["MN12SX"],
    "x_functionals": {
        "HYB_MGGA_X_MN12_SX": {
            "use_libxc": True
        }
    },
    "c_functionals": {
        "MGGA_C_MN12_SX": {}
    },
    "description": '   MN12-SX Meta-GGA Hybrid Screened Exchange-Correlation Functional\n',
    "citation": '    R. Peverati, D. G. Truhlar, Phys. Chem. Chem. Phys 14, 16187, 2012\n',
})

funcs.append({
    "name": "MN15",
    "x_functionals": {
        "HYB_MGGA_X_MN15": {
            "use_libxc": True
        }
    },
    "c_functionals": {
        "MGGA_C_MN15": {}
    },
    "description": '   MN15 Hybrid Meta-GGA Exchange-Correlation Functional\n',
    "citation": '    H. S. Yu, X. He, S. L. Li, and D. G. Truhlar, Chem. Sci. 7, 5032-5051, 2016\n',
})

funcs.append({
    "name": "N12-SX",
    "alias": ["N12SX"],
    "x_functionals": {
        "HYB_GGA_X_N12_SX": {
            "use_libxc": True
        }
    },
    "c_functionals": {
        "GGA_C_N12_SX": {}
    },
    "description": '   N12-SX Hybrid nonseparable GGA Exchange-Correlation Functional\n',
    "citation": '    R. Peverati, D.G. Truhlar, Phys. Chem. Chem. Phys. 14, 16187, 2012\n',
})

funcs.append({
    "name": "PBE50",
    "x_functionals": {
        "GGA_X_PBE": {
            "alpha": 0.5
        }
    },
    "x_hf": {
        "alpha": 0.5
    },
    "c_functionals": {
        "GGA_C_PBE": {}
    },
    "description": '   PBE50 Hybrid GGA Exchange-Correlation Functional\n',
})

funcs.append({
    "name": "revPBE0",
    "x_functionals": {
        "GGA_X_PBE_R": {
            "alpha": 0.75
        }
    },
    "x_hf": {
        "alpha": 0.25
    },
    "c_functionals": {
        "GGA_C_PBE": {}
    },
    "description": '   revPBE0 Hybrid GGA Exchange-Correlation Functional\n',
})

funcs.append({
    "name": "mPW1LYP",
    "x_functionals": {
        "GGA_X_MPW91": {
            "alpha": 0.75
        }
    },
    "x_hf": {
        "alpha": 0.25
    },
    "c_functionals": {
        "GGA_C_LYP": {}
    },
    "description": '   mPW1LYP Hybrid GGA Exchange-Correlation Functional\n',
})

funcs.append({
    "name": "mPW1PBE",
    "x_functionals": {
        "GGA_X_MPW91": {
            "alpha": 0.75
        }
    },
    "x_hf": {
        "alpha": 0.25
    },
    "c_functionals": {
        "GGA_C_PBE": {}
    },
    "description": '   mPW1PBE Hybrid GGA Exchange-Correlation Functional\n',
})

funcs.append({
    "name": "MGGA_MS2h",
    "alias": ["MGGA-MS2H", "MS2H"],
    "x_functionals": {
        "HYB_MGGA_X_MS2H": {
            "use_libxc": True
        }
    },
    "c_functionals": {
        "GGA_C_REGTPSS": {}
    },
    "description": '   MGGA_MS2h Hybrid Meta-GGA XC Functional\n',
    "citation": '    J. Sun, et al., J. Chem. Phys. 138, 044113, 2013\n',
})

funcs.append({
    "name": "MGGA_MVSh",
    "alias": ["MGGA-MVSH", "MVSH"],
    "x_functionals": {
        "HYB_MGGA_X_MVSH": {
            "use_libxc": True
        }
    },
    "c_functionals": {
        "GGA_C_REGTPSS": {}
    },
    "description": '   MGGA_MV2h Hybrid Meta-GGA XC Functional\n',
    "citation": '    J. Sun, J.P. Perdew, A. Ruzsinsky, Proc. Natl. Acad. Sci. USA 112, 685, 2015\n',
})


def get_pw6b95_tweaks():
    beta = 0.0018903811666999256  # 5.0*(36.0*math.pi)**(-5.0/3.0)
    X2S = 0.1282782438530421943003109254455883701296
    X_FACTOR_C = 0.9305257363491000250020102180716672510262  #    /* 3/8*cur(3/pi)*4^(2/3) */
    bt = 0.00538  # paper values
    c_pw = 1.7382  # paper values
    expo_pw6 = 3.8901  # paperl values
    alpha_pw6 = c_pw / X2S / X2S
    a_pw6 = 6.0 * bt / X2S
    b_pw6 = 1.0 / X2S
    c_pw6 = bt / (X_FACTOR_C * X2S * X2S)
    d_pw6 = -(bt - beta) / (X_FACTOR_C * X2S * X2S)
    f_pw6 = 1.0e-6 / (X_FACTOR_C * X2S**expo_pw6)
    return ([a_pw6, b_pw6, c_pw6, d_pw6, f_pw6, alpha_pw6, expo_pw6])


funcs.append({
    "name": "PW6B95",
    "x_functionals": {
        "GGA_X_PW91": {
            "tweak": get_pw6b95_tweaks(),
            "alpha": 0.72
        }
    },
    "x_hf": {
        "alpha": 0.28
    },
    "c_functionals": {
        "MGGA_C_BC95": {
            "tweak": [0.03668, 0.00262]
        }
    },
    "description": '    PW6B95 Hybrid Meta-GGA XC Functional\n',
    "citation": '  Y. Zhao and D. Truhlar, J. Phys. Chem. A., 109,5656-5667, 2005\n',
})

funcs.append({
    "name": "dlDF",
    "x_functionals": {
        "HYB_MGGA_X_DLDF": {
            "use_libxc": True
        }
    },
    "c_functionals": {
        "MGGA_C_DLDF": {}
    },
    "description": '    Dispersionless Hybrid Meta-GGA XC Functional\n',
    "citation": '    Pernal et. al., Phys. Rev. Lett., 103, 263201, 2009\n',
})

funcs.append({
    "name": "dlDF+D09",
    "alias": ["DLDF-D09", "DLDF-DAS2009"],
    "x_functionals": {
        "HYB_MGGA_X_DLDF": {
            "use_libxc": True
        }
    },
    "c_functionals": {
        "MGGA_C_DLDF": {}
    },
    "dispersion": {
        "type": "das2009",
        "params": {
            "s6": 1.0
        }
    },
    "description": '    Dispersionless Hybrid Meta-GGA XC Functional\n',
    "citation": '    Pernal et. al., Phys. Rev. Lett., 103, 263201, 2009\n',
})

funcs.append({
    "name": "dlDF+D10",
    "alias": ["DLDF-D10", "DLDF-DAS2010", "DLDF+D"],
    "x_functionals": {
        "HYB_MGGA_X_DLDF": {
            "use_libxc": True
        }
    },
    "c_functionals": {
        "MGGA_C_DLDF": {}
    },
    "dispersion": {
        "type": "das2010",
        "params": {
            "s6": 1.0
        }
    },
    "description": '    Dispersionless Hybrid Meta-GGA XC Functional\n',
    "citation": '    Pernal et. al., Phys. Rev. Lett., 103, 263201, 2009\n',
})

functional_list = {}
for functional in funcs:
    functional_list[functional["name"].upper()] = functional
