# -*- coding: utf-8 -*-

"""
Copyright (C) 2021 Mitchell Isaac Parker <mitch.isaac.parker@gmail.com>

This file is part of the rascore project.

The rascore project can not be copied, edited, and/or distributed without the express
permission of Mitchell Isaac Parker <mitch.isaac.parker@gmail.com>.
"""

from .col import (
    bio_lig_col,
    ion_lig_col,
    pharm_lig_col,
    chem_lig_col,
    mod_lig_col,
    mem_lig_col,
)

bio_lst = ["GNP", "GDP", "GTP", "GSP", "GCP", "ATP", "DBG", "AGN", "9GM", "CAG"]
ion_lst = [
    "CO",
    "MG",
    "MN",
    "FE",
    "CU",
    "ZN",
    "FE1",
    "FE2",
    "FE3",
    "FE4",
    "RH",
    "RH1",
]

pharm_lst = [
    "2PG",
    "PII",
    "33Y",
    "TPP",
    "IMP",
    "NNS",
    "NTA",
    "LIV",
    "OKA",
    "DBY",
    "TNS",
    "0BR",
    "08Y",
    "LW4",
    "P4P",
    "7HP",
    "NMG",
    "COU",
    "117",
    "ADE",
    "773",
    "DSF",
    "DOE",
    "STZ",
    "MII",
    "RMN",
    "DI",
    "ECS",
    "CFH",
    "PE9",
    "210",
    "AO3",
    "B1T",
    "FMR",
    "XLS",
    "WW7",
    "RLT",
    "2OH",
    "A",
    "TBA",
    "A20",
    "CRC",
    "CU3",
    "LLT",
    "DB8",
    "AFF",
    "469",
    "YYY",
    "0VT",
    "PCL",
    "ADP",
    "SFI",
    "FIL",
    "MIX",
    "RQ3",
    "LUR",
    "DDF",
    "P1B",
    "TAC",
    "NNR",
    "PML",
    "NVA",
    "TGN",
    "TCL",
    "BB8",
    "LYC",
    "CBM",
    "FNA",
    "0RP",
    "0TO",
    "MYF",
    "3AD",
    "1NP",
    "MIT",
    "QCT",
    "SFG",
    "TPS",
    "THL",
    "Z99",
    "CXX",
    "FID",
    "CGE",
    "URP",
    "TOU",
    "OLZ",
    "NOJ",
    "ADZ",
    "DNS",
    "PYR",
    "HE7",
    "H6P",
    "QIC",
    "NIS",
    "MCH",
    "PNX",
    "JKE",
    "CPB",
    "AKE",
    "NPS",
    "X2N",
    "CA4",
    "YTZ",
    "MOE",
    "FL7",
    "37T",
    "SMZ",
    "P77",
    "AHA",
    "QPT",
    "2MC",
    "919",
    "ENH",
    "SGV",
    "336",
    "GMP",
    "ID2",
    "R3W",
    "0CZ",
    "DSM",
    "RUT",
    "6PC",
    "B39",
    "NK",
    "PEY",
    "NPO",
    "DXX",
    "NHY",
    "ERG",
    "I22",
    "PN0",
    "MBD",
    "CL6",
    "3MI",
    "YTT",
    "DBX",
    "DOF",
    "4NC",
    "EVP",
    "04E",
    "1CA",
    "SRE",
    "BZ1",
    "ACR",
    "CO3",
    "SAS",
    "MTK",
    "HNQ",
    "PCG",
    "MST",
    "C5B",
    "RYN",
    "FG7",
    "ZGA",
    "ACA",
    "ATZ",
    "LE1",
    "GEN",
    "SAM",
    "CLS",
    "HY3",
    "ID3",
    "GCO",
    "BH4",
    "173",
    "AAH",
    "KBI",
    "DXT",
    "IHP",
    "QPS",
    "HXA",
    "EZL",
    "9CR",
    "1N1",
    "ACD",
    "RAL",
    "CF0",
    "DGT",
    "AND",
    "SIS",
    "SVR",
    "HFG",
    "AC0",
    "IPB",
    "PRP",
    "FAD",
    "GP9",
    "FEN",
    "ALR",
    "MFX",
    "2TY",
    "4AX",
    "3DM",
    "DPK",
    "B49",
    "NIX",
    "ALG",
    "SCA",
    "ECG",
    "LSA",
    "RR1",
    "RAF",
    "3QZ",
    "BG6",
    "NPU",
    "DHI",
    "U5P",
    "K2C",
    "CE3",
    "1PQ",
    "NBU",
    "KLV",
    "G",
    "T44",
    "IAC",
    "0SH",
    "C3S",
    "URO",
    "DNJ",
    "MQ7",
    "TO1",
    "HYP",
    "IBO",
    "PNE",
    "AC2",
    "DFV",
    "TSR",
    "FU1",
    "CCE",
    "ZLD",
    "CYT",
    "VAL",
    "EPJ",
    "K2N",
    "114",
    "30Z",
    "CLM",
    "2PM",
    "ALE",
    "6AP",
    "4PZ",
    "IMN",
    "HCZ",
    "HEM",
    "RIS",
    "DOQ",
    "T1G",
    "CAQ",
    "GSH",
    "ATG",
    "LNR",
    "RWF",
    "859",
    "IVM",
    "TSS",
    "LQZ",
    "C0R",
    "PRO",
    "POD",
    "HEP",
    "HAL",
    "RO7",
    "GBN",
    "YAN",
    "CFF",
    "PMP",
    "PTD",
    "PYS",
    "3TR",
    "B4P",
    "2MN",
    "IZP",
    "ASD",
    "FOK",
    "MTX",
    "3HP",
    "CWB",
    "MRP",
    "N7R",
    "KLT",
    "ZK5",
    "PCY",
    "15M",
    "977",
    "1IT",
    "AOR",
    "TLM",
    "CYH",
    "C2N",
    "LFX",
    "NCP",
    "218",
    "JUG",
    "IBP",
    "PC",
    "5CH",
    "3DB",
    "EFZ",
    "2BM",
    "NEQ",
    "MRE",
    "VDX",
    "AAC",
    "11C",
    "LAT",
    "CAT",
    "BHQ",
    "MTL",
    "NOV",
    "PNV",
    "GPF",
    "VX6",
    "BLQ",
    "NLA",
    "MYC",
    "RIM",
    "NIT",
    "ET1",
    "BZX",
    "T3",
    "2CS",
    "ZAR",
    "EEE",
    "DQH",
    "AKG",
    "DES",
    "JZV",
    "ERB",
    "F6Y",
    "ANQ",
    "GA3",
    "ASW",
    "14W",
    "3FG",
    "06X",
    "3IB",
    "PDD",
    "9CS",
    "CIR",
    "BI8",
    "BNS",
    "DZA",
    "LAX",
    "GA4",
    "F",
    "MC9",
    "POH",
    "OME",
    "LT4",
    "DQA",
    "3XH",
    "DAH",
    "HOA",
    "VAK",
    "URI",
    "DU",
    "BSP",
    "AL0",
    "PS9",
    "ROA",
    "LF7",
    "QO9",
    "SGE",
    "I6P",
    "OXD",
    "443",
    "ECN",
    "AOA",
    "DA",
    "RP1",
    "GLP",
    "GET",
    "032",
    "DR3",
    "DCZ",
    "CIY",
    "BAT",
    "DMQ",
    "PAB",
    "3NF",
    "PFL",
    "NO2",
    "ILE",
    "KEL",
    "104",
    "BZH",
    "4HY",
    "PA0",
    "TDP",
    "TIY",
    "68H",
    "V2H",
    "FMM",
    "TYR",
    "ZIT",
    "1DO",
    "CLY",
    "ACH",
    "8HG",
    "9PO",
    "HU5",
    "CO6",
    "CFX",
    "Q9C",
    "GDM",
    "BPN",
    "BT5",
    "SHF",
    "ROF",
    "AON",
    "Z80",
    "PBZ",
    "PFN",
    "HRM",
    "GBL",
    "D27",
    "AOI",
    "RHQ",
    "097",
    "XXX",
    "16A",
    "GND",
    "TTC",
    "6AC",
    "SHH",
    "07L",
    "TRE",
    "BB2",
    "FLU",
    "EOT",
    "Z34",
    "TNF",
    "06C",
    "MNG",
    "225",
    "1AL",
    "APC",
    "FLP",
    "VD1",
    "PAR",
    "0AZ",
    "PAL",
    "JMS",
    "ARG",
    "MRC",
    "ISN",
    "CLR",
    "PYF",
    "ASP",
    "NTM",
    "AGU",
    "OLU",
    "NFQ",
    "OHT",
    "I7A",
    "AZN",
    "230",
    "0J9",
    "PHZ",
    "SAN",
    "D7V",
    "BDP",
    "5HG",
    "BCM",
    "ETQ",
    "KIF",
    "0W8",
    "KKK",
    "IU5",
    "FMX",
    "SC5",
    "CNN",
    "D2V",
    "MUL",
    "VDY",
    "CHR",
    "MOP",
    "I7P",
    "417",
    "3HR",
    "AYA",
    "GGL",
    "AM2",
    "TTF",
    "PZQ",
    "AHN",
    "MHW",
    "TCI",
    "3MB",
    "LY4",
    "2BP",
    "CVI",
    "TES",
    "FFO",
    "DMD",
    "LAN",
    "B96",
    "3IO",
    "EQI",
    "NFL",
    "URC",
    "BI1",
    "4KO",
    "0TX",
    "REP",
    "BHD",
    "SNY",
    "EMU",
    "3AM",
    "FON",
    "BVD",
    "KYN",
    "PDC",
    "0RN",
    "0WM",
    "SY9",
    "LTN",
    "BER",
    "ZST",
    "URD",
    "CTY",
    "EV1",
    "AZ1",
    "BJM",
    "EXM",
    "RI5",
    "BOX",
    "COM",
    "1XJ",
    "B3N",
    "TME",
    "G3P",
    "DX9",
    "SNP",
    "B41",
    "DLU",
    "PLO",
    "ANL",
    "SLX",
    "385",
    "TCW",
    "TPF",
    "FUR",
    "THR",
    "BC1",
    "DAN",
    "XIX",
    "RBV",
    "BLD",
    "YCP",
    "AZ2",
    "RDF",
    "POY",
    "SQL",
    "PCI",
    "CIO",
    "GDE",
    "LTT",
    "DM2",
    "DPV",
    "DP4",
    "EDP",
    "RGG",
    "PPF",
    "4CH",
    "EME",
    "0HK",
    "DGJ",
    "0GV",
    "BZM",
    "RFX",
    "ABA",
    "ZPC",
    "TMI",
    "DIF",
    "RAP",
    "DT",
    "OSP",
    "QUN",
    "BC3",
    "BFQ",
    "2HC",
    "LGN",
    "PYV",
    "SUZ",
    "FUN",
    "3ID",
    "65B",
    "NBO",
    "BHN",
    "T22",
    "DCD",
    "CB1",
    "D16",
    "S11",
    "C04",
    "SAU",
    "PEJ",
    "B7D",
    "TEI",
    "RLJ",
    "TWO",
    "NIM",
    "147",
    "RDC",
    "GLC",
    "MYX",
    "803",
    "3D1",
    "211",
    "UCN",
    "LU2",
    "FK5",
    "OEM",
    "4MU",
    "SWA",
    "RSA",
    "TZZ",
    "SGS",
    "HDZ",
    "SFY",
    "EPB",
    "TTB",
    "HBC",
    "NT",
    "1SM",
    "T0M",
    "PEA",
    "TS8",
    "4HP",
    "LDP",
    "X94",
    "HY1",
    "8MO",
    "FMC",
    "NCH",
    "FJZ",
    "DHA",
    "M3L",
    "LYS",
    "BTN",
    "RNS",
    "XYL",
    "AOE",
    "CPT",
    "1TY",
    "FAH",
    "ZEA",
    "EFS",
    "04J",
    "4AZ",
    "TA1",
    "08D",
    "HT1",
    "NCT",
    "DCF",
    "LIP",
    "CLU",
    "ABU",
    "NRH",
    "0PY",
    "PIP",
    "MTA",
    "CIS",
    "CHO",
    "DMP",
    "TMO",
    "RIO",
    "GMC",
    "XED",
    "A5O",
    "TNT",
    "J77",
    "OTC",
    "W33",
    "HSX",
    "OLO",
    "OCA",
    "ASN",
    "CLT",
    "PIL",
    "G2F",
    "LEU",
    "UQ2",
    "I75",
    "UNK",
    "VIA",
    "MLK",
    "I0G",
    "NHP",
    "TYI",
    "BCG",
    "4OA",
    "PE2",
    "FER",
    "TMQ",
    "2AP",
    "FNZ",
    "ZZE",
    "PNN",
    "HID",
    "TZE",
    "DM1",
    "BZQ",
    "LNL",
    "BT6",
    "PDE",
    "LBF",
    "PMZ",
    "PZO",
    "DM5",
    "NOG",
    "DUT",
    "715",
    "DK1",
    "COH",
    "ETS",
    "DP6",
    "1MC",
    "PM6",
    "CNL",
    "DRZ",
    "TAO",
    "CTO",
    "HE2",
    "C5P",
    "AEN",
    "AAE",
    "NH3",
    "GKR",
    "THA",
    "BHS",
    "TRZ",
    "CTX",
    "79Z",
    "CDC",
    "SHR",
    "G50",
    "IDB",
    "X89",
    "CIB",
    "IXX",
    "LEI",
    "EDT",
    "OX1",
    "TXL",
    "MCT",
    "AMP",
    "GCS",
    "MEZ",
    "IOS",
    "DX4",
    "MOA",
    "MIY",
    "8CL",
    "MGR",
    "CCS",
    "GDS",
    "GOA",
    "MB3",
    "L0B",
    "DZP",
    "4AP",
    "RB0",
    "PAU",
    "GN1",
    "AS4",
    "RTL",
    "TFX",
    "HPA",
    "IZC",
    "OCS",
    "TPO",
    "1CS",
    "G39",
    "MCE",
    "ZCT",
    "ZD6",
    "DOL",
    "IUR",
    "B72",
    "NTI",
    "ZOL",
    "AA",
    "AS0",
    "H33",
    "NFN",
    "YOF",
    "DM6",
    "ET",
    "DR1",
    "RCO",
    "CL8",
    "ZON",
    "SMC",
    "G2H",
    "3GC",
    "PEM",
    "9CA",
    "BRL",
    "LUM",
    "MET",
    "Y00",
    "THG",
    "DCR",
    "EB4",
    "BNT",
    "FVX",
    "1LM",
    "CYY",
    "ASE",
    "P8S",
    "XRA",
    "ANF",
    "COX",
    "KYA",
    "HCI",
    "9RA",
    "END",
    "HFT",
    "FO1",
    "NIO",
    "MAN",
    "OLI",
    "IRE",
    "STR",
    "HUP",
    "D5M",
    "OBN",
    "GW6",
    "E4P",
    "MNR",
    "TLS",
    "3AT",
    "POL",
    "CSS",
    "UGA",
    "FOM",
    "RUB",
    "CQL",
    "CFA",
    "041",
    "BEQ",
    "PDA",
    "CBW",
    "DR7",
    "V55",
    "2AF",
    "LOC",
    "11D",
    "HXC",
    "EMO",
    "T13",
    "PNT",
    "TPV",
    "QUE",
    "EB1",
    "16Y",
    "FUC",
    "TUD",
    "EST",
    "DAP",
    "VDN",
    "X8Z",
    "EYK",
    "OBI",
    "PEL",
    "RPT",
    "ESM",
    "ZIO",
    "MKC",
    "QMR",
    "J2Z",
    "CTI",
    "ERY",
    "1KX",
    "706",
    "SRY",
    "V",
    "B81",
    "AIC",
    "SBI",
    "HDA",
    "MGS",
    "DME",
    "URB",
    "6FP",
    "486",
    "GLU",
    "NGM",
    "SP5",
    "SNL",
    "AER",
    "ZIP",
    "4MP",
    "H4B",
    "BRN",
    "JZ3",
    "9PL",
    "TOT",
    "TIC",
    "TRR",
    "CBO",
    "AIN",
    "Y27",
    "TMG",
    "TLT",
    "TYU",
    "0LI",
    "AME",
    "HYF",
    "FB2",
    "ZY7",
    "QV7",
    "AGI",
    "TEP",
    "PUY",
    "CUE",
    "INS",
    "AF",
    "NOX",
    "HSE",
    "TMP",
    "DUC",
    "N4E",
    "A26",
    "30B",
    "N2O",
    "SWF",
    "CXN",
    "16D",
    "TEL",
    "78P",
    "CRS",
    "TMH",
    "SLZ",
    "ICF",
    "RIT",
    "VGH",
    "DP0",
    "O",
    "0JN",
    "ZOM",
    "TIZ",
    "U02",
    "MYT",
    "TRP",
    "IGP",
    "TPA",
    "C2F",
    "IMH",
    "KOJ",
    "8PR",
    "HBA",
    "MZM",
    "LOB",
    "SSC",
    "AG0",
    "PNY",
    "IOH",
    "TH8",
    "CYZ",
    "AX3",
    "13X",
    "R18",
    "MK1",
    "BTL",
    "SLO",
    "QUS",
    "COC",
    "152",
    "FLH",
    "AZM",
    "API",
    "OCH",
    "VK3",
    "MMP",
    "IQS",
    "BAU",
    "JAN",
    "KSA",
    "CQA",
    "4TB",
    "PRL",
    "AP5",
    "XAV",
    "OHP",
    "SGA",
    "FUX",
    "URA",
    "ID8",
    "DEQ",
    "SYN",
    "1BO",
    "RIV",
    "S2H",
    "PXB",
    "BE2",
    "Z90",
    "DSC",
    "ARF",
    "HRP",
    "NEB",
    "RRC",
    "HTX",
    "T27",
    "HAN",
    "REE",
    "PSO",
    "MML",
    "2CG",
    "KTR",
    "SA0",
    "CU9",
    "HOP",
    "PHE",
    "SPS",
    "URF",
    "MEE",
    "EL",
    "C15",
    "ANW",
    "2PP",
    "HNI",
    "356",
    "MG7",
    "LGC",
    "CLQ",
    "0UN",
    "PF",
    "AOM",
    "OBG",
    "B1Q",
    "VPR",
    "DOR",
    "DE3",
    "4CS",
    "ETA",
    "NS4",
    "DDM",
    "A9S",
    "PG2",
    "NIL",
    "CGO",
    "RTZ",
    "L8P",
    "THB",
    "1FL",
    "NCD",
    "IM4",
    "OAS",
    "PAC",
    "GG2",
    "TON",
    "KIV",
    "TYK",
    "ICO",
    "SFX",
    "BDZ",
    "SHU",
    "1ZT",
    "DNF",
    "PME",
    "FME",
    "MLG",
    "34D",
    "DMG",
    "ORE",
    "PUC",
    "VGL",
    "NOS",
    "AC5",
    "1PC",
    "CHC",
    "BES",
    "1AC",
    "DCK",
    "FDP",
    "B31",
    "H3P",
    "VPX",
    "RFZ",
    "AXI",
    "IPD",
    "HCC",
    "NXX",
    "PHT",
    "F42",
    "FLV",
    "BRF",
    "PZE",
    "TOL",
    "LLC",
    "AE2",
    "HAB",
    "XDE",
    "IBI",
    "0U9",
    "RBT",
    "SKA",
    "CY9",
    "EAA",
    "7NI",
    "GJZ",
    "43M",
    "AMR",
    "ENO",
    "4DI",
    "RHB",
    "NDR",
    "SHA",
    "CSD",
    "DZN",
    "BHA",
    "HCY",
    "NIZ",
    "13D",
    "BAL",
    "KH1",
    "HLT",
    "FCN",
    "HIS",
    "AGH",
    "NZO",
    "XYP",
    "A8S",
    "C41",
    "BLS",
    "CHZ",
    "AMW",
    "2TN",
    "FOA",
    "BPV",
    "ASR",
    "TRB",
    "SOR",
    "TFO",
    "SXX",
    "PRM",
    "GSN",
    "HRG",
    "U",
    "ZIR",
    "08H",
    "D4P",
    "DE1",
    "REN",
    "SMX",
    "FMN",
    "PAE",
    "LY2",
    "RAV",
    "2TB",
    "SC2",
    "SPB",
    "HQE",
    "OCE",
    "DMA",
    "KHA",
    "OHM",
    "08J",
    "DHT",
    "PLQ",
    "NFZ",
    "SMA",
    "X0T",
    "ROC",
    "DIC",
    "NPY",
    "5MU",
    "OC9",
    "1UN",
    "DEX",
    "HLZ",
    "MEL",
    "N6M",
    "1CY",
    "VOR",
    "SD5",
    "PP3",
    "ZNH",
    "CSU",
    "HZP",
    "TOK",
    "AZG",
    "TPM",
    "NO",
    "TK4",
    "42C",
    "CYS",
    "BPR",
    "PGG",
    "TSZ",
    "MT1",
    "F50",
    "ML1",
    "DSN",
    "MTT",
    "MI1",
    "VIR",
    "BO2",
    "PXL",
    "QSO",
    "AZS",
    "NMM",
    "NEC",
    "PL3",
    "5FW",
    "BSU",
    "AEF",
    "OYA",
    "PBG",
    "MHM",
    "UN1",
    "CZA",
    "FUA",
    "TOP",
    "CTC",
    "NEH",
    "DB7",
    "IFM",
    "CLL",
    "FWD",
    "SEP",
    "TCK",
    "AZT",
    "LPA",
    "TRU",
    "SLB",
    "STL",
    "FUD",
    "TP0",
    "JTZ",
    "RAB",
    "GM6",
    "AZO",
    "EGG",
    "N2P",
    "HOS",
    "ESL",
    "SDS",
    "0LA",
    "LDZ",
    "C21",
    "CIL",
    "MOF",
    "XYS",
    "UQ8",
    "FC6",
    "MCG",
    "REM",
    "2GM",
    "MBT",
    "MPB",
    "VXX",
    "M51",
    "GRE",
    "EHD",
    "SLF",
    "GLA",
    "505",
    "CYU",
    "AMZ",
    "PGX",
    "AFB",
    "OTR",
    "DGY",
    "ANM",
    "STU",
    "NLQ",
    "ILO",
    "TC9",
    "ACO",
    "ASC",
    "FPO",
    "1GP",
    "AB1",
    "THH",
    "DCE",
    "APZ",
    "3HA",
    "WY1",
    "11A",
    "CLW",
    "1TB",
    "A80",
    "OXI",
    "GD9",
    "2ND",
    "FSM",
    "AZZ",
    "KDH",
    "W71",
    "B6P",
    "LQQ",
    "FIT",
    "CXL",
    "PAV",
    "MXL",
    "MAH",
    "ADA",
    "RKE",
    "NIN",
    "FLR",
    "NIV",
    "198",
    "HEF",
    "ROX",
    "HBX",
    "3TF",
    "MIG",
    "ALA",
    "SAK",
    "MRY",
    "BMM",
    "PXM",
    "LYA",
    "PNC",
    "TR5",
    "BMA",
    "AFT",
    "TUB",
    "MZR",
    "4AT",
    "308",
    "PIQ",
    "UOC",
    "ISP",
    "HCD",
    "CBD",
    "GA2",
    "PNF",
    "SRO",
    "VLB",
    "BL1",
    "MAL",
    "17Z",
    "ABN",
    "DRN",
    "UMP",
    "EMT",
    "RFP",
    "AR",
    "911",
    "NAI",
    "JZ0",
    "PND",
    "E20",
    "NTO",
    "ONA",
    "EP",
    "5CL",
    "PNS",
    "TNG",
    "HSM",
    "GHP",
    "MOI",
    "PQN",
    "CP6",
    "0XE",
    "N7I",
    "AMH",
    "ZMR",
    "M77",
    "MIL",
    "5GP",
    "CMP",
    "MAX",
    "SCK",
    "F89",
    "A2F",
    "RAM",
    "NQ",
    "HGU",
    "G34",
    "TOR",
    "PYG",
    "I1E",
    "H4S",
    "SER",
    "X2M",
    "EA1",
    "KS1",
    "AGG",
    "3AB",
    "TXC",
    "P1Z",
    "BCT",
    "88Z",
    "RHN",
    "DAL",
    "3QU",
    "4NS",
    "0L1",
    "VIT",
    "IGN",
    "478",
    "GTX",
    "LPB",
    "2AE",
    "KNA",
    "4FE",
    "GTR",
    "FRD",
    "2HA",
    "4NL",
    "ALY",
    "XIN",
    "KXN",
    "DIT",
    "U33",
    "NAD",
    "MCM",
    "CEL",
    "EQN",
    "SCI",
    "FLF",
    "FOZ",
    "6NA",
    "4NP",
    "GMN",
    "TYL",
    "W11",
    "IQB",
    "FVS",
    "GLN",
    "TUH",
    "GPJ",
    "QRP",
    "BS4",
    "DXC",
    "ETV",
    "AHD",
    "3NP",
    "PF2",
    "AES",
    "MCZ",
    "PCR",
    "GEO",
    "2DI",
    "OXL",
    "NLG",
    "KAN",
    "HMU",
    "SA9",
    "TF4",
    "WPP",
    "3GR",
    "017",
    "8DG",
    "AB0",
    "AKN",
    "AC6",
    "ISD",
    "EOL",
    "IAS",
    "OPE",
    "ECT",
    "T98",
    "GMM",
    "CRN",
    "EDR",
    "1K5",
    "REF",
    "CP0",
    "ADN",
    "TFP",
    "KWT",
    "SCR",
    "MLR",
    "AQ4",
    "DAT",
    "IWR",
    "CFB",
    "RZX",
    "XAN",
    "BZI",
    "H8H",
    "3CE",
    "3T5",
    "CL9",
    "1YJ",
    "1YE",
    "BUA",
    "TLF",
    "HI6",
    "NPE",
    "DBH",
    "ZES",
    "TDR",
    "ORN",
    "0UB",
    "MBR",
    "MEM",
    "VD3",
    "C2M",
    "EAL",
    "DXE",
    "06Y",
    "MLO",
    "C",
    "BFP",
    "5EH",
    "VIV",
    "MGX",
    "DCP",
    "CBL",
    "ERM",
    "BCD",
    "AR3",
    "6MP",
    "35G",
    "DP7",
    "FLW",
    "B4N",
    "OMP",
    "LDC",
    "C4C",
    "ALO",
    "0QA",
    "KNI",
    "EJ4",
    "MLC",
    "ELV",
    "CHX",
    "174",
    "D3M",
    "SAH",
    "AD5",
    "BNL",
    "PDO",
    "NON",
    "EPA",
    "RS3",
    "TBN",
    "CTN",
    "03V",
    "FUM",
    "CBU",
    "TOY",
    "DAR",
    "268",
    "TAZ",
    "3HB",
    "E4B",
    "ECO",
    "TNL",
    "MPT",
    "DPR",
    "LNV",
    "BAX",
    "HPP",
    "3PY",
    "WRA",
    "C2R",
    "LBT",
    "PSP",
    "KOP",
    "GTQ",
    "GCH",
    "406",
    "ITU",
    "07J",
    "09N",
    "TCH",
    "TSN",
    "RBF",
    "9TP",
    "SSF",
    "B3D",
    "BGC",
    "MMZ",
    "BEP",
    "BEN",
    "KMP",
    "GIQ",
    "A77",
    "DLY",
    "STG",
    "OXY",
    "PAW",
    "ATP",
    "ESC",
    "KTN",
    "IYR",
    "PZA",
    "ECL",
    "PD1",
    "DID",
    "CDX",
    "DHL",
    "VIB",
    "LAS",
    "AVP",
    "J3Z",
    "2ZS",
    "MSM",
    "AG2",
    "F6Z",
    "ITP",
    "1CP",
    "SCM",
    "GNG",
    "DHC",
    "AX2",
    "JN3",
    "TKT",
    "ACJ",
    "PRS",
    "142",
    "IBN",
    "NBV",
    "IPE",
    "P7I",
    "HQY",
    "H35",
    "AVN",
    "15U",
    "GNT",
    "DA2",
    "CH5",
    "DX2",
    "CTS",
    "KLN",
    "STI",
    "LPR",
    "AP7",
    "DUR",
    "HEG",
    "CFE",
    "S1P",
    "TIM",
    "GAL",
    "TQ8",
    "NAR",
    "MXA",
    "5ID",
    "COA",
    "IQU",
    "3TC",
    "GMY",
    "MNH",
    "PLP",
    "GAS",
    "XUL",
    "J01",
    "4MZ",
    "NRG",
    "NAJ",
    "VJJ",
    "5BM",
    "BP4",
    "PZI",
    "0HQ",
    "MNS",
    "B40",
    "FAQ",
    "AMJ",
    "ATI",
    "MDN",
    "CBE",
    "MYU",
    "1BN",
    "HT",
    "OIN",
    "SPP",
    "CIA",
    "U10",
    "PA1",
    "RET",
    "ELD",
    "B3I",
    "CPF",
    "KOV",
    "DGX",
    "HFZ",
    "PYI",
    "DMY",
    "REA",
    "667",
    "TAG",
    "EIC",
    "AOX",
    "MEV",
    "NCA",
    "MXD",
    "NMY",
    "HMT",
    "ANI",
]

chem_lst = [
    "GLY",
    "CL",
    "TCE",
    "IOD",
    "BR",
    "MO",
    "RE",
    "HO",
    "RU1",
    "W1",
    "OS",
    "IR",
    "PT",
    "PT1",
    "AU",
    "HG",
    "CE",
    "PR",
    "SM",
    "EU",
    "GD",
    "TB",
    "YB",
    "LU",
    "AL",
    "GA",
    "IN",
    "SB",
    "TL",
    "PB",
    "PD",
    "AG",
    "CD",
    "LA",
    "W",
    "RU",
    "NI",
    "CR",
    "BA",
    "CS",
    "SR",
    "RB",
    "K",
    "NA",
    "LI",
    "CA",
    "SQD",
    "NBN",
    "L2C",
    "NAA",
    "DOD",
    "8PE",
    "1PG",
    "DDR",
    "MW2",
    "ME2",
    "MN5",
    "NDG",
    "PLD",
    "XE",
    "PBM",
    "ULI",
    "UNL",
    "12P",
    "SQU",
    "NAG",
    "LCO",
    "MLT",
    "2PE",
    "TAU",
    "PEU",
    "PX4",
    "IRI",
    "DTU",
    "GUN",
    "CD4",
    "DAO",
    "144",
    "OCM",
    "NER",
    "SIN",
    "MW3",
    "HED",
    "LDA",
    "CYC",
    "KR",
    "OCT",
    "DPO",
    "BOG",
    "DEP",
    "PMS",
    "TLA",
    "CO2",
    "TCA",
    "L44",
    "EAP",
    "NEX",
    "HEX",
    "EDO",
    "OF3",
    "7PH",
    "P22",
    "CDL",
    "A2G",
    "TE",
    "CUZ",
    "NET",
    "PI",
    "POV",
    "MMC",
    "AU3",
    "C10",
    "LMT",
    "PER",
    "IR3",
    "PHQ",
    "OC3",
    "ETX",
    "ETE",
    "SAR",
    "L4P",
    "DHB",
    "DIO",
    "DKA",
    "BO3",
    "PG0",
    "1PE",
    "MBN",
    "BNZ",
    "PO4",
    "NGZ",
    "PGT",
    "DGG",
    "BU1",
    "PGO",
    "P3G",
    "MLI",
    "SPH",
    "6PE",
    "NH4",
    "MO5",
    "P4C",
    "MAC",
    "CD3",
    "EOH",
    "UND",
    "ETF",
    "VO4",
    "TBU",
    "MC3",
    "CNS",
    "IPA",
    "LHG",
    "7PG",
    "CAD",
    "P4G",
    "SWE",
    "MES",
    "7E9",
    "THJ",
    "PAM",
    "TRD",
    "LIO",
    "TGL",
    "MW1",
    "NA2",
    "YT3",
    "ENC",
    "CE9",
    "OF1",
    "PE5",
    "PEV",
    "CMO",
    "MO3",
    "3PE",
    "TG1",
    "CMJ",
    "HEZ",
    "ARS",
    "XAT",
    "MYY",
    "DTD",
    "SPK",
    "PLC",
    "6PL",
    "H2S",
    "P1O",
    "CE1",
    "HSH",
    "TRA",
    "NO3",
    "MO6",
    "BTB",
    "OPC",
    "PG6",
    "E4N",
    "SE4",
    "PGR",
    "PC2",
    "TRS",
    "NCO",
    "7E8",
    "5AD",
    "OCN",
    "BEZ",
    "DMF",
    "HTO",
    "N8E",
    "02U",
    "MYS",
    "MBO",
    "PPI",
    "CON",
    "SOG",
    "STE",
    "HAE",
    "MTE",
    "HTG",
    "AF3",
    "PEE",
    "P33",
    "AE4",
    "LXB",
    "MOH",
    "GVT",
    "P15",
    "4AG",
    "DPG",
    "ORO",
    "3NI",
    "KO4",
    "SCN",
    "CO5",
    "L1P",
    "PE8",
    "3PG",
    "MO4",
    "RSG",
    "OC5",
    "FOR",
    "MVC",
    "PHB",
    "BEN",
    "YEG",
    "NAW",
    "2OP",
    "B3H",
    "DHJ",
    "UNX",
    "NAO",
    "HCS",
    "BM3",
    "D10",
    "HOH",
    "DGA",
    "MH3",
    "CD5",
    "XPE",
    "THM",
    "BME",
    "FLC",
    "GLV",
    "P25",
    "15P",
    "MH2",
    "OLA",
    "DTV",
    "FTT",
    "KEN",
    "ACM",
    "CPS",
    "NVP",
    "SUC",
    "R16",
    "CCN",
    "PX2",
    "OC6",
    "3PH",
    "MPD",
    "EMC",
    "MOS",
    "LMR",
    "NA5",
    "LAC",
    "DTT",
    "GOL",
    "LCP",
    "HGP",
    "OC4",
    "PX8",
    "CXS",
    "OCL",
    "BET",
    "MO1",
    "KAI",
    "PG4",
    "CN6",
    "PPV",
    "7PE",
    "PTN",
    "IMD",
    "NA6",
    "13P",
    "AUC",
    "SPD",
    "OES",
    "SO4",
    "PGF",
    "PEH",
    "CD1",
    "P6G",
    "MAE",
    "HAI",
    "SRT",
    "MLA",
    "HSG",
    "BNG",
    "PUT",
    "PD7",
    "KDO",
    "DVT",
    "DMS",
    "GAI",
    "NC",
    "L2P",
    "DMR",
    "PTY",
    "AE3",
    "SMO",
    "OXM",
    "L3P",
    "HT3",
    "DMI",
    "D1D",
    "HGC",
    "BHG",
    "AGA",
    "PCF",
    "DDQ",
    "IBM",
    "PEO",
    "1AG",
    "GGD",
    "PC6",
    "LFA",
    "BE7",
    "CYN",
    "PEK",
    "OLC",
    "LMG",
    "MYR",
    "I42",
    "TWT",
    "PLM",
    "PGE",
    "TAM",
    "IPH",
    "PSC",
    "MPO",
    "HTH",
    "LI1",
    "6JZ",
    "BXC",
    "MO2",
    "PGV",
    "UMQ",
    "DET",
    "RG1",
    "OC2",
    "BGL",
    "SPM",
    "LXZ",
    "SGM",
    "TCN",
    "YB2",
    "HGX",
    "XPA",
    "16P",
    "ICT",
    "1EM",
    "SPZ",
    "PC7",
    "DGD",
    "NHE",
    "OH",
    "PE3",
    "SPJ",
    "PEX",
    "543",
    "SO2",
    "FMT",
    "DUD",
    "CHT",
    "F09",
    "AKR",
    "6UL",
    "MSE",
    "CHD",
    "Y1",
    "PC8",
    "NSP",
    "PQ9",
    "PG8",
    "CXE",
    "GD3",
    "M2M",
    "9PE",
    "PL9",
    "OCO",
    "FOL",
    "U1",
    "CB3",
    "OGA",
    "BAM",
    "XP4",
    "LMU",
    "B3P",
    "LUT",
    "SAL",
    "BCN",
    "PG5",
    "IPL",
    "ACN",
    "PEG",
    "DD9",
    "TAR",
    "EU3",
    "XY2",
    "C1O",
    "C2O",
    "C14",
    "PT4",
    "DMN",
    "PA8",
    "PX6",
    "RSF",
    "HCA",
    "TOE",
    "D12",
    "EPE",
    "CN3",
    "PEF",
    "THE",
    "UPL",
    "TMA",
    "TEA",
    "BO4",
    "D01",
    "HP6",
    "BCR",
    "PC1",
    "SPW",
    "IUM",
    "URE",
    "ACT",
    "6PH",
    "ACY",
    "LPP",
    "CIT",
    "NGA",
    "SOH",
    "PE4",
    "YF3",
    "MRD",
    "2DP",
    "RHD",
    "HC4",
    "CAC",
    "OC1",
    "SX",
    "MGE",
    "OLB",
    "CVK",
]
mod_lst = ["ACE", "FAR", "GER", "CMT", "CSO", "CSX"]

mem_lst = ["PCW", "17F", "7Q9"]

lig_class_dict = {
    bio_lig_col: bio_lst,
    ion_lig_col: ion_lst,
    pharm_lig_col: pharm_lst,
    chem_lig_col: chem_lst,
    mod_lig_col: mod_lst,
    mem_lig_col: mem_lst,
}

lig_col_lst = list(lig_class_dict.keys())