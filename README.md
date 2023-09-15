# Automated Blast Analysis and Visualization

This Python script automates the process of generating bar plots for a set of annotated results, specifically designed for Blast count best hits results in CSV format. The primary aim of this script is to provide a versatile and automated solution for generating bar plots from Blast results, allowing users to visualize and analyze their data effortlessly.The aim of this script is to empower users to perform efficient and automated analysis of Blast count best hits results, making it suitable for a wide range of research and data visualization tasks.

## Command

To use this script, you can run the following command:

```
python Simreads_annotation_analysis_auto.py -d /path/to/the/directory -o /path/to/the/out_directory
```

## Command Line Arguments

- `-d` or `--in_dir`: Specify the path to the directory containing the CSV files with Blast count best hits annotated results.

- `-o` or `--out_dir`: Specify the path to the output directory where the generated bar plots will be saved.

## Workflow

1. The script iterates through the specified directory, processing only CSV files that contain Blast count best hits results.

2. It updates column names in the CSV files for proper visualization, ensuring compatibility with various Blast result formats.

3. For each unique organism identified in the dataset (extracted from the filenames), the script creates a dedicated bar plot. Each plot is organized by subject common names and their percentage proportions, providing valuable insights into the data.

4. To aid in data interpretation, the script adds a red dashed line at the 10% mark on the y-axis, serving as a visual reference.

5. The generated bar plots are saved as JPEG files in the specified output directory, with filenames labeled as "Figure_[Organism].jpg." This systematic approach ensures that users can easily locate and reference their results.

6. Upon completion, the script prints a confirmation message, indicating that the bar plot generation process is finished, and the resulting plots are available in the specified output directory.

### Have a GOOD DAY 🌻
