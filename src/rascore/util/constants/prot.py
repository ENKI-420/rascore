# -*- coding: utf-8 -*-
"""
  Copyright 2022 Mitchell Isaac Parker

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""

from ..functions.color import get_lst_colors

rbd_pfam = "RBD"
pi3k_pfam = "PI3K_RBD"
ra_pfam = "RA"
ra_gef_pfam = "RA-RasGEF"
gef_pfam = "RasGEF"
gap_pfam = "RasGAP"

effector_name = "Effector"
gef_name = "GEF"
gap_name = "GAP"
nano_name = "Nanodisc"
binder_name = "Binder"
other_prot_name = "Other"
mult_prot_name = "Multiple"
none_prot_name = "None"

cdc_name = "CDC25"
rem_name = "REM"

gef_cdc_name = f"{gef_name}.{cdc_name}"
gef_rem_name = f"{gef_name}.{rem_name}"

prot_class_dict = {
    effector_name: [rbd_pfam, pi3k_pfam, ra_pfam, ra_gef_pfam],
    gef_name: [gef_pfam],
    gap_name: [gap_pfam],
    nano_name: [nano_name],
    binder_name: [binder_name],
    other_prot_name: [other_prot_name],
    none_prot_name: [none_prot_name],
}

prot_class_lst = [
    effector_name,
    gap_name,
    gef_cdc_name,
    gef_rem_name,
    binder_name,
    nano_name,
    other_prot_name,
    none_prot_name,
]

prot_color_dict = get_lst_colors(
    [
        effector_name,
        gap_name,
        gef_name,
        binder_name,
        nano_name,
        other_prot_name,
        none_prot_name,
    ],
    palette="Set2",
    return_dict=True,
)

prot_color_dict[gef_cdc_name] = prot_color_dict[gef_name]
prot_color_dict[gef_rem_name] = prot_color_dict[gef_name]


prot_pfam_dict = {
    "APOA1_HUMAN": "Nanodisc",
    "RASF1_HUMAN": "RA",
    "RADIL_HUMAN": "RA",
    "RAPH1_HUMAN": "RA",
    "RASF1_CAEEL": "RA",
    "SPRI_DROME": "RA",
    "RASF5_HUMAN": "RA",
    "RPGF2_MOUSE": "RA-RasGEF",
    "RPGF6_HUMAN": "RA-RasGEF",
    "RASF5_MOUSE": "RA",
    "RPGF2_BOVIN": "RA-RasGEF",
    "SNX27_MOUSE": "RA",
    "PLCE1_HUMAN": "RA-RasGEF",
    "PLCE1_MOUSE": "RA-RasGEF",
    "SNX27_HUMAN": "RA",
    "MYO9B_MOUSE": "RA",
    "SNX27_RAT": "RA",
    "RASF2_MOUSE": "RA",
    "RAIN_HUMAN": "RA",
    "RPGF2_RAT": "RA-RasGEF",
    "MYO10_BOVIN": "RA",
    "MYO9B_HUMAN": "RA",
    "MY9AA_DANRE": "RA",
    "RAIN_MOUSE": "RA",
    "RIN2_HUMAN": "RA",
    "RPGF2_CANLF": "RA-RasGEF",
    "RASF2_HUMAN": "RA",
    "MST50_MAGO7": "RA",
    "PKHH3_HUMAN": "RA",
    "STE50_YEAST": "RA",
    "RASF4_HUMAN": "RA",
    "RADIL_DANRE": "RA",
    "RHG20_RAT": "RA",
    "STE4_SCHPO": "RA",
    "RASF4_RAT": "RA",
    "RASF1_MOUSE": "RA",
    "RGL2_MOUSE": "RA-RasGEF",
    "SNX27_BOVIN": "RA",
    "RGL2_HUMAN": "RA-RasGEF",
    "RASF5_RAT": "RA",
    "RASF7_MOUSE": "RA",
    "RPGF_CAEEL": "RA-RasGEF",
    "RASF6_HUMAN": "RA",
    "RGL1_DANRE": "RA-RasGEF",
    "RHG20_HUMAN": "RA",
    "RGL3_MOUSE": "RA-RasGEF",
    "PKHH3_RAT": "RA",
    "RASF2_RAT": "RA",
    "RASF6_MOUSE": "RA",
    "RGL1_HUMAN": "RA-RasGEF",
    "RGL3_HUMAN": "RA-RasGEF",
    "Y7875_DICDI": "RA",
    "RASF4_MOUSE": "RA",
    "RASF8_HUMAN": "RA",
    "RASF6_RAT": "RA",
    "RASF7_HUMAN": "RA",
    "PLCE1_RAT": "RA-RasGEF",
    "RHG20_MOUSE": "RA",
    "RGL2_CANLF": "RA-RasGEF",
    "MYO9A_RAT": "RA",
    "MYO9B_RAT": "RA",
    "RIN1_HUMAN": "RA",
    "PLCE1_CAEEL": "RA-RasGEF",
    "RGL1_MOUSE": "RA-RasGEF",
    "RPGF2_HUMAN": "RA-RasGEF",
    "RADIL_MOUSE": "RA",
    "RIN2_MOUSE": "RA",
    "RASF3_MOUSE": "RA",
    "AB1IP_XENLA": "RA",
    "GNDS_RAT": "RA-RasGEF",
    "GRB7_RAT": "RA",
    "AB1IP_MOUSE": "RA",
    "AB1IP_HUMAN": "RA",
    "AFAD_MOUSE": "RA",
    "DGKQ_MOUSE": "RA",
    "AB1IP_CHICK": "RA",
    "AFAD_HUMAN": "RA",
    "DGKQ_HUMAN": "RA",
    "ARAP1_HUMAN": "RA",
    "ARAP2_HUMAN": "RA",
    "ARAP1_MOUSE": "RA",
    "GRB10_PIG": "RA",
    "ARAP3_MOUSE": "RA",
    "AB1IP_DANRE": "RA",
    "GNDS_HUMAN": "RA-RasGEF",
    "ARAP3_HUMAN": "RA",
    "GRB14_HUMAN": "RA",
    "AFAD_RAT": "RA",
    "DGKQ_RAT": "RA",
    "ARAP2_MOUSE": "RA",
    "GRB7_HUMAN": "RA",
    "GRB10_MOUSE": "RA",
    "GRB14_BOVIN": "RA",
    "MYO9A_MOUSE": "RA",
    "GRB14_MOUSE": "RA",
    "GRB14_RAT": "RA",
    "GRB10_HUMAN": "RA",
    "MYO9A_HUMAN": "RA",
    "GNDS_MOUSE": "RA-RasGEF",
    "MYO10_HUMAN": "RA",
    "GRB7_MOUSE": "RA",
    "MY9AB_DANRE": "RA",
    "GRB7_BOVIN": "RA",
    "GRB10_RAT": "RA",
    "RASF3_HUMAN": "RA",
    "PKHH3_MOUSE": "RA",
    "RASF8_MOUSE": "RA",
    "RAF1_HUMAN": "RBD",
    "RAF1_MOUSE": "RBD",
    "TIAM1_MOUSE": "RBD",
    "RAF1_CHICK": "RBD",
    "RGS_DROME": "RBD",
    "RAF1_PONAB": "RBD",
    "RGS14_HUMAN": "RBD",
    "RGS14_MOUSE": "RBD",
    "RAF1_RAT": "RBD",
    "RAF1_BOVIN": "RBD",
    "RGS12_RAT": "RBD",
    "TIAM1_HUMAN": "RBD",
    "RGS14_RAT": "RBD",
    "RGS12_HUMAN": "RBD",
    "ARAF_HUMAN": "RBD",
    "ARAF_RAT": "RBD",
    "BRAF_COTJA": "RBD",
    "BRAF_HUMAN": "RBD",
    "BRAF_MOUSE": "RBD",
    "KRAF1_CAEEL": "RBD",
    "KRAF1_DROME": "RBD",
    "RIP3_DICDI": "RBD",
    "BRAF_CHICK": "RBD",
    "SIF1_DROME": "RBD",
    "ARAF_MOUSE": "RBD",
    "SIF2_DROME": "RBD",
    "RGS12_MOUSE": "RBD",
    "RAF1_XENLA": "RBD",
    "ARAF_PIG": "RBD",
    "KRAF1_CAEBR": "RBD",
    "PK3CD_HUMAN": "PI3K_RBD",
    "PK3CD_MOUSE": "PI3K_RBD",
    "PI3K2_DICDI": "PI3K_RBD",
    "P3C2A_HUMAN": "PI3K_RBD",
    "PK3CG_PIG": "PI3K_RBD",
    "PK3CA_BOVIN": "PI3K_RBD",
    "P3C2B_HUMAN": "PI3K_RBD",
    "PK3CG_MOUSE": "PI3K_RBD",
    "PK3CA_RAT": "PI3K_RBD",
    "PK3CB_HUMAN": "PI3K_RBD",
    "P3C2A_MOUSE": "PI3K_RBD",
    "PI3K1_DICDI": "PI3K_RBD",
    "AGE1_CAEEL": "PI3K_RBD",
    "PK3CB_MOUSE": "PI3K_RBD",
    "PK3CA_HUMAN": "PI3K_RBD",
    "PK3CG_HUMAN": "PI3K_RBD",
    "PK3CB_RAT": "PI3K_RBD",
    "PK3CA_MOUSE": "PI3K_RBD",
    "P3C2A_PONAB": "PI3K_RBD",
    "P3C2G_HUMAN": "PI3K_RBD",
    "P3C2G_RAT": "PI3K_RBD",
    "PI3K3_DICDI": "PI3K_RBD",
    "AGE1_CAEBR": "PI3K_RBD",
    "SOS1_MOUSE": "RasGEF",
    "SH2D3_HUMAN": "RasGEF",
    "RGRF1_MOUSE": "RasGEF",
    "LTE1_YEAST": "RasGEF",
    "RPGF1_HUMAN": "RasGEF",
    "SOS_DROME": "RasGEF",
    "RPGF3_RAT": "RasGEF",
    "SH2D3_MOUSE": "RasGEF",
    "RGRF2_MOUSE": "RasGEF",
    "RPGF3_MOUSE": "RasGEF",
    "RPGF4_RAT": "RasGEF",
    "SOS2_HUMAN": "RasGEF",
    "RPGF4_HUMAN": "RasGEF",
    "RGRF1_RAT": "RasGEF",
    "RGPS1_HUMAN": "RasGEF",
    "RPGF3_HUMAN": "RasGEF",
    "RGPS1_DANRE": "RasGEF",
    "SOS_CAEEL": "RasGEF",
    "RG1BA_DANRE": "RasGEF",
    "RPGF5_RAT": "RasGEF",
    "SDC25_YEAS8": "RasGEF",
    "GRP2A_XENLA": "RasGEF",
    "RPGFL_MOUSE": "RasGEF",
    "RPGF1_CAEEL": "RasGEF",
    "RGPS1_CHICK": "RasGEF",
    "RGPS2_MACFA": "RasGEF",
    "RGRF2_RAT": "RasGEF",
    "RGPS2_HUMAN": "RasGEF",
    "STE6_SCHPO": "RasGEF",
    "RPGFL_PONPY": "RasGEF",
    "SDC25_YEAS6": "RasGEF",
    "SDC25_YEAS1": "RasGEF",
    "RGF1C_MOUSE": "RasGEF",
    "GRP2B_XENLA": "RasGEF",
    "KNDC1_HUMAN": "RasGEF",
    "GRP4_BOVIN": "RasGEF",
    "RGF1C_MACFA": "RasGEF",
    "RPGFL_HUMAN": "RasGEF",
    "RGF1C_HUMAN": "RasGEF",
    "RG1BB_DANRE": "RasGEF",
    "RGRF2_DANRE": "RasGEF",
    "RGPS1_MOUSE": "RasGEF",
    "RPGF5_MOUSE": "RasGEF",
    "RPGF5_HUMAN": "RasGEF",
    "YL016_YEAST": "RasGEF",
    "RGPS2_MOUSE": "RasGEF",
    "RPGF4_MOUSE": "RasGEF",
    "RGRF2_HUMAN": "RasGEF",
    "SDC25_YEAS7": "RasGEF",
    "SOS2_MOUSE": "RasGEF",
    "SOS1_HUMAN": "RasGEF",
    "SDC25_YEASX": "RasGEF",
    "RGRF1_HUMAN": "RasGEF",
    "BCAR3_MOUSE": "RasGEF",
    "EFC25_SCHPO": "RasGEF",
    "GBPC_DICDI": "RasGEF",
    "GRP2_MOUSE": "RasGEF",
    "BCAR3_HUMAN": "RasGEF",
    "CDC25_CANAL": "RasGEF",
    "CDC25_LACKL": "RasGEF",
    "CDC25_YEAST": "RasGEF",
    "BCAR3_RAT": "RasGEF",
    "BCAR3_BOVIN": "RasGEF",
    "BEM2_ASHGO": "RasGEF",
    "BUD5_YEAST": "RasGEF",
    "GFLB_DICDI": "RasGEF",
    "GRP3_HUMAN": "RasGEF",
    "GEFE_DICDI": "RasGEF",
    "GEFG_DICDI": "RasGEF",
    "GEFH_DICDI": "RasGEF",
    "GEFK_DICDI": "RasGEF",
    "GEFN_DICDI": "RasGEF",
    "GEFO_DICDI": "RasGEF",
    "GEFX_DICDI": "RasGEF",
    "GEFY_DICDI": "RasGEF",
    "GEFA_DICDI": "RasGEF",
    "GEFB_DICDI": "RasGEF",
    "GEFC_DICDI": "RasGEF",
    "GRP2_BOVIN": "RasGEF",
    "BEM2_YEAST": "RasGEF",
    "GEFD_DICDI": "RasGEF",
    "GEFF_DICDI": "RasGEF",
    "GEFI_DICDI": "RasGEF",
    "GEFJ_DICDI": "RasGEF",
    "GEFL_DICDI": "RasGEF",
    "GEFM_DICDI": "RasGEF",
    "GEFP_DICDI": "RasGEF",
    "GEFQ_DICDI": "RasGEF",
    "GEFR_DICDI": "RasGEF",
    "GEFS_DICDI": "RasGEF",
    "GEFV_DICDI": "RasGEF",
    "GEFW_DICDI": "RasGEF",
    "LTE1_ASHGO": "RasGEF",
    "GRP4_RAT": "RasGEF",
    "GRP1_XENLA": "RasGEF",
    "GRP4_HUMAN": "RasGEF",
    "GRP1_HUMAN": "RasGEF",
    "BCAR3_XENLA": "RasGEF",
    "BCAR3_MACFA": "RasGEF",
    "GBPD_DICDI": "RasGEF",
    "GRP4_MOUSE": "RasGEF",
    "GRP1_XENTR": "RasGEF",
    "KNDC1_MOUSE": "RasGEF",
    "GRP1_RAT": "RasGEF",
    "LTE1_CANGA": "RasGEF",
    "LTE1_KLULA": "RasGEF",
    "GRP1_MOUSE": "RasGEF",
    "GRP2_RAT": "RasGEF",
    "GRP2_HUMAN": "RasGEF",
    "RGDSR_HUMAN": "RasGEF",
    "RGF1B_HUMAN": "RasGEF",
    "RGF1B_PONAB": "RasGEF",
    "RGF1A_HUMAN": "RasGEF",
    "RGF1A_XENTR": "RasGEF",
    "RGF1B_BOVIN": "RasGEF",
    "RGF1B_MOUSE": "RasGEF",
    "RGF1B_XENTR": "RasGEF",
    "C3G_DROME": "RasGEF",
    "RASA3_HUMAN": "RasGAP",
    "RASL3_HUMAN": "RasGAP",
    "RNG2_SCHPO": "RasGAP",
    "RASL2_HUMAN": "RasGAP",
    "NF1_HUMAN": "RasGAP",
    "IQGA1_MOUSE": "RasGAP",
    "IQG1_YEAST": "RasGAP",
    "RGAA_DICDI": "RasGAP",
    "IQGA2_HUMAN": "RasGAP",
    "RASA1_HUMAN": "RasGAP",
    "SYGP1_MOUSE": "RasGAP",
    "SYGP1_RAT": "RasGAP",
    "RASA1_RAT": "RasGAP",
    "RME6_CAEEL": "RasGAP",
    "BUD2_CANAL": "RasGAP",
    "DAB2P_HUMAN": "RasGAP",
    "GAPD1_MOUSE": "RasGAP",
    "GAP1_DROME": "RasGAP",
    "DAB2P_RAT": "RasGAP",
    "GAPD1_HUMAN": "RasGAP",
    "GAPA_DICDI": "RasGAP",
    "NF1_RAT": "RasGAP",
    "IQGA3_HUMAN": "RasGAP",
    "NF1_MOUSE": "RasGAP",
    "IQGA1_HUMAN": "RasGAP",
    "SYGP1_HUMAN": "RasGAP",
    "RASA2_HUMAN": "RasGAP",
    "RASA3_RAT": "RasGAP",
    "GAP2_DROME": "RasGAP",
    "RASA3_BOVIN": "RasGAP",
    "RASL3_MOUSE": "RasGAP",
    "RAS4B_HUMAN": "RasGAP",
    "RASL3_BOVIN": "RasGAP",
    "RME6_DROME": "RasGAP",
    "RASA1_BOVIN": "RasGAP",
    "RME6_CAEBR": "RasGAP",
    "RME6_DROPS": "RasGAP",
    "RASA3_MOUSE": "RasGAP",
    "NGAP_HUMAN": "RasGAP",
    "NFAA_DICDI": "RasGAP",
    "RASL1_MOUSE": "RasGAP",
    "RASL1_HUMAN": "RasGAP",
    "RASL2_MOUSE": "RasGAP",
    "RASA2_MOUSE": "RasGAP",
    "RASA2_RAT": "RasGAP",
    "IRA1_YEAST": "RasGAP",
    "GAPD1_XENLA": "RasGAP",
    "BUD2_YEAST": "RasGAP",
    "GAP1_SCHPO": "RasGAP",
    "GAP1_CAEEL": "RasGAP",
    "GAP2_CAEEL": "RasGAP",
    "GAPD1_BOVIN": "RasGAP",
    "IQG1_CANAL": "RasGAP",
    "NGAP_DICDI": "RasGAP",
    "IRA2_YEAST": "RasGAP",
    "IQGA2_MOUSE": "RasGAP",
    "DAB2P_MOUSE": "RasGAP",
}