"""Universe of tracked tickers."""

from typing import Dict, List

TICKERS: Dict[str, List[str]] = {
    "commodities": [
        "CL=F",
        "BZ=F",
        "NG=F",
        "TTF=F",
        "NCC=F",
        "LSPAAR",
        "HG=F",
        "LN1!",
        "SMM-Li",
        "CO1!",
        "U.U",
        "Polysilicon_Daqing",
        "ECFZ25",
        "FCEU3",
        "CCA",
        "^VIX",
    ],
    "integrated_oil_gas": [
        "XOM",
        "CVX",
        "BP",
        "SHEL",
        "TTE",
        "EQNR",
        "PBR",
        "OXY",
    ],
    "green_utilities_ipps": [
        "NEE",
        "ENEL.MI",
        "IBE.MC",
        "ORSTED.CO",
        "BEPC",
        "BEP",
    ],
    "solar_oems": ["FSLR", "ENPH", "JKS", "CSIQ"],
    "wind_oems": ["VWS.CO", "ENR.DE", "GE"],
    "batteries_ev": [
        "TSLA",
        "1211.HK",
        "300750.SZ",
        "373220.KS",
        "6752.T",
        "FREY",
    ],
    "hydrogen_fuel_cell": ["PLUG", "BLDP", "BE"],
    "mining_materials": ["ALB", "SQM", "FCX", "GLEN.L", "BHP", "RIO"],
    "carbon_capture_dac": ["ACC.OL"],
    "nuclear_smr_chain": ["CCJ", "KAP.L", "EDF.PA", "EXC"],
    "etfs": ["ICLN", "TAN", "FAN", "LIT", "URNM", "XLE"],
    "indices": ["^SPNY"],
    "risk_free": ["BIL"],
}

ALL_TICKERS: List[str] = [t for group in TICKERS.values() for t in group]
