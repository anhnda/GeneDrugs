import os

C_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = "%s/out" % C_DIR
DrugBankDrugGenePath = "%s/data/DrugBankProteinGeneTarget.txt" % C_DIR


GENE_DRUG_JSON = "%s/GeneDrug.json" % OUT_DIR