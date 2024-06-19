#### 循环进行bin3和checkm筛选
import pandas as pd
import os

def read_hi_mag(qa):
    qa_matrix = pd.read_csv(qa, sep = "\t")
    hi_mags = qa_matrix[(qa_matrix["Completeness"]>=90) & (qa_matrix["Contamination"]<=10)]["Name"]
    return list(hi_mags)

def get_hi_contig(hi_mags_file):
    names = []
    with open(hi_mags_file, 'r') as file:
        for line in file:
            line = line.strip()
            # 如果一行以">"开头，将">"后面的内容添加到列表中
            if line.startswith('>'):
                names.append(line[1:].strip())
    return names

def print_list(c_list, outpath):
    with open(outpath, "w") as file:
        file.write("\n".join(c_list))

def mv_mf(mags, bins, prix):
    for i in mags:
        os.system("mv "+bins+i+".fna Hi_mags/" + prix + i + ".fna")
        

os.makedirs("tmp", exist_ok=True)
os.makedirs("Hi_mags", exist_ok=True)
bin_path = "bin3c_res/fasta/"
qafile = "bin3c_res/checkm/quality_report.tsv"
mv_mags = read_hi_mag(qafile)
mv_contigs = []
for i in mv_mags:
    mv_contigs += get_hi_contig(bin_path + i+".fna")
mv_contigs = [i.split(" ")[1][7:] for i in mv_contigs]
print_list(mv_contigs, "tmp/contigs.list")
mv_mf(mv_mags, bin_path, str(2))