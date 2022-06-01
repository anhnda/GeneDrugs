import params
import utils
import json

def load_drugbank():
    f = open(params.DrugBankDrugGenePath)
    gene2drug = dict()
    while True:
        line = f.readline()
        if line == "":
            break
        line = line.strip()
        parts = line.split("|")
        drugId = parts[0]
        drugName = parts[1]
        targetInfos = parts[2].split("$")
        # print(targetInfos)
        for targetInfo in [targetInfos[0]]:
            if len(targetInfo) == 0:
                continue

            targets = targetInfo.split("__")
            for target in targets:
                ss = target.split("#")
                # print(ss)
                proId, proName, gene = ss[0], ss[1], ss[2]
                if len(gene) == 0:
                    continue
                else:
                    geneTarget = utils.get_insert_dict(gene2drug, gene, set())
                    geneTarget.add((drugId, drugName, proId, proName))
    f.close()
    return gene2drug

def export_json():
    gene2drug = load_drugbank()
    fo = open(params.GENE_DRUG_JSON, "w")
    for gene, drugs in gene2drug.items():
        target_info = []
        for drugInfo in drugs:
            drugId, drugName, proId, proName = drugInfo
            re = {"drug_id" : drugId,
                  "drug_name" : drugName,
                  "protein_uniprot": proId,
                  "protein_name" : proName}
            target_info.append(re)
        item = {"gene": gene, "drug_info": target_info}
        fo.write(json.dumps(item) + "\n")
    fo.close()
if __name__ == "__main__":
    utils.ensure_dir(params.OUT_DIR)
    export_json()
