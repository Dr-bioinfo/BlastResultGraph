## This script will generate bar plot for the a set of annoatated results ##Automated_code 

# commands : python Simreads_annotation_analysis_auto.py -d /path/to/the/directory -o /path/to/the/out_directory

import os
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
import argparse

parser = argparse.ArgumentParser("This code plots the annotated results (ID)")
input = parser.add_argument_group(title="Input Files", description="Enter the required input files")   
input.add_argument("-d", "--in_dir", action='store', dest='Indirr',help="path to FASTQ files" ) 
input.add_argument("-o", "--out_dir", action='store', dest='Outdirr',help="path to FASTQ files" ) 
args = parser.parse_args()
indir = args.Indirr
outdir = args.Outdirr

# Create the output directory if it doesn't exist
os.makedirs(outdir, exist_ok=True)

#directory = '/home/alphabox0006/Jerry/36_org_sample/result/blast_result2'  # Specify the directory path

# Iterate over files in the directory
for filename in os.listdir(indir):
    if filename.endswith('.csv'):  # Process only CSV files
        filepath = os.path.join(indir, filename)
        blast = pd.read_csv(filepath)
        
        # Update column names with special characters
        blast.columns = ['subject_com_names', 'Count_BestHit', 'Perc_Proportion', 'Total_BestHit']

         # Extract organism name from the filename
        organism_name = os.path.splitext(filename)[0]  # Removes the file extension

        blast['Organism'] = organism_name

        organism_name = blast['Organism'].unique()

        for i in organism_name:
            sns.set_style('white')
            plot = sns.FacetGrid(blast.loc[blast['Organism'] == i],
                                 sharex=False,
                                 sharey=True,
                                 height=4,
                                 aspect=1)
            plot.map(sns.barplot, 'subject_com_names', 'Perc_Proportion', order=blast.loc[blast['Organism'] == i]['subject_com_names'].unique(), color='#34495e')
            for ax in plot.axes.flat:
                for label in ax.get_xticklabels():
                    label.set_rotation(90)
                ax.axhline(10, ls='--', linewidth=0.5, color='red')

            plot.fig.suptitle(str(i))
            sns.set(font_scale=0.5)
            plt.tight_layout()
            ax.yaxis.set_major_locator(MultipleLocator(25))
            ax.set(ylim=(0,100))

            # Display and save the plot
            #plt.show()
            # Save the plot in the output directory
            output_filename = os.path.join(outdir, "Figure_" + str(i) + ".jpg")
            plt.savefig(output_filename, dpi=600, transparent=False)
            plt.close()

print("Plot Done")

## DOne 
# Good Day 
