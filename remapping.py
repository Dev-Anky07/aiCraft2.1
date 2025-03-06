import os
import glob

# Paths to annotation files
testset_annotations = '/Users/anky/Documents/GitHub/aiCraft/set1/train/labels/*.txt'
#testset_annotations = '/Users/anky/Documents/GitHub/aiCraft/set1/valid/labels/*.txt'
#dataset1_annotations = '/path/to/dataset1/labels/*.txt'
#dataset2_annotations = '/Users/anky/Documents/GitHub/aiCraft/Dataset2ObjDet/Labels/txt/*.txt'
#dataset3_annotations = '/path/to/dataset3/labels/*.txt'

# Mapping dictionaries (adjust based on your datasets)
testset_mapping = {0:6,1:1,2:2,3:3,4:2,5:4}
#dataset1_mapping = {0: 0, 1: 2, 2: 2, 3: 2, 4: 4, 5: 4, 6: 4, 7: 4, 8: 2, 9: 3, 10: 3}
#dataset2_mapping = {0: 3, 1: 7, 2: 0, 3: 8, 4: 6, 5: 6}
#dataset3_mapping = {0: 7, 1: 9, 2: 0, 3: 1, 4: 2, 5: 8, 6: 7, 7: 5, 8: 3, 9: 10, 10: 4, 11: 11}

# Function to update annotations
def update_annotations(annotation_path, mapping):
    for annotation_file in glob.glob(annotation_path):
        with open(annotation_file, 'r') as f:
            lines = f.readlines()
        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) == 0:
                continue
            class_id = int(parts[0])
            new_class_id = mapping[class_id]
            new_line = ' '.join([str(new_class_id)] + parts[1:]) + '\n'
            new_lines.append(new_line)
        with open(annotation_file, 'w') as f:
            f.writelines(new_lines)
            print(f'updated {class_id} to {new_class_id}\n')

# Update each dataset
update_annotations(testset_annotations,testset_mapping)
#update_annotations(dataset1_annotations, dataset1_mapping)
#update_annotations(dataset2_annotations, dataset2_mapping)
#update_annotations(dataset3_annotations, dataset3_mapping)
